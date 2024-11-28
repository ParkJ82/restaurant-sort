from scrape_url_data import scrape_url_data
from parse_html import parse_html

def save_valid_url(url, output_file, lock):
    """Validate and save URLs that meet specific conditions."""
    content = scrape_url_data(*url)
    if content:
        is_valid, first, third = parse_html(content.prettify())
        if is_valid:
            with lock:
                output_file.write(f"{url[0]} | Rating: {round(first/third, 1)}\n")
                output_file.flush()
            print(f"Valid: {url[0]} | Rating: {round(first/third, 1)}")