# Chapter 14
# Excel To CSV Converter Project

#! python3

# Importing the needed modules
import os, openpyxl, csv

# Going to the location of the files
filesDir = ''
os.chdir(filesDir)

# Looping over the files in the current directory
for excelFile in os.listdir():
    # Working only with Excel files
    if excelFile.endswith('.xlsx'):
        # Opening the Excel file
        wb = openpyxl.load_workbook(excelFile)
        for sheetName in wb.get_sheet_names():
            sheet = wb[sheetName]
            print('Working with sheet %s of file %s.' %(sheet.title,excelFile))
            # Writing the contents of the sheet to a CSV file
            with open('sheet_%s_of_file_%s.csv' %(sheet.title,os.path.splitext(excelFile)[0]),'w',newline='') as csvFile:
                csvWriter = csv.writer(csvFile)
                # Looping all the rows in the sheet
                for row in range(1,sheet.max_row+1):
                    rowData = [] # List with all the values of the current row
                    for col in range(1,sheet.max_column+1):
                        # Appending the values of the current row to the list
                        rowData.append(sheet.cell(row=row,column=col).value)
                    # Writing the values of the looped row to the file
                    csvWriter.writerow(rowData)