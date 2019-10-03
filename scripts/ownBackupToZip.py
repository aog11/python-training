# Chapter 9
# Backing Up Folder to Zip File project
# This is my own version before proceeding with the one in the book,
# hence why it's so simple :D

#! python3
import os, zipfile

def backupToZip(path, zip, folder):
    # Changing to the directory with the folder
    os.chdir(path)

    # Opening the zip to store the data in
    backupZip = zipfile.ZipFile(zip,'a')

    # Adding the folder to the zip
    backupZip.write(folder)

    # Listing the contents in the zip
    print(backupZip.namelist())

    # Closing the zip file
    backupZip.close()

backupToZip ('C:\\files','newzip.zip','dates')