import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#random number between 1 and 21
number = random.randrange(1,22)

#complete the rest of the URL
if number <= 9:
    url = 'https://ebible.org/asv/JHN0' + str(number) + '.htm'
else:
    url = 'https://ebible.org/asv/JHN'+ str(number) +'.htm'

#webpage = 'https://ebible.org/asv/JHN'
#print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
title = soup.title
print(title.text)
table_rows = soup.findAll("tr")

# work through page to find paragraph then find verse within the paragraph

#random verse from random page

page_verses = soup.findAll('div', class_= 'p')

my_verses = []

for section_verses in page_verses:
    verse_list = section_verses.text.split(".")

    for v in verse_list:
        my_verses.append(v)

my_verses = [i for i in my_verses if i != ' ']

my_choice = random.choice(my_verses)

print()
print(f"Chapter: {number}")
print(f"Verse: {my_choice}")
print()
