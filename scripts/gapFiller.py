# Chapter 9
# Filling In The Gaps project

import os, shutil

def gapFiller(path):
    number = 0
    # Creating the files missing the gaps
    for i in range(10):
        if (i + 1)%2 == 0:
            newFile = open(folder + '\\spam00%s.txt' %(i + 1),'w')
            newFile.write('This is the file #%s.' %(i + 1))
            newFile.close()
    # Looking for the gaps in the files
    # By renaming the files
    for i in range(10):
        if not os.path.exists(folder + '\\spam00%s.txt' %(i + 1)):
            for j in range(10):
                number += 1
                if os.path.exists(folder + '\\spam00%s.txt' %(number)):
                    shutil.move(folder + '\\spam00%s.txt' %(number), folder + '\\spam00%s.txt' %(i + 1))
                    break

    # Looking for the gaps in the files
    # By adding the missing files
    for i in range(10):
        if not os.path.exists(folder + '\\spam00%s.txt' %(i + 1)):
            newFile = open(folder + '\\spam00%s.txt' %(i + 1),'w')
            newFile.write('This is the file #%s, which was missing.' %(i + 1))
            newFile.close()

# Folder containing the files
folder = 'C:\\files\\gaps'
gapFiller(folder)