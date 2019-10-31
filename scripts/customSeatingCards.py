# Chapter 17
# Custom Seating Cards Project

#! python3

# Importing the needed modules
import os
from PIL import Image, ImageDraw, ImageFont

# Going to the directory with the images
imagesDir = ''
os.chdir(imagesDir)

# Font information
fontsFolder = 'C:\\Windows\\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)

# Opening the guests file
guestsFileDir = ''
with open(os.path.join(guestsFileDir,'guests.txt')) as guestsFile:
    guests = guestsFile.readlines()

    # Setting the dimensions
    width = 288
    height = 360

    for i in range(len(guests)):
        # Creating the image file
        im = Image.new('RGBA',(width,height),'white')

        # Opening the flower file
        flowerIm = Image.open('flower.png')

        # Pasting the flower
        im.paste(flowerIm, None, flowerIm)

        draw = ImageDraw.Draw(im) 
        # Drawing the rectangle
        draw.rectangle((0,0,width - 1,height - 1), outline='black')
        # Writing the name of the guest in the image
        draw.text((50,115),guests[i].replace('\n',''),fill='black',font=arialFont)

        # Saving the resulting invitation
        im.save('%s.png' %(guests[i].replace('\n','')))