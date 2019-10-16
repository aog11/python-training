# Chapter 11
# Image Site Downloader project

# Importing the needed modules
import requests, bs4, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Directory for the saved images
savedImgDir = ''

# Opening the site, choosing imgur
browser = webdriver.Chrome()
browser.get('http://imgur.com')

# Searching a topic
topic = 'lebron james'
topic_selector = browser.find_element_by_class_name('Searchbar-textInput')
topic_selector.send_keys(topic)
topic_selector.send_keys(Keys.ENTER)

# Requesting the resulting search
res = requests.get(browser.current_url)
soup = bs4.BeautifulSoup(res.text)

# Selecting and downloading the images
imagesList = soup.select('img')
for img in imagesList:
    # The images that end with b.jpg are thumbnails, I want the full images instead
    if img.get('src').endswith('b.jpg'):
        imgUrl = 'http:' + img.get('src').replace('b.jpg','.jpg')
    else:
        imgUrl = 'http:' + img.get('src')
    res = requests.get(imgUrl)
    savedImg = open(os.path.join(savedImgDir, os.path.basename(imgUrl)), 'wb')
    for chunk in res.iter_content(100000):
        savedImg.write(chunk)
    savedImg.close()