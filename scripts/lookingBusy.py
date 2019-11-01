# Chapter 18
# Looking Busy Project

#! python3

# Importing the needed modules
import pyautogui

# Moving the mouse slightly every ten seconds
while True:
    pyautogui.PAUSE = 10
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 2, y + 2)