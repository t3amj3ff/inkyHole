#!/usr/bin/env python

# PiHole stats to InkyPHAT script thingy
#
# Created by TJ - 2018-12-14
#
# Run on PiHole Pi
# Setup cron job to run chronometer.sh -j to export data to JSON file
# and then run this script to display it on the InkyPHAT
#

# Import bits
import json, time
from collections import OrderedDict
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw


# Read PiHole JSON file
# Added OrderedDict to read json file in order
pihole_data = json.loads(open('/opt/inkyhole/pihole.json').read(), object_pairs_hook=OrderedDict)


# Setup the InkyPHAT display
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.RED)


# Set the logo as the background
img = Image.open("/opt/inkyhole/piholelogobig.png")
draw = ImageDraw.Draw(img)


# Print the date in the top right
date = time.strftime("%Y-%m-%d")

x = inky_display.WIDTH - 61
y = 0

draw.text((x, y), date, inky_display.WHITE)


# Pick a font
from font_hanken_grotesk import HankenGroteskMedium

font = ImageFont.truetype(HankenGroteskMedium, 22)


# Labels for the data items
message = [
        "DHCP: ",
        "DNS: ",
        "Ads: ",
        "%: ",
]


# Read through the json data and draw it on the screen

y = 5
i = 0

for key in pihole_data:
        x = 5
        value = pihole_data[key]
        #print("Key: {} , Data: {}".format(key, value))
        w, h = font.getsize(message[i])
        draw.text((x, y), message[i], inky_display.WHITE, font)
        x = x + w + 2
        draw.text((x, y), str(value), inky_display.WHITE, font)
        y = y + 22 + 1
        i += 1


inky_display.set_image(img)
inky_display.show()
