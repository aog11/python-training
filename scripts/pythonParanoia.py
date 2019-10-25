# Chapter 13
# PDF Paranoia Project

#! python3

# Importing the needed modules
import os, PyPDF2
from getpass import getpass
from send2trash import send2trash

# Asking for the passwords
encryptPwd = getpass('Please enter the password to encrypt the files: ')

# Directory where the PDFs are located
pdfDir = ''
os.chdir(pdfDir)

# Walking the directory
for folder, subfolder, filename in os.walk('.'):
    # Working with the PDF files
    for file in filename:
        if file.endswith('.pdf'):
            newPdfName = '%s_encrypted.pdf' % (os.path.splitext(file)[0])
            fileToEncrypt = open(file,'rb')
            pdfReader = PyPDF2.PdfFileReader(fileToEncrypt)
            pdfWriter = PyPDF2.PdfFileWriter()
            # Working with the files that are not encrypted
            if not pdfReader.isEncrypted:
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(encryptPwd)
                # Saving the encrypted file and closing the one opened
                with open(newPdfName,'wb') as encryptedPDF:
                    pdfWriter.write(encryptedPDF)
            fileToEncrypt.close()

# Deleting the unencrypted files
for folder, subfolder, filename in os.walk('.'):
    for file in filename:
        if file.endswith('.pdf'):
            # Testing that the file has been encrypted
            encryptedFile = open(file,'rb')
            pdfReader = PyPDF2.PdfFileReader(encryptedFile)
            if pdfReader.isEncrypted:
                if pdfReader.decrypt(encryptPwd):
                    encryptedFile.close()
                    print('File %s has been encrypted correctly.' % (file))
                    fileToRemove = file.replace('_encrypted','')
                    send2trash(fileToRemove)
                else:
                    encryptedFile.close()
                    print('Provided password does not work for file %s ' % (file))
            else:
                encryptedFile.close()
                print('File %s is not encrypted.' % (file))
print('Done.')