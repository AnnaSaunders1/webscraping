import requests
import json
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font
from urllib.request import urlopen, Request
from plotly.graph_objs import Bar
from plotly import offline

webpage = 'https://quotes.toscrape.com/page/{}/'

# assign variables
tags_dict = {}
authors = {}
quote_lengths = []
max_length = 0
min_length = 100
top_authors = []
tags_list = []

## Cycle through pages to gather information
page = 1
for page in range(1,11):
    ##   Open the website in python 	
    url = f"https://quotes.toscrape.com/page/{page}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    response = requests.get(url)
    req = Request(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Gather quotes
    quotes = soup.findAll('div', class_="quote")
    
    # Gather the variable information
    for quote in quotes: 

        for x in soup.findAll('div class="tags"'):
            tag = soup.findAll('a class="tag"')
            tags.append(tag)

        # Gather Author data
        author = soup.find('small', class_="author").text
        if author in authors:
            authors[author] += 1
        else:
            authors[author] = 1            

        # Gather Quote Data
        quote_txt = soup.find('span', class_="text").text
        length = len(quote)
        quote_lengths.append(length)
        if length > max_length:
            longest = quote_txt
            longest_author = author
        if length < min_length:
            shortest = quote_txt
            shortest_author = author

        # Gather Tag Data
        tags = quote.find('div', class_="tags").findAll('a', class_='tag')
        for tag in tags:
            text = tag.text

            if text in tags_dict:
                tags_dict[text] += 1
            else:
                tags_dict[text] = 1

            if text not in tags_list:
                tags_list.append(text)

#### Print Information

print()
print('Author Data:')

print()
print('Authors and Quote Counts:')
for k,y in authors.items():
    print(f'Author: {k}   Quotes: {y}')

print()
print('Author with the most quotes:')
highest_count = max(authors.values())
for k,y in authors.items():
    if y == highest_count:
        print(f'Author: {k}   Quotes: {y}')

print()
print('Author with the lease quotes:')
least_count = min(authors.values())
for k,y in authors.items():
    if y == highest_count:
        print(f'Author: {k}   Quotes: {y}')

print()   
print('Quote Data:')    
print()

#find quote length average
avg_length = int(sum(quote_lengths) / len(quote_lengths))
print(f'Average Quote length: {avg_length}')
print()

#Longest Quote
print('Longest Quote:')
print(longest)
print(f'Author: {longest_author}')
print()

#Shortest Quote
print('Shortest Quote:')
print(shortest)
print(f'Author: {shortest_author}')
print()

print()
print('Tag Data:')
print()

#the most popular tag
print('Most popular tag:')
popular = max(tags_dict.values())
for k,y in tags_dict.items():
    if y == popular:
        print(f'Tag: {k}   Uses: {y}')

#amount of tags
print()
print(f'Total Tags Used: {len(tags_dict)}')
print


##   Visualization

# top 10 authors
graph_authors = []
graph_counts = []
counter = 1
if counter < 11:
    for k,y in authors.items():
        graph_authors.append(k)
        graph_counts.append(y)

data = [
    {
        "type": "bar",
        "x": graph_authors,
        "y": graph_counts,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {"width": 1.5, "color": "rgb(25,25,25)"},
            },
        "opacity": 0.6,
    }
]

my_layout = {
    "title": "Top 10 Authors",
    "xaxis": {"title": "Authors"},
    "yaxis": {"title": "Number of Quotes"}
}

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="TopAuthors.html")


# top 10 tags


graph_tags = []
graph_counts = []
counter = 1

for tag in tags_list[:10]:
    graph_tags.append(tag)

for k,y in tags_dict.items():
    if k in graph_tags:
        graph_counts.append(y)

data = [
    {
        "type": "bar",
        "x": graph_tags,
        "y": graph_counts,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {"width": 1.5, "color": "rgb(25,25,25)"},
            },
        "opacity": 0.6,
    }
]

my_layout = {
    "title": "Top 10 Tags",
    "xaxis": {"title": "Tags"},
    "yaxis": {"title": "Count"}
}

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="TopTags.html")
