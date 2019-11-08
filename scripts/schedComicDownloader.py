# Chapter 15
# Scheduled Web Comic Downloader Project
# Windows version

#! python3

# Importing the needed modules
import os, requests, bs4
from datetime import datetime
from time import time

# Getting the current date
currDate = datetime.fromtimestamp(time())
currDate = currDate.strftime('%d-%m-%Y')

# Going to the directory to download the comic
comicsDir = ''
os.chdir(comicsDir)

# Creating the folder for the comic's date
os.makedirs(currDate, exist_ok=True)
os.chdir(currDate)

# Downloading the comic webpage
comicUrl = 'http://theawkwardyeti.com/'
res = requests.get(comicUrl)
webData = bs4.BeautifulSoup(res.text)

# Checking if there's a next comic
nextComic = webData.select('.navi.navi-next.navi-void')

# You're at the latest one
if not nextComic == []:
    # Downloading the cover image
    comic = webData.select('#comic img')
    res = requests.get(comic[0].get('src'))
    # Getting the extension of the image
    imgExtension = os.path.splitext(comic[0].get('src'))[1]
    with open('cover_theawkwardyeti_%s%s'%(currDate,imgExtension),'wb') as imageFile:
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
    # Downloading the rest of the comic
    comics = webData.select('.entry p img')
    for i in range(len(comics)):
        res = requests.get(comics[i].get('src'))
        comicName = os.path.basename(comics[i].get('src'))
        with open(comicName,'wb') as ImageFile:
            for chunk in res.iter_content(100000):
                ImageFile.write(chunk)