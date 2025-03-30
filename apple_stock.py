# apple_stock.py
# scrapes Apple's historical stock data from Yahoo Finance
# URL: https://finance.yahoo.com/quote/AAPL/history?p=AAPL

import requests
from bs4 import BeautifulSoup

# Send a request to Yahoo Finance
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')

# table containing the stock data
table = soup.find('table', {'data-test': 'historical-prices'})

#print
print("Apple (AAPL) Historical Stock Data")
print("-" * 50)
print(f"{'Date':<15} {'Close Price':<15}")
print("-" * 50)

# Check table
if table:
    # Find all rows in the table body
    rows = table.find('tbody').find_all('tr')
    
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 5:
            date = cells[0].text.strip()
            close_price = cells[4].text.strip()  # The 5th column contains the closing price
            
            print(f"{date:<15} {close_price:<15}")
else:
    print("Table not found.")
    print("Try updating the script or manually checking the URL.")
