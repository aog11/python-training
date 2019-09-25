#Chapter 6
#Bullet Point Adder project

#! python3

import sys, pyperclip
text = pyperclip.paste()

lines = text.split('\n')
print(lines)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
print(text)
pyperclip.copy(text)