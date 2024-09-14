from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import logging
from dotenv import load_dotenv
import os

# -------- Load Environment Variables --------
load_dotenv()

# -------- Configurable Parameters from .env --------
URL = os.getenv("SCRAPE_URL")  # URL to scrape
OUTPUT_EXCEL = "output.xlsx"  # Output file name for Excel
TAG_TO_SCRAPE = "p"  # HTML tag to scrape
LOG_LEVEL = logging.INFO  # Logging level

# -------- Logging Configuration --------
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")


def setup_driver(headless=True):
    """Set up the Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver


def fetch_dynamic_content(url, tag_to_scrape):
    """Fetch the content of a dynamic webpage using Selenium."""
    driver = setup_driver()
    try:
        driver.get(url)
        logging.info(f"Successfully accessed {url}")
        elements = driver.find_elements(By.TAG_NAME, tag_to_scrape)
        data = [element.text for element in elements]
        return data
    except Exception as e:
        logging.error(f"Error fetching content from {url}: {e}")
        return []
    finally:
        driver.quit()


def save_data_to_excel(data, filename):
    """Save extracted data to an Excel file."""
    df = pd.DataFrame(data, columns=[f"{TAG_TO_SCRAPE.capitalize()} Content"])
    df.to_excel(filename, index=False)
    logging.info(f"Data saved to {filename}")


if __name__ == "__main__":
    data = fetch_dynamic_content(URL, TAG_TO_SCRAPE)
    save_data_to_excel(data, OUTPUT_EXCEL)
