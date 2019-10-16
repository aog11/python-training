# Chapter 11
# 2048 game Project

# Importing the modules I need
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time, selenium.common.exceptions

# Opening the website
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

# Play the game five times and send the socres
scores = []
for t in range(5):
    # Sending random keys
    game = browser.find_element_by_tag_name('html')

    while True:
        key = random.randint(1,4)

        if key == 1:
            game.send_keys(Keys.UP)
        elif key == 2:
            game.send_keys(Keys.DOWN)
        elif key == 3:
            game.send_keys(Keys.LEFT)
        else:
            game.send_keys(Keys.RIGHT)
        
        # Breaking the loop once the game's over
        try:
            game_over = browser.find_element_by_css_selector("div[class='game-message game-over']")
            break
        except selenium.common.exceptions.NoSuchElementException:
            pass

    # Saving the score
    time.sleep(1)
    scores.append(browser.find_element_by_css_selector("div[class='score-container']").text)
    time.sleep(1.25)
    browser.refresh()

# Printing the scores
print ('Game over! Here are your scores:')
print('%s' % ('\n'.join(scores)))
highest = browser.find_element_by_css_selector("div[class='best-container']").text
print('Your highest score is: %s' % (highest))