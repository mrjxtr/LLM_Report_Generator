import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from dotenv import load_dotenv
import os

# -------- Load Environment Variables --------
load_dotenv()

# -------- Configurable Parameters from .env --------
URL = os.getenv("SCRAPE_URL")  # URL to scrape
OUTPUT_CSV = "output.csv"  # Output file name for CSV
TAG_TO_SCRAPE = "p"  # HTML tag to scrape
LOG_LEVEL = logging.INFO  # Logging level

# -------- Logging Configuration --------
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")


def fetch_static_page(url):
    """Fetch the content of a static webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Successfully fetched the content from {url}")
        return response.content
    except requests.RequestException as e:
        logging.error(f"Error fetching content from {url}: {e}")
        return None


def parse_static_page(content, tag_to_scrape):
    """Parse the content of a static webpage with BeautifulSoup."""
    try:
        soup = BeautifulSoup(content, "html.parser")
        elements = [element.text for element in soup.find_all(tag_to_scrape)]
        logging.info("Successfully parsed the webpage content")
        return elements
    except Exception as e:
        logging.error(f"Error parsing the webpage content: {e}")
        return []


def save_data_to_csv(data, filename):
    """Save extracted data to a CSV file."""
    df = pd.DataFrame(data, columns=[f"{TAG_TO_SCRAPE.capitalize()} Content"])
    df.to_csv(filename, index=False)
    logging.info(f"Data saved to {filename}")


if __name__ == "__main__":
    content = fetch_static_page(URL)
    if content:
        data = parse_static_page(content, TAG_TO_SCRAPE)
        save_data_to_csv(data, OUTPUT_CSV)
