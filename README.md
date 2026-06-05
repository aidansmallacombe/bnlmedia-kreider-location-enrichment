# Overview:
This is a small Python ETL pipeline developed for BNL Media Vantures intended to support market research for their prospective client Kreider Farms.

Kreider Farms is a privately-owned farmstead located in Manheim, PA. They sell dairy and egg products to over 2,400 distributor locations across the US. BNL Media Ventures was interested in sourcing location-based data for distributors within 11 target counties in the Greater Philadelphia Region and Southern New Jersey.

The objective was to determine:
The number of Kreider distributor locations by county within the target counties
The number of Kreider distributor locations by retailers within the target counties

# Data Sources:
- Kreider Farms public distributor locator: https://www.kreiderfarms.com/locations/
- SimpleMaps US ZIP Code Database: https://simplemaps.com/data/us-zips (see data/README.md for more)

# ETL:

### Extract:
Distributor location data was extracted from ‘locations_src.html’, a response returned from a network request on the distributor locator webpage. Location records were contained directly in a large Javascript object ‘_mapLocations’.

### Transform:
Location records were parsed and normalized before being formatted into a json dictionary with fields containing the location’s ID, retail group, address information, and county (which was blank because county data was not recorded).

To determine the county of the locations, zip codes from the location records were cross-matched with entries in the SimpleMaps US zip code database, which contained county data. Location records were updated with county info, and then filtered to only include records in target counties.

# Load:
The location records were written to a CSV and loaded into SQLite as a database. Aggregation queries were created to count the number of locations per county and per retailer. Both query results were written to CSV’s, all three files can be found in the ‘outputs’ directory.

# Results:
- 2,429 distributor locations recorded
- 767 distributor locations found in 11 target counties
- CSV recording location data for all 767 target distributor locations
- CSV recording number of locations per target county
- CSV recording number of locations per retailer within target counties

# Technologies:

- Python
- SQLite
- CSV Processing
- JSON Parsing
- Regular Expressions
- ETL Data Pipelines
