#!.env/bin/python

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

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageSequence

text_font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 8)
NUM_FONT = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 11)

def main(matrix, data):
    print data
    global draw
    image = Image.new("RGB", (64, 32))  # Can be larger than matrix iff wanted!!
    draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
    drawRedScore(str(data['score1']))
    drawBlueScore(str(data['score2']))
    drawBatting(data['batting'])
    drawDiamond()
    drawBases(data['base1'], data['base2'], data['base3'])
    drawInning(str(data['inning']), data['batting'])
    drawStrikes(data['strikes'])
    drawOuts(data['outs'])
    matrix.Clear()
    matrix.SetImage(image.im.id, 0, 0)

def drawIntro(matrix):
    baseballIntro = Image.open("images/baseball.gif")
    for frame in ImageSequence.Iterator(baseballIntro):
        frame = frame.copy()
        corrected_frame = Image.new("RGB", frame.size, (255, 255, 255))
        corrected_frame.paste(frame)
        matrix.SetImage(corrected_frame.im.id, 0, 0)
        time.sleep(.25)
        matrix.Clear()

def drawRedScore(score1):
    global draw
    BORDER = "red"
    SCORE_COLOR = "yellow"
    draw.line([0, 0, 17, 0], fill=BORDER)
    draw.line([17, 1, 17, 15], fill=BORDER)
    draw.line([16, 15, 0, 15], fill=BORDER)
    draw.line([0, 14, 0, 1], fill=BORDER)
    draw.text([3, 2], score1 if len(score1) > 1 else "0{0}".format(score1), font=NUM_FONT, fill=SCORE_COLOR)

def drawBlueScore(score2):
    global draw
    BORDER = "blue"
    SCORE_COLOR = "yellow"
    draw.line([0, 16, 17, 16], fill=BORDER)
    draw.line([17, 17, 17, 31], fill=BORDER)
    draw.line([16, 31, 0, 31], fill=BORDER)
    draw.line([0, 30, 0, 17], fill=BORDER)
    draw.text([3, 18], score2 if len(score2) > 1 else "0{0}".format(score2), font=NUM_FONT, fill=SCORE_COLOR)

def drawBatting(batting):
    global draw
    team1 = [18, 0, 18, 15]
    team2 = [18, 16, 18, 31]
    if not batting:
        draw.line(team1, fill="yellow")
    else:
        draw.line(team2, fill="yellow")

def drawDiamond():
    global draw
    BASE_PATH = "green"
    draw.line([37, 27, 47, 17], fill=BASE_PATH) # home - 1st
    draw.line([47, 14, 37, 4], fill=BASE_PATH) # 1st - 2nd
    draw.line([34, 4, 24, 14], fill=BASE_PATH) # 2nd - 3rd
    draw.line([24, 17, 34, 27], fill=BASE_PATH) # 3rd - home

def drawBases(base1, base2, base3):
    global draw
    NO_RUNNER = "grey"
    RUNNER = "yellow"
    draw.rectangle([35, 28, 36, 29], fill=NO_RUNNER) # home
    draw.rectangle([48, 15, 49, 16], fill=RUNNER if base1 else NO_RUNNER) # 1st
    draw.rectangle([35, 2, 36, 3], fill=RUNNER if base2 else NO_RUNNER) # 2nd
    draw.rectangle([22, 15, 23, 16], fill=RUNNER if base3 else NO_RUNNER) # 3rd    

def drawInning(inning, batting):
    global draw
    INNING_COLOR = "white"
    draw.line([31, 10, 31, 16], fill=INNING_COLOR)
    draw.text([36, 7], inning, font=NUM_FONT, fill=INNING_COLOR)
    if not batting:
        draw.line([30, 11, 32, 11], fill=INNING_COLOR)
        draw.line([29, 12, 33, 12], fill=INNING_COLOR)
    else:
        draw.line([29, 14, 33, 14], fill="white")
        draw.line([30, 15, 32, 15], fill="white")
   
def drawStrikes(strikes):
    global draw
    FILLED = "red"
    NOT_FILLED = "white"
    draw.rectangle([34, 18, 37, 19], fill=FILLED if strikes > 0 else NOT_FILLED) # top
    draw.rectangle([34, 21, 37, 22], fill=FILLED if strikes > 1 else NOT_FILLED) # middle
    draw.rectangle([34, 24, 37, 25], fill=NOT_FILLED) # bottom

def drawOuts(outs):
    global draw
    BORDER = "blue"
    NOT_OUT = "black"
    OUT = "red"
    
    draw.rectangle([54, 2, 61, 9], fill=OUT if outs > 0 else NOT_OUT, outline=BORDER) # top
    draw.rectangle([54, 12, 61, 19], fill=OUT if outs > 1 else NOT_OUT, outline=BORDER) # middle
    draw.rectangle([54, 22, 61, 29], fill=NOT_OUT, outline=BORDER)


if __name__ == "__main__":
    main(None, None)
