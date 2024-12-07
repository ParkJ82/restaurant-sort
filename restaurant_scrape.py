from load_valid_urls import load_valid_urls
import threading
from concurrent.futures import ThreadPoolExecutor
from save_valid_url import save_valid_url
import os

def restaurant_scrape():
    search_term = input("Enter the search term: ")
    max_workers = int(input("Enter the number of workers: "))
    start_index = int(input("Enter the starting index: "))
    excluded_terms = {"까페", "카페", "커피", "커피집"}
    csv_path = 'restaurant.csv'
    output_path = f"restaurant_{search_term}.txt".replace(" ", "_")

    valid_urls = load_valid_urls(csv_path, search_term, excluded_terms)
    if start_index >= len(valid_urls):
        print("Starting index is out of range.")
        return

    # Slice the list to start from the given index
    valid_urls = valid_urls[start_index:]
    print(f"Collected {len(valid_urls)} valid URLs starting from index {start_index}.")

    # Initialize the counter with the starting index
    count = [start_index]

    lock = threading.Lock()
    # Open the file in append mode to avoid clearing it
    with open(output_path, "a", encoding="utf-8") as output_file:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(lambda url: save_valid_url(url, output_file, lock, count), valid_urls)

    print(f"Results saved to {output_path}")
    return output_path
