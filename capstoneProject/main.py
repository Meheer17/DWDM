from data_ingestion.web_scraper import scrape_all_websites
from data_processing.data_cleaner import clean_data
from data_storage.json_writer import save_to_json

def main():
    # Step 1: Scrape data from websites
    scraped_data = scrape_all_websites()
    
    # Step 2: Clean the scraped data
    cleaned_data = clean_data(scraped_data)
    
    # Step 3: Save cleaned data to JSON
    if cleaned_data:
        save_to_json(cleaned_data)

if __name__ == "__main__":
    main()