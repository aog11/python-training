# Chapter 11
# Download XKCD comics project

#! python3

import os, requests, bs4

url = 'http://xkcd.com' # starting url
# create the dir
mkdir = ''
os.makedirs(mkdir, exist_ok=True) # store comics here
# change to that directory
os.chdir(mkdir)
dir = os.getcwd()

while not url.endswith('#'):
    # Download the page
    print('Downloading the page')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         try:
             comicUrl = 'http:' + comicElem[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             continue
            
    # Save the image to ./xkcd.
    imageFile = open(os.path.join(dir, os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')