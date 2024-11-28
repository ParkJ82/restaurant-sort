from bs4 import BeautifulSoup

def parse_html(input_html):
    """Validate content and extract numerical conditions from HTML."""
    soup = BeautifulSoup(input_html, 'html.parser')
    items = soup.find_all('li', class_='avHEe')
    if len(items) < 3: return False, None, None
    try:
        first = int(''.join(filter(str.isdigit, items[0].find('span', class_='dDRIH').get_text(strip=True))))
        third = int(''.join(filter(str.isdigit, items[2].find('span', class_='dDRIH').get_text(strip=True))))
        return (first >= 500 and first / third >= 3.0), first, third
    except (AttributeError, ValueError): return False, None, None