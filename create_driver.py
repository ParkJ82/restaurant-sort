from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Selenium Setup
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")  # Add headless mode

# Initialize WebDriver temporarily to fetch the User-Agent
temp_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
user_agent = temp_driver.execute_script("return navigator.userAgent;")  # Extract User-Agent dynamically
temp_driver.quit()

# Add the dynamically fetched User-Agent
chrome_options.add_argument(f"user-agent={user_agent}")

def create_driver():
    """Return a new Selenium WebDriver instance."""
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
