# Chapter 13
# Brute-Force PDF Password Breaker Project

# Importing the needed modules
import os, PyPDF2, sys

# Location of the files and the dictionary
filesDir = ''
os.chdir(filesDir)

# Looking for all the PDF files in the location
pdfFiles = []
for folder, subfolder, filename in os.walk('.'):
    for file in filename:
        if file.endswith('.pdf'):
            pdfFiles.append(file)

# Sorting the pdf files
pdfFiles.sort(key=str.lower)

# Printing the pdf files found to select one to decrypt
print('These are the PDFs found, which one would you like to decrypt?')
for pdf in pdfFiles:
    numberedFile = '%s- %s' %(str(pdfFiles.index(pdf) + 1), pdf)
    print(numberedFile)
selectedFile = ''
# Making sure that the number introduced corresponds to the actual amount of files
while True:
    # Making sure that the input is an integer value
    try:
        print('Response: ',end='')
        selectedFile = int(input())
        if selectedFile > len(pdfFiles):
            print('The selected file does not exist.')
            continue
        else:
            break
    except ValueError:
        print('Please enter a valid number.')
        continue

# Decrypting the file
with open(pdfFiles[selectedFile - 1],'rb') as selectedPDF:
    pdfReader = PyPDF2.PdfFileReader(selectedPDF)
    # Only working with the files that are encrypted
    if not pdfReader.isEncrypted:
        print('The selected file is not encrypted.')
    # Opening the dictionary with the passwords
    else:
        with open('dictionary.txt','r') as dictionary:
            # Going through each password in the dictionary (uppercase and lowercase) and printing the correct one
            for passwd in dictionary.readlines():
                upperPWD = passwd.replace('\n','')
                lowerPWD = passwd.replace('\n','').lower()
                if pdfReader.decrypt(upperPWD):
                    print('The password of file %s is %s.' %(pdfFiles[selectedFile], upperPWD))
                    break
                elif pdfReader.decrypt(lowerPWD):
                    print('The password of file %s is %s.' %(pdfFiles[selectedFile], lowerPWD))
                    break