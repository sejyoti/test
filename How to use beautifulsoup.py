# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = 'https://commerce-app.gov.in/eidb/ecntcomq.asp'

# Make request and parse HTML
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find totals table
table = soup.find('table', id='tblData')

# Initialize dataframe
df = pd.DataFrame(columns=['Year', 'IndiaTotal'])

# Extract row data
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    year = cols[0].text.strip()
    total = cols[4].text.strip()[1:]

    # Remove commas
    total = total.replace(',', '')

    # Convert to float
    total = float(total)

    # Append to dataframe
    df = df.append({'Year':int(year), 'IndiaTotal':total}, ignore_index=True)

# Export dataframe to CSV
df.to_csv('india_data.csv', index=False)
