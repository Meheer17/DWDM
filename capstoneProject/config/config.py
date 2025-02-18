import os

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Output file path
OUTPUT_JSON_PATH = os.path.join(DATA_DIR, "scraped_data.json")

# List of website links to scrape
WEBSITE_LINKS = [
    "https://meheer.vercel.app",
]