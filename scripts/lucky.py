# Chapter 11
# Feeling Lucky Search project

#! python3

import requests, sys, webbrowser, bs4

sys.argv.append('odoo')

print ('Googling....')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,"html.parser")

# Open a browser tab for each result.
#linkElems = soup.select('.r a') Line of code in the book
linkElems = soup.select('div#main > div > div > div > a') # What worked after a web search
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))