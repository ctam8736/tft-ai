from ScreenInterpreter import ScreenInterpreter
from PlayerControl import PlayerControl
from Board import Board
import pyautogui


class Bot:
    def __init__(self):
        self.info_reader = ScreenInterpreter()
        self.controller = PlayerControl()
        self.board = board()

    def runBot(self):
        """
        Starts the main AI loop.
        """
        print("Running...")
        self.info_reader.retrieveData(pyautogui.screenshot())
        print("Identified champs from store: " + str(self.info_reader.getStore()))
        print("Identified gold total: " + str(self.info_reader.getGold()))

    def buyRelevant(self):

