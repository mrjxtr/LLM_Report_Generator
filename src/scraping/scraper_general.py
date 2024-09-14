import scrapy
from dotenv import load_dotenv
import os

# -------- Load Environment Variables --------
load_dotenv()

# -------- Configurable Parameters from .env --------
START_URLS = [os.getenv("SCRAPE_URL")]
TAG_TO_SCRAPE = "p::text"  # CSS Selector for scraping
OUTPUT_FORMAT = "json"  # Output format (json, csv, xml)


class GeneralSpider(scrapy.Spider):
    name = "general_spider"
    start_urls = START_URLS

    def parse(self, response):
        elements = response.css(TAG_TO_SCRAPE).getall()
        yield {f"{TAG_TO_SCRAPE}": elements}


# Run the spider: scrapy runspider scraper_general.py -o output.<OUTPUT_FORMAT>
