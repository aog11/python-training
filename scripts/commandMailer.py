# Chapter 11
# Command Line Emailer project

# Importing the needed modules
import pyperclip, time
from selenium import webdriver

# Getting the email and password from the clipboard
email, passwd = pyperclip.paste().split()
to_mail = 'antonifco@gmail.com'
mail_subject = 'Python Mail'
mail_text='This is a text sent from my python script. \n :)'

# Accessing the email
browser = webdriver.Chrome()
browser.get('http://mail.google.com')

# Finding the input boxes email and password and sending them input
email_input = browser.find_element_by_name('identifier')

# email
email_input.send_keys(email)

# Clicking the next button
nextButton = browser.find_element_by_class_name('CwaK9')
nextButton.click()

# Waiting for the new page to load
time.sleep(1)

# password
passwd_input = browser.find_element_by_name('password')
passwd_input.send_keys(passwd)

# Clicking the next button
nextButton = browser.find_element_by_class_name('CwaK9')
nextButton.click()

# Writting an email

time.sleep(5) # Waiting for the page to completely load

# Clicking redact
redact = browser.find_element_by_css_selector("div[class='T-I J-J5-Ji T-I-KE L3']")
redact.click()
time.sleep(0.75)
# Recepient
to = browser.find_element_by_name('to')
to.send_keys(to_mail)

# Subject
subject = browser.find_element_by_name('subjectbox')
subject.send_keys(mail_subject)

# Mail text
text = browser.find_element_by_id(':rm')
text.send_keys(mail_text)

# Send the mail
send = browser.find_element_by_css_selector("div[class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
send.click()
time.sleep(0.75)

# Exiting the browser
browser.quit()