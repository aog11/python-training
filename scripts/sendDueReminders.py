# Chapter 16
# Sending Member Dues Reminder Emails Project

#! python3

# Importing the needed modules
import os, openpyxl, smtplib
from getpass import getpass

# Asking for the password of the email
senderEmail = 'pytest1066@gmail.com'
passwd = getpass('Please enter the password of the configured email (%s):' %(senderEmail))

# Going to the directory with the excel file
excelDir = ''
os.chdir(excelDir)

# Open the spreadsheet and get the latest dues status
wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb['Sheet1']

lastCol = sheet.max_column
latestMonth = sheet.cell(row=1,column=lastCol).value

# Check each member's payment status
unpaidMembers = {}
for r in range(2,sheet.max_row + 1):
    payment = sheet.cell(row=r,column=lastCol).value
    if payment != 'paid':
        name = sheet.cell(row=r,column=1).value
        email = sheet.cell(row=r,column=2).value
        unpaidMembers[name] = email

# Log in to email account
smtpObj = smtplib.SMTP('imap.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(senderEmail,passwd)

# Send out reminder emails
for name, email in unpaidMembers.items():
    body = ("Subject: %s dues unpaid. \nDear %s, \nRecords show that you have not paid dues for %s."
            "Please make this payment as soon as possible. Thank you!'" % (latestMonth, name, latestMonth))
    print('Sending email to %s...' % email)
    sendmailStatus = smtpObj.sendmail(senderEmail,email, body)

    if sendmailStatus != {}:
        print('There was a problem sending email to %s: %s' % (email, sendmailStatus))
smtpObj.quit()