from src import extract_locations
from src import zip_lookup
from src._paths import LOCATIONS_CSV_PATH, COUNTY_AGG_CSV_PATH, RETAIL_AGG_CSV_PATH, DB_PATH

import csv
import sqlite3

locations = extract_locations.get_locations()
zips = zip_lookup.get_zip_dict()
filtered_locations = []

for loc in locations:
    zip_code = loc["zip"]

    if zip_code in zips:
        loc["county"] = zips[zip_code]["county"]
        filtered_locations.append(loc)

locations = filtered_locations

# testing
# print(locations[0]["county"])
# print(len(zips))
# print(locations[0]["zip"])
# print(locations[0]["zip"] in zips)
# print(len(locations)) -> total number of distributors in target counties: 767

# writer for distibutor legend csv
with open(LOCATIONS_CSV_PATH, "w", newline="", encoding="utf-8") as loc_table:
    fieldnames = ["location_id", "retailer_group", "address", "city", "state", "zip", "county"]
    dict_writer = csv.DictWriter(loc_table, fieldnames=fieldnames)

    # write locations data to csv - success!
    dict_writer.writeheader()
    for loc in locations:
        dict_writer.writerow(loc)

# sqlite3 connection setup
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# drop table before each run to avoid error
cur.execute("drop table if exists locations")

# create table
cur.execute("create table locations(location_id, retailer_group, address, city, state, zip, county)")

# insert into table
for loc in locations:
    cur.execute(
        """
        insert into locations (location_id, retailer_group, address, city, state, zip, county)
        values (?, ?, ?, ?, ?, ?, ?)
        """,
        (loc["location_id"],loc["retailer_group"], loc["address"], loc["city"], loc["state"], loc["zip"], loc["county"])
    )

conn.commit()

# query: aggregate by county
cur.execute("""
            select county, state, count(*) as distributor_count 
            from locations
            group by county
            order by state, county
            """)

# fetch query result and write
county_counts = cur.fetchall()

with open(COUNTY_AGG_CSV_PATH, "w", newline="", encoding="utf-8") as county_table:
    county_writer = csv.writer(county_table)

    county_writer.writerow(["county", "state", "distributor_count"])

    for county, state, count in county_counts:
        county_writer.writerow([county, state, count])

# query: aggregate by retailer (location_id)
cur.execute("""
            select retailer_group, count(*) as distributor_count 
            from locations
            group by retailer_group
            order by retailer_group
            """)

retail_counts = cur.fetchall()

with open(RETAIL_AGG_CSV_PATH, "w", newline="", encoding="utf-8") as retail_table:
    retail_writer = csv.writer(retail_table)

    retail_writer.writerow(["retailer_group", "distributor_count"])

    for retail, count in retail_counts:
        retail_writer.writerow([retail, count])

conn.close()

    