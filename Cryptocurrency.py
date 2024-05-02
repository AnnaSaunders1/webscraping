from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://crypto.com/price'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text)

cc_data = soup.findAll("div", attrs={"class": "table-cell"})

counter = 2
for x in range(5):

    
    name = cc_data[counter].text
    last_price = float(cc_data[counter+1].text)
    change = float(cc_data[counter+1].text.strip('%'))
    previous_price = round(last_price / (1 + change/100),2)
    
    print()
    print(f'Company Name: {name}')
    print(f"Change: {change}")
    print(f"Price: {last_price}")
    print(f"Previous Prive: {previous_price}")
    print()

    counter += 6



#display


