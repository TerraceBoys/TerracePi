__author__ = 'branden'

import Image
import ImageDraw
import ImageColor
import time
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix


class teamInfo:
    def __init__(self, name, score):
        self.name = name    #String: Team name
        self.score = score  #Int: Team score

score_board = []
matrix = Adafruit_RGBmatrix(32, 2)
introFont = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf",20)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf",12)


def main():
    global game_update
    game_update = True
    gameIntro()
    gameDisplay()
    while True:
        if game_update:
            gameDisplay()
            game_update = False


def gameIntro():
    image = Image.new("RGB", (64, 32)) # Can be larger than matrix iff wanted!!
    draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
    draw.text((4,2), "Baseball", fill="blue", font=introFont)
    matrix.Clear()
    matrix.SetImage(image.im.id,0,0)


def gameDisplay():
    image = Image.new("RGB", (64, 32)) # Can be larger than matrix iff wanted!!
    draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
    draw.text((4,-2), score_board[0].name, fill="blue", font=font)
    draw.text((30,-2), score_board[1].name, fill="blue", font=font)
    matrix.Clear()
    matrix.SetImage(image.im.id,0,0)


def init_game(info):
    teams = info.split(":")
    team1 = teamInfo(teams[0], 0)
    team2 = teamInfo(teams[1], 0)
    score_board.append(team1)
    score_board.append(team2)


def updateScore(info):
    global game_update
    for t in score_board:
        if t.name == info[0]:
            t.score += info[1]
            break
    game_update = True



if __name__ == "__main__":
    main()