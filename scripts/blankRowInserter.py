# Chapter 12
# Blank Row Inserter Project

#! python3

# Importing the needed modules
import os, sys, openpyxl

# Receiving the input
if len(sys.argv) < 4:
    print('Please send all the needed parameters: \n 1. Starting row \n 2. Amount of blank rows \n 3. Excel file to open')
    sys.exit()
startRow, addBlanks, filename = sys.argv[1:4]

# Turning the string numbers into integers
startRow = int(startRow)
addBlanks = int(addBlanks)

# Opening the file
filePath = 'C:\\Users\\antoni ozoria\\Desktop\\DBA ANTONI\\Git Repos\\python-training\\files\\'
os.chdir(filePath)
wb1 = openpyxl.load_workbook(filename)
sheet1 = wb1.active

# Creating the new file with the blank lines
wb2 = openpyxl.Workbook()
sheet2 = wb2.active

# Adding the lines before the blank ones
for row in range(1,startRow):
    for column in range(1,sheet1.max_column + 1):
        sheet2.cell(row=row,column=column).value = sheet1.cell(row=row,column=column).value
# Adding the blank lines
for row in range(1,sheet2.max_row+1):
    for column in range(1,sheet2.max_column+1):
        sheet2.cell(row=row+addBlanks,column=column).value = ''
# Adding the remaining of the file after the blank lines
for row in range(1,sheet1.max_row+1):
    for column in range(1,sheet1.max_column + 1):
        sheet2.cell(row=row+startRow+addBlanks-1,column=column).value = sheet1.cell(row=row+startRow-1,column=column).value

# Saving the file as a copy
wb2.save('copyOf%s'%(filename))