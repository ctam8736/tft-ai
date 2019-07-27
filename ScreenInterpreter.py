from PIL import Image
import PIL.ImageOps
import pytesseract


class ScreenInterpreter:

    # constructor
    def __init__(self):
        # track relevant data on the frame
        self.data = {
            "board": [],
            "store": [None] * 5,
            "gold": 0,
            "level": 0,
            "xp": 0,
            "win_streak": 0,
            "items": {
                "chain_vest": 0,
                "negatron_cloak": 0,
                "needlessly_large_rod": 0,
                "bf_sword": 0,
                "recurve_bow": 0,
                "golden_spatula": 0,
            },
        }

    # main function: reads data from in-game screenshot
    def retrieveData(self, screenshot):
        # run tesseract to locate text
        # recognize champs in store and on board
        # see gold
        # if champ info open, record

        # asssume 1920 by 1080
        img = screenshot
        x = 485
        for i in range(5):
            img1 = PIL.ImageOps.invert(img.crop((x, 1041, x + 140, 1069)))
            img1 = img1.convert("LA")
            self.data["store"][i] = pytesseract.image_to_string(
                img1, config="-c tessedit_char_blacklist=.,"
            )
            x += 201

    def getStore(self):
        return self.data["store"]

