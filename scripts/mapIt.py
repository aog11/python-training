# Chapter 11
# Map It project

#! python3

# Importing the needed modules
import pyperclip, sys, webbrowser

# Taking the address as a command line argument or from the clipboard
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# Creating the URL for Google Maps
web_url = 'https://www.google.com/maps/place/%s' % (address.replace(' ','+'))

# Opening the URL
webbrowser.open(web_url)