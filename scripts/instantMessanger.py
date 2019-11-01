# Chapter 18
# Instant Messanger Bot

#! python3

# NOTE: I was already logged in Facebook while trying this script, so
# what it mainly does is to look for the specified friends and send them
# a message, but you need to already be authenticated before this works!

# Importing the needed modules
import os, time, pyautogui

# Locating the search bar image
imageDir = ''
os.chdir(imageDir)

# Giving me time to go to the browser
time.sleep(5)

# List with the friends to look for and message
friendsList = []

# Function to make the program wait for the website
def waitForWebsite():
    pyautogui.PAUSE = 1
    pyautogui.typewrite(['enter'])

# Messaging the friends
for friend in friendsList:
    # Locating the chats search bar
    searchBar = pyautogui.locateOnScreen('searchFriends.png')
    # Obtaining the coordinates
    x, y = pyautogui.center(searchBar)
    # Clicking the bar
    pyautogui.click(x,y)

    # Searching the friend
    pyautogui.typewrite(friend)
    waitForWebsite()

    # Message sent
    pyautogui.typewrite('Message sent from Python!')
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['esc'])
    
    # Confirmation in screen
    print('Messaged %s.' %(friend))

    # Moving the mouse out of the way
    pyautogui.moveTo(100,100)