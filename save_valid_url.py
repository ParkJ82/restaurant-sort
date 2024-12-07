from scrape_url_data import scrape_url_data
from parse_html import parse_html
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)
base_url = "https://map.naver.com/p/entry/place/"

# url: [query, 사업장명, 도로명주소]
# content: rating html, restaurant id, 종류
def save_valid_url(url, output_file, lock, count):
    """Validate and save URLs that meet specific conditions."""
    print(url[0])
    content = scrape_url_data(*url)
    count[0] += 1
    print(f"Count: {count[0]}")
    print(content[2])
    if content[0]:
        is_valid, first, third = parse_html(content[0].prettify())
        print(url[1], first, third)
        if is_valid:
            print(f"Valid: {url[0]} | Rating: {round(first/third, 1)}")
            with lock:
                output_file.write(f"{url[0]}, {content[1]} {content[2]} | Rating: {round(first/third, 1)}\n")
                output_file.flush()
                print(url[1], content[2], url[2], content[1])
            reponse = (supabase.table("restaurants").upsert({
                "name": url[1], 
                "rating": round(first / third, 1), 
                "category": content[2], 
                "address": url[2], 
                "url": base_url + str(content[1])
            }, on_conflict="url").execute())