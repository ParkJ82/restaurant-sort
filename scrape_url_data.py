from create_driver import create_driver
import time
from bs4 import BeautifulSoup
from retry_fetch import retry_fetch

def scrape_url_data(url, business_name):
    """Fetch and return content for a URL, with retry logic."""
    driver = create_driver()
    try:
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup.find('div', class_='_LCtS XCPfA') or retry_fetch(driver, business_name)
    except Exception as e: print(f"Error: {e}")
    finally: driver.quit()