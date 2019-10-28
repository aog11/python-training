# Chapter 14
# Removing The Header From CSV Files Project

#! python3

# Importing the needed modules
import os, csv

# Going to the directory with the csv files
filesDir = ''
os.chdir(filesDir)

# Going over the files in the directory
for csvFile in os.listdir():
    # Working only with the csv files
    if csvFile.endswith('.csv'):
        print('Removing header from %s ...' %(csvFile))
        # Read the csv file (skipping first row)
        csvRows = []
        with open(csvFile) as csvFileObj:
            readerObj = csv.reader(csvFileObj)
            for row in readerObj:
                if readerObj.line_num == 1:
                    continue # skip first row
                csvRows.append(row)
        # Write out the CSV file
        with open('headerRemoved_%s'%(csvFile),'w',newline='') as csvFileObj:
            csvWriter = csv.writer(csvFileObj)
            for row in csvRows:
                csvWriter.writerow(row)