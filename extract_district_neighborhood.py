import re

def extract_district_neighborhood(address):
    """Extract and return the district and the next word from an address."""
    match = re.search(r'서울특별시\s([가-힣]+구\s[^\s]+)', address)
    return match.group(1) if match else None