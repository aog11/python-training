# Chapter 9
# Selective Copy project

import os, shutil

def selectiveCopy(origin,destination):
    # Walking through the specified folder
    for folder, subfolder, filename in os.walk(origin):
        for file in filename:
            # Files to move to the specified destination
            if file.endswith('.txt') or file.endswith('.zip'):
                #print('Copying %s to %s' % (os.path.join(folder,file), destination)) #Verifying that the correct files will be copied
                shutil.copy(os.path.join(folder,file),destination)
    print('Done.')

selectiveCopy('C:\\files','C:\\destination')