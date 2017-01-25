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

#matrix = Adafruit_RGBmatrix(32, 2)
font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 8)
message = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 22)
train = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 11)
weather_font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 10)

global panel_state
panel_state = {'schedule': None, 'weather': None}

def main(matrix):
    global draw
    image = Image.new("RGB", (64, 32))
    draw = ImageDraw.Draw(image)
    setup_board()
    train_display()
    weather_display()
    weather_icon = Image.open("sun2")
    weather_icon.load()
    matrix.Clear()
    matrix.SetImage(image.im.id, 0, 0)
    matrix.SetImage(weather_icon.im.id, 44, 13)
            
def setup_board():
    global draw
    draw.text((2, 1), "l TERRACE", font=font, fill="white")
    draw.line((0, 0, 63, 0), fill="#400080")
    draw.line((0, 31, 63, 31), fill="#400080")
    draw.line((63, 1, 63, 30), fill="#400080")
    draw.line((40, 1, 40, 30), fill="#400080")
    draw.line((0, 1, 0, 30), fill="#400080")
    draw.line((1, 9, 39, 9), fill="#400080")

def set_weather(temp, temp_color):
    global panel_state
    panel_state['weather'] = {'temp':str(temp), 'temp_color':temp_color}

def set_mbta(schedule):
    global panel_state
    panel_state['schedule'] = schedule

def train_display():
    global draw
    schedule = panel_state['schedule']
    if schedule:
        train1, color1, train2, color2 = mbtaTimeDisplay.panel_train(schedule)
        draw.text((4, 10), train1, font=train, fill=color1)
        draw.text((4, 19), train2, font=train, fill=color2)
    else:
        draw.text((4, 10), "No", font=train, fill="red")
        draw.text((4, 19), "Trains", font=train, fill="red")

def weather_display():
    global draw
    weather = panel_state['weather']
    if weather:
        draw.text((46, 3), weather['temp'] + u"\u00b0", font=weather_font, fill=weather['temp_color'])
    else:
        draw.text((44, 3), "N\A", font=weather_font, fill="red")

if __name__ == "__main__":
    main()
