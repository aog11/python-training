# Chapter 17
# Adding A Logo Project

#! python3

# Importing the needed modules
import os
from PIL import Image, ImageSequence

# Going to the directory with the images
imgDir = ''
os.chdir(imgDir)

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME).convert('RGBA')
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo',exist_ok=True)

# Loop over all files in the working directory
for filename in os.listdir('.'):
    if os.path.splitext(filename.lower())[1] not in ('.png','.jpg','.bmp','.gif') \
        or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo itself
    
    im = Image.open(filename).convert('RGBA')
    width, height = im.size

    # Check if images needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # Resize the image
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
    
    # Skipping the image if its the same size as the logo
    if (width == logoWidth) and (height == logoHeight):
        continue

    # Add the logo
    print('Adding logo to %s...' %(filename))
    # Working with regular GIF files
    if filename.lower().endswith('.gif'):
        frames = []
        gifIm = Image.open(filename)
        for frame in ImageSequence.Iterator(gifIm):
            frame = frame.copy()
            frame.paste(logoIm, mask=logoIm)
            frames.append(frame)
        frames[0].save(os.path.join('withLogo',filename), save_all=True, append_images=frames[1:])
    # Working with regular image files
    else:
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
        # Save changes
        im.save(os.path.join('withLogo',filename),'PNG') # Adding transparency with PNG