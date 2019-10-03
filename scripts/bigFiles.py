# Chapter 9
# This is my version of the "Deleting Uneeded Files" project but
# I didn't have any files I wanted to delete so I instead decided
# to print files that exceeded a certain size.

import os

def bigFiles(path):
    for folder, subfolder, filename in os.walk(path):
        for file in filename:
            if os.path.getsize(os.path.join(folder,file)) > 2000000:
                print ('File %s is greater than 2mb.' % (os.path.join(folder,file)))

# Path to walk through
path = ''
bigFiles(path)