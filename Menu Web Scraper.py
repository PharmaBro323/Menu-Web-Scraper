from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://univofminnesota.campusdish.com/LocationsAndMenus/ComstockDiningHall?locationId=2122&storeIds=&mode=Daily&periodId=2036&date=03%2F09%2F2020" 
       
try:
    page = urlopen(url)
except:
    print("Error opening the URL")
    
soup = BeautifulSoup(page, 'html.parser')

text = soup.find_all(text=True)

for content in soup.find_all('span', {"class": "item__name"}):
    print (content.text)

