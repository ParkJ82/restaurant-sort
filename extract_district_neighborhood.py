import re

def extract_district_neighborhood(address):
    """Extract and return the district and neighborhood from an address."""
    match = re.search(r'서울특별시\s([가-힣]+구\s[가-힣0-9]+동)[\d가-힣\s-]*', address)
    return match.group(1) if match else None