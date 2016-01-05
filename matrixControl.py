__author__ = 'Terrace Boiz'

# !/usr/bin/python

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

import time
import traceback

import Image
import ImageDraw
import ImageFont
import mbtaTimeDisplay
import mbtaJsonParse
import Weather
from rgbmatrix import Adafruit_RGBmatrix


matrix = Adafruit_RGBmatrix(32, 2)
font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 8)
message = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 22)
train = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 11)
weather = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 10)
pending_Text = []


def main():
    global draw
    if len(pending_Text) == 0:
        image = Image.new("RGB", (64, 32))  # Can be larger than matrix iff wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        draw.text((2, 1), "1 TERRACE", font=font, fill="white")
        draw.line((0, 0, 63, 0), fill="#000070")
        draw.line((0, 31, 63, 31), fill="#000070")
        draw.line((63, 1, 63, 30), fill="#000070")
        draw.line((40, 1, 40, 30), fill="#000070")
        draw.line((0, 1, 0, 30), fill="#000070")
        draw.line((1, 9, 39, 9), fill="#000070")
        train_display()
        weather_display()
        weather_icon = Image.open("sun2")
        weather_icon.load()
        matrix.Clear()
        matrix.SetImage(image.im.id, 0, 0)
        matrix.SetImage(weather_icon.im.id, 44, 13)
    else:
        image = Image.new("RGB", (len(pending_Text[0]) * 10, 32))  # Can be larger than matrix iff wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        draw.text((0, 0), pending_Text[0], fill="white", font=message)
        for n in range(64, -image.size[0], -1):
            matrix.Clear()
            matrix.SetImage(image.im.id, n, 0)
            time.sleep(0.035)
        pending_Text.pop(0)
        main()


def train_display():
    try:
        global draw
        train1, color1, train2, color2 = mbtaTimeDisplay.panel_train(mbtaJsonParse.schedule)
        draw.line((4, 12, 35, 12), fill="white")

        draw.line((6, 11, 6, 13), fill="red")
        draw.line((10, 11, 10, 13), fill="yellow")
        draw.line((15, 11, 15, 13), fill="green")
        draw.text((4, 14), train1, font=train, fill=color1)
    except TypeError:
        draw.text((4, 10), "No", font=train, fill="red")
        draw.text((4, 19), "Trains", font=train, fill="red")
    except:
        print traceback.print_exc()


def weather_display():
    try:
        global draw
        current_weather, weather_color = Weather.weather_panel()
        draw.text((46, 3), current_weather, font=weather, fill=weather_color)
    except NameError:
        print "Caught Name error"
        print traceback.print_exc()
        draw.text((46, 3), "N\A", font=weather, fill="red")
    except:
        print "Caught unhandled exception in matrixcontrol.weatherDisplay"
        print traceback.print_exc()
        draw.text((46, 3), "N\A", font=weather, fill="red")

        




