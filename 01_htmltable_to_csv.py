import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.in2013dollars.com/bitcoin-price').content
soup = BeautifulSoup(response, 'html.parser')

# find all alternative
# table = soup.find_all("table", {"class": "table table-striped"})[0]
table = soup.table
theaders = table.find_all('th')
trows = table.find_all('tr')
headers = [header.text for header in theaders]
rows = []


for trow in trows[1:]:
    td = trow.find_all('td')
    row = [i.text for i in td]
    rows.append(row)


dataFrame = pd.DataFrame(data = rows, columns = headers)
print(dataFrame)
dataFrame.to_csv('lab1.csv', index=False)