# Chapter 8
# Multiclipboard project
# This is a version I decided to make before proceeding with the one in the chapter
# In the end I left like this, liked my version better :)

#! python3

# Importing the modules I need
import sys, shelve, pyperclip, os, pprint, re

# Validating that I have the needed parameters
if len(sys.argv) < 2:
    print('You need to pass a command and a key.')
    sys.exit()
elif len(sys.argv) > 3:
    print('You only need to pass two arguments (a command and a key).')
    sys.exit()

# Assigning the values to the variables
text = pyperclip.paste()
action = sys.argv[1].strip().lower()
variable = sys.argv[2]
result = ''

secondArgRegex = re.compile(r'[^a-zA-Z]')
if action == 'save' and secondArgRegex.findall(variable) != []:
    print('The name of the variable cannot contain numbers or special characters.')
    sys.exit()

# Changing to the directory to place the files
os.chdir('C:\\files')

# Opening the shelve file
shelveFile = shelve.open('multiclip')

# Doing something based on the action sent in by the user
try:
    # Saves the content of the clipboard to the specified variable
    if action == 'save':
        shelveFile[variable] = text
    # Pastes the content specified variable or all of them to the clipboard
    elif action == 'get':
        if variable == '*':
            for k in shelveFile.keys():
                result += shelveFile[k] + '\n'
            pyperclip.copy(result)
        else:
            pyperclip.copy(shelveFile[variable])
    # Deletes the specified variable or all of them
    elif action == 'delete':
        if variable == '*':
            for k in shelveFile.keys():
                del shelveFile[k]
        else:
            del shelveFile[variable]
    # Prints the specified variable or all of them
    elif action == 'list':
        if variable == '*':
            pprint.pprint(dict(shelveFile.items()))
        else:
            pprint.pprint(shelveFile[variable])
except KeyError:
    # Closing the shelve file and exiting the program in case of the expected exception
    print('The specified variable does not exist.')
    shelveFile.close()
    sys.exit()

# Closing the shelve file
shelveFile.close()