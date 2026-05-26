# 🇳🇬 Scraping Nigeria's Largest Companies from Wikipedia

## Overview

This project demonstrates end-to-end web scraping using **BeautifulSoup** and **Requests**, with data storage and structuring handled by **Pandas**. The target data is a Wikipedia table listing the 25 largest companies in Nigeria by revenue.

---

## Tools & Libraries

| Library | Purpose |
|---|---|
| `requests` | Fetching the raw HTML from Wikipedia |
| `BeautifulSoup` | Parsing and navigating the HTML structure |
| `pandas` | Structuring scraped data into a DataFrame and exporting to CSV |

---

## Project Workflow

### 1. Fetch the Web Page
A `GET` request is sent to the Wikipedia URL with a browser-style `User-Agent` header to avoid request blocks.

```python
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Nigeria'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
```

### 2. Locate the Target Table
BeautifulSoup's `find()` method targets the first `wikitable sortable` table on the page, which contains the revenue rankings.

```python
table = soup.find('table', class_='wikitable sortable')
```

### 3. Extract Column Headers
All `<th>` header tags are found and their text content is stripped into a clean list.

```python
table_headings = table.find_all('th')
table_columns = [heading.text.strip() for heading in table_headings]
```

### 4. Extract Row Data
Each `<tr>` row (skipping the header row) is iterated, and the `<td>` cell values are extracted and appended to a list.

```python
column_data = table.find_all('tr')
data = []
for row in column_data[1:]:
    row_data = row.find_all('td')
    cell = [data.text.strip() for data in row_data]
    data.append(cell)
```

### 5. Build DataFrame and Export
The data list is loaded into a Pandas DataFrame using the extracted headers, then saved as a CSV file.

```python
import pandas as pd

df = pd.DataFrame(data, columns=table_columns)
df.to_csv('Top_Nigeria_company.csv', index=False)
```

---

## Output

A clean, structured dataset of **25 companies** with the following fields:

| Column | Description |
|---|---|
| Rank | Company ranking by revenue |
| Company | Company name |
| Industry | Sector (Oil & Gas, Telecoms, Agroindustry, etc.) |
| Revenue (US$ millions) | Annual revenue in USD millions |
| Profits (US$ millions) | Annual profits in USD millions |

**Sample rows:**

| Rank | Company | Industry | Revenue | Profits |
|---|---|---|---|---|
| 1 | Nigeria National Petroleum | Oil and gas | 9,706 | 1,877 |
| 3 | MTN Nigeria | Telecommunications | 3,514 | 536 |
| 4 | Dangote Cement | Cement | 2,699 | 721 |

---

## Key Concepts Demonstrated

- Setting request headers to mimic browser behaviour
- Navigating HTML with `find()` and `find_all()`
- List comprehension for clean data extraction
- DataFrame construction from scraped lists
- Exporting structured data to CSV with `to_csv()`

---

## Skills

`Python` `BeautifulSoup` `Requests` `Pandas` `Web Scraping` `Data Collection`
