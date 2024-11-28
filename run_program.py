from restaurant_scrape import restaurant_scrape
from sort_text import sort_text

def main():
    output_path = restaurant_scrape()
    sort_text(output_path)
    print("Program successfully ran")

if __name__ == "__main__":
    main()