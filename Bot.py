from ScreenInterpreter import ScreenInterpreter
from PlayerControl import PlayerControl
from Field import Field
from Champion import Champion
import pyautogui


class Bot:

    star_values = [1, 1.8, 3.6]

    def __init__(self):
        self.info_reader = ScreenInterpreter()
        self.controller = PlayerControl()
        self.field = Field()

    def runBot(self):
        """
        Starts the main AI loop.
        """
        print("Running...")
        self.info_reader.retrieveData(pyautogui.screenshot())
        print("Identified champs from store: " + str(self.info_reader.getStore()))
        print("Identified gold total: " + str(self.info_reader.getGold()))

    def valueOf(self, champion):
        """
        Returns the champion's estimated value to the bot.
        """
        if champion is None:
            return 0
        return self.star_values[champion.star_level - 1] * (1 + 0.2 * champion.tier)

    def purchaseLoop(self):
        """
        To do: buys best candidate champions from the store in exchange for empty/low-value champions on field.
        """

        #if bench is full, find worst champion
        min_value = -1
        worst_idx = 0
        if not self.field.hasEmptySpaces():
            # find minimum champion on bench
            bench_champ_values = list(map(self.valueOf, self.field.bench_position))
            min_value = bench_champ_values[0]
            for idx, value in enumerate(bench_champ_values):
                if value < min_value:
                    min_value = value
                    worst_idx = idx
            print(
                "Worst champion: "
                + str(self.field.bench_position[worst_idx])
                + " at value "
                + str(min_value)
            )

        #find best champion in store
        self.info_reader.retrieveData(pyautogui.screenshot())
        store_champ_values = list(
            map(
                (lambda champ_name: self.valueOf(self.championFromName(champ_name))),
                self.info_reader.data["store"],
            )
        )
        max_value = 0
        best_idx = 0
        for idx, value in enumerate(store_champ_values):
            if value > max_value:
                max_value = value
                best_idx = idx
        print(
            "Best champion: "
            + str(self.info_reader.data["store"][best_idx])
            + " at value "
            + str(max_value)
        )

        #if bench can be improved, exchange
        if min_value < max_value:
            if min_value > 0:
                self.controller.sellChampion(worst_idx)
            self.buyChampion(best_idx)
        print(self.info_reader.data["store"])
        print(store_champ_values)

    def buyChampion(self, store_idx):
        """
        Buys champion at store index. (Clicks and adds to internal field.)
        """
        self.controller.buyChampion(store_idx)
        self.field.addChampionToBench(
            self.championFromName(self.info_reader.data["store"][store_idx])
        )

    def sellChampion(self, bench_idx):
        """
        Sells champion at bench index. (Targets with 'E' and removes from internal field.)
        """
        self.controller.sellChampion(bench_idx)
        self.field.removeChampionFromBench(bench_idx)

    def championFromName(self, champ_name):
        champ = Champion(champ_name, 1)
        if champ.name is None:
            return None
        else:
            return champ

    def decideReroll(self):
        """
        Returns true if rerolling is favorable.
        """
        return False

    def optimizeBoard(self):
        """
        To do: from pool of champs, make best (synergistic) board configuration.
        """
        pass
