# Chapter 16
# Random Choice Assigment Emailer Project

#! python3

# Importing the needed modules
import random, sys, smtplib
from getpass import getpass

# Creating the chores
chores = ['cooking','dusting','doing the dishes','walking the dog']

# List with emails
emails = [] # Add emails here

# We need the same amount of chores as people
if len(chores) < len(emails):
    print('The amount of chores has to be equal to the people receiving them.')
    sys.exit()
elif len(emails) < len(chores):
    print('The amount of people has to be equal to the amount of chores.')
    sys.exit()

# SMTP Configuration
senderMail = 'pytest1066@gmail.com'
emailPasswd = getpass('Please enter the password for the configured sender (%s): ' %(senderMail))
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(senderMail,emailPasswd)

# Assigning the chores
for chore in chores:
    for email in emails:
        randomChore = random.choice(chores)
        chores.remove(randomChore)
        # Sending the email
        body = 'Subject: Assigned chore\n\nHello, your assigned chore is: %s.' % (randomChore)
        smtpObj.sendmail(senderMail,email,body)

# Logging out of the email
smtpObj.quit()
print('Done.')