# Creating the files with european and american style dates
# needed for chapter 9

import os, datetime

os.chdir('C:\\files\\dates')

#American style date
dateFormat = datetime.date.__format__(datetime.date.today(),'%m-%d-%Y')

for i in range(4):
    createdFile = open ('file %s %s.txt' %(i + 1,dateFormat), 'w')
    createdFile.write('This file has an american style date in the name.')
    createdFile.close()

#European style date
dateFormat = datetime.date.__format__(datetime.date.today(),'%d-%m-%Y')

for i in range(4):
    createdFile = open ('file %s %s.txt' %(i + 1,dateFormat), 'w')
    createdFile.write('This file has an european style date in the name.')
    createdFile.close()