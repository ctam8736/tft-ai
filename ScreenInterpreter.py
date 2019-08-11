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
        """
        Retrieves relevant data (e.g. champs, gold, items, etc.) from the latest screenshot.
        """
        # run tesseract to locate text
        # recognize champs in store and on board
        # see gold
        # if champ info open, record

        # update store
        x = 485
        for i in range(5):
            self.data["store"][i] = self.read(
                self.cropAndEdit(screenshot, x, 1041, x + 140, 1069)
            )
            x += 201

        # update gold
        """
        thresh = 150
        fn = lambda x: 255 if x > thresh else 0
        screenshot = (
            self.cropAndEdit(screenshot, 873, 881, 906, 910)
            .resize((200, 200), Image.ANTIALIAS)
            .convert("L")
            .point(fn, mode="1")
        )
        ## Modified from source 20190810
        str_gold = self.read(screenshot, whitelist="0123456789")
        if(len(str_gold) < 1):
            str_gold = = pytesseract.image_to_string(screenshot,
                            config="--psm 10 -c tessedit_char_whitelist=0123456789")
        self.data["gold"] = int(str_gold)
        ## EndModified
        """

    def cropAndEdit(self, img, x1, y1, x2, y2):
        """
        Crops, inverts, and desaturates image.
        """
        img1 = PIL.ImageOps.invert(img.crop((x1, y1, x2, y2)))
        img1 = img1.convert("LA")
        img1.save("out.png")
        return img1

    def read(self, img, blacklist=".,", whitelist=None):
        """
        Performs the tesseract operation on a cropped image after inversion and desaturation.
        """
        if whitelist:
            return pytesseract.image_to_string(
                img, config="-c tessedit_char_whitelist=" + whitelist
            )
        else:
            return pytesseract.image_to_string(
                img, config="-c tessedit_char_blacklist=" + blacklist
            )

    def getStore(self):
        """
        Returns array containing champions found in store (use after retrieval).
        """
        return self.data["store"]

    def getGold(self):
        """
        Returns current gold count (use after retrieval).
        """
        return self.data["gold"]
