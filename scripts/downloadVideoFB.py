# Facebook video downloader

#! python3

# Importing the needed modules
import requests, re, os

# Facebook URL of the video
facebookURL = ''
# Requesting that URL
res = requests.get(facebookURL)
# Looking for the text that contains the URL of the video
videoURL = re.search('hd_src:"(.+?)"', res.text).group(1)
# Requesting the actual video
res = requests.get(videoURL)

# Changing to the directory to place the video
os.chdir('')

# Downloading the video
with  open('video.mp4','wb') as Video:
    for chunk in res.iter_content(100000):
        Video.write(chunk)