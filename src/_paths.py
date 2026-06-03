from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
REFERENCE_DIR = DATA_DIR / "reference"
OUTPUT_DIR = ROOT_DIR / "outputs"

RAW_HTML_PATH = RAW_DIR / "locations_src.html"
ZIP_DB_PATH = REFERENCE_DIR / "simplemaps_uszips_basicv1.94" / "uszips.csv"

LOCATIONS_CSV_PATH = OUTPUT_DIR / "kf_enriched_distributor_locations.csv"
COUNTY_AGG_CSV_PATH = OUTPUT_DIR / "kf_distributors_county_agg.csv"
RETAIL_AGG_CSV_PATH = OUTPUT_DIR / "kf_distributors_retail_agg.csv"
DB_PATH = OUTPUT_DIR / "locations.db"