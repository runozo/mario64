"""Converts a png to multicolor sprite."""
from PIL import Image
from termcolor import colored  # https://pypi.org/project/termcolor/

print(colored('hello', 'red'))

# Can be many different formats.
im = Image.open('../assets/animation_frames/mario_run_right.png')
pix = im.load()
image_colors = {}
color_amount = 0
# https://www.c64-wiki.com/wiki/Sprite#Multicolor_sprite_pattern
# Pixels with a bit pair of "00" appear transparent, like "0" bits do in high resolution mode.
# Pixels with a bit pair of "01" will have the color specified in address 53285/$D025.
# Pixels with a bit pair of "11" will have the color specified in address 53286/$D026.
c64_color_values = [('00', 'white'), ('01', 'blue'),
                    ('11', 'red'), ('10', 'yellow')]
# Get the width and hight of the image for iterating over

print("Image size is %sx%s" % im.size)
print("Counting unique colours...")

for y in range(im.size[1]):
    for x in range(im.size[0]):
        if not pix[x, y] in image_colors:
            image_colors[pix[x, y]] = color_amount
            color_amount += 1

print("Image has %s unique colours, converting..\n\n" % len(image_colors))

out = ''
if color_amount <= 4:
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            out += colored(c64_color_values[image_colors[pix[x, y]]]
                           [0], c64_color_values[image_colors[pix[x, y]]][1])
        out += '\n'
    print(out)
else:
    print("Too many colors for a c64 sprite, exiting.")
print('Done.')
