import requests
from bs4 import BeautifulSoup
from config.config import WEBSITE_LINKS

def scrape_website(url):
    """
    Scrape data from a single website.
    """
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract all text from <p> tags
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

        # Return structured data
        return {
            "url": url,
            "paragraphs": paragraphs
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

def scrape_all_websites():
    """
    Scrape data from all websites in the config.
    """
    scraped_data = []
    for url in WEBSITE_LINKS:
        print(f"Scraping {url}...")
        data = scrape_website(url)
        if data:
            scraped_data.append(data)
    return scraped_data