# Chapter 8
# Regex Search project

import os, re

# Looking for the txt files in the specified directory
textFileRegex = re.compile(r'[a-zA-Z0-9^\\\/:\*\"<>\|]+\.txt')
baseDir = 'C:\\files'
allFiles = os.listdir(baseDir)
matchedFiles = textFileRegex.findall(' '.join(allFiles))

# Creating a Regex to evaluate the content in the files and searching it in them
textFileRegex = re.compile(r'bacon|eggs|fruit')
for file in matchedFiles:
    textFile = open(os.path.join(baseDir,file))
    text = textFile.readlines()
    match = textFileRegex.findall(' '.join(text))
    if match != []:
        print('\nFile %s has a matched word' % (file))
        print('\n'.join(text))
    textFile.close()