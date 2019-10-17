# Chapter 11
# Link Verification Project

# Importing the needed modules
import requests, requests.exceptions, bs4, os

# Setting the URL
url = 'http://weather.gov'

# Requesting the URL
res = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
soup = bs4.BeautifulSoup(res.text)
links = soup.select('a')

# Verifying the links
for link in links:
    newURL = link.get('href')
    try:
        res = requests.get(newURL, headers = {'User-agent': 'your bot 0.1'})
        res.raise_for_status()
    except Exception as exc:
        print ('Link %s does not exist.' % (newURL))