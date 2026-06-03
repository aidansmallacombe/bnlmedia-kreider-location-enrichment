from src._paths import RAW_HTML_PATH

import re
import json

def get_locations():
    with open(RAW_HTML_PATH, "r", encoding="utf-8") as file:
        text = file.read()

    # search text for regex pattern to find object "_mapLocations"
    match = re.search(r"var _mapLocations\s*=\s*(\{.*?\});", text, re.DOTALL)

    match_res = match.group(1)
    # print(locations[:10000] + "\n")
    # print(locations[-1000:])

    loc_dict = json.loads(match_res)
    # print(type(loc_dict))
    # print(len(loc_dict))

    # dict contains other attributes outside of location data
    # "locations" will contain pure location data
    locations = []

    for location_id, store_data in loc_dict.items():

        # establish structure for necessary data
        loc = {
            "location_id": "",
            "retailer_group": "",
            "address": "",
            "city": "",
            "state": "",
            "zip": "",
            "county": ""
        }

        # location_id marked by the "post_title" attribute
        loc["location_id"] = store_data["post_title"]
        loc["retailer_group"] = normalize_retail_group(store_data["post_title"])

        # address data stored in "location_meta" attribute
        meta = store_data["location_meta"]

        loc["address"] = meta["address"]
        loc["city"] = meta["city"]
        loc["state"] = meta["state"]
        loc["zip"] = meta["zip"]

        # append location dict to list
        locations.append(loc)

    # print(len(locations))
    # print(locations[0:5])
    return locations

# normalize retail_group attribute for easier retail counts
def normalize_retail_group(name):
    name = name.upper().strip()

    name = re.sub(r"#\d+", "", name)
    name = re.sub(r"\s*-\s*.*$", "", name)
    name = re.sub(r"\s*\(\s*.*\)$", "", name)
    name = name.replace(" STORE", "")
    name = name.strip()

    if "ACME" in name:
        return "ACME"
    if "GIANT" in name:
        return "GIANT"

    return name

# get_locations()
    
        






