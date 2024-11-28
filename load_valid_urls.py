import csv
from extract_district_neighborhood import extract_district_neighborhood
from is_valid_row import is_valid_row

def load_valid_urls(csv_path, search_term, excluded_terms):
    """Load and filter valid URLs from a CSV file."""
    with open(csv_path, encoding='cp949', errors='ignore') as file:
        return [
            (f"https://search.naver.com/search.naver?query={row['사업장명']}+{extract_district_neighborhood(row['지번주소'])}", row['사업장명'])
            for row in csv.DictReader(file)
            if is_valid_row(row, search_term, excluded_terms)
        ]