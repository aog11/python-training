# Chapter 15
# Simple Countdown Program Project

#! python3

# Importing the needed modules
import time, os, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft-= 1

# Going to the location of alarm.wav
os.chdir('')

# At the end of the countdown, play a sound file
subprocess.Popen(['start','alarm.wav'],shell=True)