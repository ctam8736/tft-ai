from PIL import Image
import PIL.ImageOps
import pytesseract
import pyautogui
import time
import keyboard

from ScreenInterpreter import ScreenInterpreter
from Champion import Champion
from PlayerControl import PlayerControl
from Bot import Bot


def testStoreVision():
    "Reads champions in store from screenshot, adds them to board, then prints synergies."
    print("Reading...")
    info_reader = ScreenInterpreter()
    info_reader.retrieveData(pyautogui.screenshot())
    print("Identified champs from store: " + str(info_reader.getStore()))
    print("Identified gold total: " + str(info_reader.getGold()))


def testManeuvering():
    "Tests moving champions around."
    print("Maneuvering...")
    pc = PlayerControl()
    pc.placeChampOnBoard(0, 18)
    pc.reorderChampOnBoard(18, 10)
    pc.reorderChampOnBoard(10, 11)
    pc.placeChampOnBench(11, 1)
    pc.reorderChampOnBench(1, 6)
    pc.reorderChampOnBench(6, 6)
    pc.placeChampOnBoard(6, 14)
    pc.reorderChampOnBoard(14, 6)


def buyOut():
    "Buys all chmapions in store."
    pc = PlayerControl()
    for i in range(5):
        pc.buyChampion(i)
        time.sleep(0.3)


# main execution
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed("-"):  # if key 'a' is pressed
            testStoreVision()
        elif keyboard.is_pressed("="):
            testManeuvering()
        else:
            pass
    except:
        print("Oh no.")  # if user pressed other than the given key the loop will break
        break
