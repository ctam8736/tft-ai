from PIL import Image
import PIL.ImageOps
import pytesseract

from ScreenInterpreter import ScreenInterpreter
from Champion import Champion
from Board import Board

board = Board()
interpreter = ScreenInterpreter()
img = Image.open("Screen05.png")
interpreter.retrieveData(img)
print(interpreter.getStore())
for champ_name in interpreter.getStore():
    board.addChampion(Champion(champ_name, 1))
board.printActive()
