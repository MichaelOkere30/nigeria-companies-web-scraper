from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Nigeria'
# 1. Define a standard browser User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', class_='wikitable sortable')
table_headings = table.find_all('th')
table_columns = [heading.text.strip() for heading in table_headings]
column_data = table.find_all('tr')
data1=[]
for row in column_data[1:]:
    row_data = row.find_all('td')
    cell = [data.text.strip() for data in row_data]
    data1.append(cell)
import pandas as pd
df = pd.DataFrame(data1, columns=table_columns)
print(df)
