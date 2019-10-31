# Chapter 17
# Identifying Photo Folders on the Hard Drive Project

#! python3

# Importing the needed modules
import os
from PIL import Image

# Walking the directory looking for image files
for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    
    # Cheking the files
    for filename in filenames:
        if os.path.splitext(filename.lower())[1]  not in ('.png','.jpg','.bmp','.gif'):
            numNonPhotoFiles += 1
            continue
        
        # Opening the image
        im = Image.open(filename)
        # Check if width and height are larger than 500
        width, height = im.size
        if width > 500 and height > 500:
            # Image is counted as a photo
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo
            numNonPhotoFiles += 1
    
    # This is a photo folder
    if numPhotoFiles > numNonPhotoFiles:
        print(foldername)