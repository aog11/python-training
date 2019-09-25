#Chapter 6
#Password Locker project

#! python3
import sys, pyperclip

PASSWORDS = {'email': '32D0A676AEB6362D5325ABECBCFBA2AC',
             'blog': 'B7BE05179372C0F8AD89B856728FD0D7',
             'luggage': 7896543254789}

if len(sys.argv) < 2:
    print ('The Password Manager needs an account to retrieve its password!')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('The password of your ' + account + ' is ' + str(PASSWORDS[account]))
else:
    print('There is no account named ' + account)