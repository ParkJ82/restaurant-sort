from create_driver import create_driver
import time
from bs4 import BeautifulSoup
import re

def extract_additional_data(soup):
    """Extract href number and lnJFt text."""
    href_number = None
    lnJFt_text = None
    
    # Extract the href number (after /place/)
    href_element = soup.find('div', class_='LylZZ').find('a', href=True)
    if href_element:
        href = href_element['href']
        match = re.search(r'/place/(\d+)', href)
        if match:
            href_number = match.group(1)
    
    # Extract the text inside lnJFt
    lnJFt_element = soup.find('span', class_='lnJFt')
    if lnJFt_element:
        lnJFt_text = lnJFt_element.text
    
    return href_number, lnJFt_text

def retry_fetch(driver, business_name):
    """Retry fetching content for a business using a fallback URL."""
    driver.get(f"https://search.naver.com/search.naver?query={business_name}")
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find main content
    main_content = soup.find('div', class_='place_section_content')
    if not main_content:
        return None, None, None
    
    # Extract additional data
    href_number, lnJFt_text = extract_additional_data(soup)

    return main_content, href_number, lnJFt_text

def scrape_url_data(url, business_name, address):
    """Fetch and return content for a URL, with retry logic."""
    driver = create_driver()
    try:
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Try to find main content
        main_content = soup.find('div', class_='_LCtS XCPfA')
        if not main_content:
            # If main content is not found, retry and extract data there
            return retry_fetch(driver, business_name)
        
        # Extract additional data from main content
        href_number, lnJFt_text = extract_additional_data(soup)

        return main_content, href_number, lnJFt_text

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None
    finally:
        driver.quit()