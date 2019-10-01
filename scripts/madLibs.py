# Chapter 8
# Mad Libs project

import os, re

# Opening and reading the file
baseText = open('C:\\files\\baseMadLib.txt')
fileText = baseText.read()

# Looking for the ocurrences to replace in the text
ocurrenceRegex = re.compile(r'ADJECTIVE')
if ocurrenceRegex.search(fileText).group() != '':
    print ('Enter an adjective: ', end='')
    adjective = input()
    fileText = re.sub(r'ADJECTIVE',adjective,fileText)

ocurrenceRegex = re.compile(r'NOUN')
if ocurrenceRegex.search(fileText).group() != '':
    print ('Enter a noun: ', end='')
    noun1 = input()
    fileText = re.sub(r'the NOUN',noun1,fileText)

ocurrenceRegex = re.compile(r'VERB')
if ocurrenceRegex.search(fileText).group() != '':
    print ('Enter an verb: ', end='')
    verb = input()
    fileText = re.sub(r'VERB',verb,fileText)

ocurrenceRegex = re.compile(r'nearby NOUN')
if ocurrenceRegex.search(fileText).group() != '':
    print ('Enter a noun: ', end='')
    noun2 = input()
    fileText = re.sub(r'nearby NOUN',noun2,fileText)

# Printing the resulting string and saving it in a new file
print (fileText)
newFile = open ('C:\\files\\resultMadLib.txt','w')
newFile.write(fileText)
newFile.close()