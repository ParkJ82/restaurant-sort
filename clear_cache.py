from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import shutil
import os

# Define paths where WebDriverManager caches drivers
cache_dir = os.path.expanduser("~/.wdm")  # Default cache directory for WebDriverManager

# Clear WebDriverManager cache explicitly
def clear_cache():
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        print(f"Cache at {cache_dir} cleared successfully.")
    else:
        print(f"No cache found at {cache_dir}.")

# Setup ChromeDriver explicitly
def setup_driver():
    print("Setting up ChromeDriver...")
    driver_path = ChromeDriverManager().install()
    print(f"ChromeDriver installed at: {driver_path}")
    return driver_path

# Selenium Setup
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Clear the cache explicitly
clear_cache()

# Install ChromeDriver and get the path
driver_path = setup_driver()

# Initialize WebDriver temporarily to fetch the User-Agent
temp_driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
user_agent = temp_driver.execute_script("return navigator.userAgent;")  # Extract User-Agent dynamically
temp_driver.quit()

# Add the dynamically fetched User-Agent
chrome_options.add_argument(f"user-agent={user_agent}")

# Function to create a new driver instance
def create_driver():
    """Return a new Selenium WebDriver instance."""
    return webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# Example Usage
driver = create_driver()
driver.get("https://www.example.com")
print(driver.page_source)
driver.quit()
