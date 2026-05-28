"""
Nigeria Largest Companies Scraper
----------------------------------
Scrapes the list of largest companies in Nigeria from Wikipedia
and exports the data to a CSV file.
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup


# --- Constants ---
URL = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Nigeria'
OUTPUT_FILE = 'data/Top_Nigeria_company.csv'
HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    )
}


def fetch_page(url: str, headers: dict) -> BeautifulSoup:
    """Fetch the webpage and return a BeautifulSoup object."""
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')


def extract_table(soup: BeautifulSoup) -> pd.DataFrame:
    """Extract the first wikitable from the page and return a DataFrame."""
    table = soup.find('table', class_='wikitable sortable')

    # Extract column headers
    columns = [th.text.strip() for th in table.find_all('th')]

    # Extract row data
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = [td.text.strip() for td in row.find_all('td')]
        if cells:
            rows.append(cells)

    return pd.DataFrame(rows, columns=columns)


def save_to_csv(df: pd.DataFrame, filepath: str) -> None:
    """Save the DataFrame to a CSV file."""
    df.to_csv(filepath, index=False)
    print(f"Data saved to '{filepath}'")


def main():
    print("Fetching page...")
    soup = fetch_page(URL, HEADERS)

    print("Extracting table data...")
    df = extract_table(soup)

    print(df.to_string(index=False))

    save_to_csv(df, OUTPUT_FILE)


if __name__ == '__main__':
    main()
