__author__ = 'Terrace Boiz'

#!/usr/bin/python

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import Image
import ImageDraw
import ImageColor
import time
import ImageFont
import mbtaTimeDisplay, mbtaJsonParse, Weather
from collections import defaultdict
from rgbmatrix import Adafruit_RGBmatrix


matrix = Adafruit_RGBmatrix(32, 2)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf",12)
train = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf",10)
weather = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf",10)


def main():
    global draw
    image = Image.new("RGB", (64, 32)) # Can be larger than matrix iff wanted!!
    draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
    draw.text((4,-2), "Trains", fill="blue", font=font)
    draw.line((4,10,34,10), fill="white")
    trainDisplay()
    weatherDisplay()
    image2 = Image.open("rain")
    image2.load()
    matrix.Clear()
    matrix.SetImage(image.im.id,0,0)
    matrix.SetImage(image2.im.id,42,13)


def trainDisplay():
    try:
        global draw
        train1, color1, train2, color2 = mbtaTimeDisplay.panelTrain(mbtaJsonParse.schedule)
        draw.text((5, 10), train1, font=train, fill=color1)
        draw.text((5,20), train2, font=train, fill=color2)
    except:
        draw.text((5, 10), "No Trains", font=train, fill=1)
        draw.text((5,20), "Faggot", font=train, fill="red")

def weatherDisplay():
    try:
        global draw
        currentWeather, weathercolor = Weather.weatherPanel()
        draw.text((44, 3), currentWeather, font=weather, fill=weathercolor)
    except:
        draw.text((44, 3), "NO", font=weather, fill="red")




