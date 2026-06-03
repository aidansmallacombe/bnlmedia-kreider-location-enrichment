from src._paths import ZIP_DB_PATH

import csv

def get_zip_dict():
    PA_target_counties = ["Philadelphia", "Montgomery", "Bucks", "Delaware", "Chester"]
    NJ_target_counties = ["Camden", "Burlington", "Gloucester", "Ocean", "Atlantic", "Cape May"]

    zip_dict = {}

    with open(ZIP_DB_PATH, "r", encoding="utf-8") as db:
        reader = csv.DictReader(db, delimiter=",")
        for row in reader:
            if row["state_id"] == "PA":
                if row["county_name"] in PA_target_counties:
                    zip_dict[row["zip"]] = {
                        "state" : row["state_id"],
                        "county": row["county_name"]
                    }
            if row["state_id"] == "NJ":
                if row["county_name"] in NJ_target_counties:
                    zip_dict[row["zip"]] = {
                        "state" : row["state_id"],
                        "county": row["county_name"]
                    }

    # testing
    # zip_dict = get_zip_dict()
    # print(len(zip_dict))
    # print(list(zip_dict.items())[:5])
    # print(zip_dict['19422'])

    return zip_dict

# get_zip_dict()



