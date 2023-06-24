
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.example.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = []
for item in soup.find_all('div', {'class': 'item'}):
    name = item.find('h2').text
    price = item.find('span', {'class': 'price'}).text
    data.append([name, price])

df = pd.DataFrame(data, columns=['Name', 'Price'])
df.to_csv('data.csv', index=False)

df2 = pd.read_csv('https://example.com/large_data.csv')