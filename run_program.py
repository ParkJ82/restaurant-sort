from restaurant_scrape import restaurant_scrape
from sort_text import sort_text
from clear_cache import run_clear_cache

def main():
    run_clear_cache()
    output_path = restaurant_scrape()
    sort_text(output_path)
    print("Program successfully ran")

if __name__ == "__main__":
    main()