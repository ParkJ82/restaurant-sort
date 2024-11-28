import time
from bs4 import BeautifulSoup

def retry_fetch(driver, business_name):
    """Retry fetching content for a business using a fallback URL."""
    driver.get(f"https://search.naver.com/search.naver?query={business_name}")
    time.sleep(3)
    return BeautifulSoup(driver.page_source, 'html.parser').find('div', class_='place_section_content')