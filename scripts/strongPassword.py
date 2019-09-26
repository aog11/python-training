#Chapter 7
#Strong Password Detection project

import re

def passwordValidation(pwd):
    if len (pwd) < 8:
        print ('Your password needs to be at least eight characters long.')
        return
    else:
        numberRegex = re.compile(r'[0-9]+')
        match = numberRegex.findall(pwd)
        if not match:
            print('Your password needs at least one digit.')
            return

        upperRegex = re.compile(r'[A-Z]+')
        match = upperRegex.findall(pwd)
        if not match:
            print('Your password needs at least one uppercase character.')
            return

        symbolRegex = re.compile(r'[\*\#\-_]+')
        match = symbolRegex.findall(pwd)
        if not match:
            print('Your password needs at least one special character.')
            return
        
        print('Your password is secure.')

#Wanted to make my tests quicker, ended up setting the password
#to a variable.
password = 'Truenooo*1'
if password == '':
    print ('Please enter a password to validate its strength: ',end='')
    password = input()

passwordValidation(password)