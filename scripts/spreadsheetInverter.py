# Chapter 12
# Spreadsheet Cell Inverter Project

#! python3

# Importing the needed modules
import os, openpyxl

# Opening the file
filePath = ''
wb1 = openpyxl.load_workbook(filePath)
sheet1 = wb1.active

# Creating a copy the opened file
wb2 = openpyxl.Workbook()
sheet2 = wb2.active

# Inverting the values and putting them in the copy file
for row in range(1,sheet1.max_row+1):
    for column in range(1,sheet1.max_column+1):
        sheet2.cell(row=column,column=row).value = sheet1.cell(row=row,column=column).value

# Saving the copy file
wb2.save('inverted%s' %(os.path.basename(filePath)))