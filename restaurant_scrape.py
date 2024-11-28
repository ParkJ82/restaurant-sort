from load_valid_urls import load_valid_urls
import threading
from concurrent.futures import ThreadPoolExecutor
from save_valid_url import save_valid_url

def restaurant_scrape():
    search_term = input("Enter the search term: ")
    max_workers = int(input("Enter the number of workers: "))
    excluded_terms = {"까페", "카페", "커피", "커피집"}
    csv_path = 'restaurant.csv'
    output_path = f"restaurant_{search_term}.txt".replace(" ", "_")

    valid_urls = load_valid_urls(csv_path, search_term, excluded_terms)
    print(f"Collected {len(valid_urls)} valid URLs.")

    lock = threading.Lock()
    with open(output_path, "w", encoding="utf-8") as output_file:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(lambda url: save_valid_url(url, output_file, lock), valid_urls)

    print(f"Results saved to {output_path}")
    return output_path