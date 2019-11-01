# Chapter 18
# Form Filler Project

#! python3

# Importing the needed modules
import pyautogui, time

# Positions
nameField = (549, 358)
submitButton = (586, 946)
submitButtonColor = (26, 115, 232)
submitAnotherLink = (615, 404)

# Data for the form
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]

pyautogui.PAUSE = 0.5

# Function to wait for the form to respond to the keys
def waitForForm():
        pyautogui.PAUSE = 0.50
        pyautogui.typewrite(['enter'])
        pyautogui.PAUSE = 0.50
        pyautogui.typewrite(['\t'])


for person in formData:
    # Give the user a chance to kill the script
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Scrolling so the submit button shows up
    pyautogui.scroll(-200)

    # Wait until form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)

    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    # Fill out Name field
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out Greatest Fear(s) field
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out Source of Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.typewrite(['down'])
        waitForForm()
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down'])
        waitForForm()
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down'])
        waitForForm()
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down'])
        waitForForm()

    # Fill out Robocop field
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out Additional comments
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the "Submit another response" link
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])