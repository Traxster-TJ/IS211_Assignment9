import requests
from bs4 import BeautifulSoup

# Send a request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')


table = soup.find('table', class_='wikitable')

# Print the header
print("Super Bowl Champions")
print("-" * 70)
print(f"{'Season':<8} {'SB':<5} {'Winner':<25} {'Score':<10} {'Loser':<25}")
print("-" * 70)

# Find all rows
rows = table.find_all('tr')[1:]  # Skip the header row


for row in rows:
    cells = row.find_all(['td', 'th'])
    if len(cells) >= 5:
        season = cells[0].text.strip()
        sb = cells[1].text.strip()
        winner = cells[2].text.strip()
        score = cells[3].text.strip()
        loser = cells[4].text.strip()
        
        print(f"{season:<8} {sb:<5} {winner:<25} {score:<10} {loser:<25}"
