"""Converts a png to multicolor sprite."""
from PIL import Image

im = Image.open('../assets/animation_frames/mario_run_right.png') # Can be many different formats.
pix = im.load()
color_count = {}
print ("Image size is %sx%s" % im.size)  # Get the width and hight of the image for iterating over
for y in range(im.size[1]):
    for x in range(im.size[0]):
        color_count[pix[x,y]] = True

print("Image has %s different colours" % len(color_count))

# https://www.c64-wiki.com/wiki/Sprite#Multicolor_sprite_pattern
# Pixels with a bit pair of "00" appear transparent, like "0" bits do in high resolution mode.
# Pixels with a bit pair of "01" will have the color specified in address 53285/$D025.
# Pixels with a bit pair of "11" will have the color specified in address 53286/$D026.

out = ''
if len(color_count)<=4:
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            if pix[x,y] == (0, 0, 0, 255):
                # transparent 
                out.append('00 ')
            


