# Chapter 13
# Combining Select Pages From Many PDFs Project

#! python3

import os, PyPDF2

# Get all the PDF filenames.
currPath = ''
pdfFiles = []
for filename in os.listdir(currPath):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(os.path.join(currPath,filename),'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages (except the first) and add them.
    if not pdfReader.isEncrypted: # Skip the encrypted files.
        for pageNum in range(1,pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

# save the resulting PDF to a file.
pdfOutput = open(os.path.join(currPath,'allminutes.pdf'),'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()