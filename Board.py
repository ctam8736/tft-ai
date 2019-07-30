class Board:
    def __init__(self):
        self.champions = {}
        self.position = [None] * 21
        self.active_synergies = {
            "Assassin": {"active": 0, "required": [3, 6]},
            "Blademaster": {"active": 0, "required": [3, 6]},
            "Brawler": {"active": 0, "required": [2, 4]},
            "Elementalist": {"active": 0, "required": [3]},
            "Guardian": {"active": 0, "required": [2]},
            "Gunslinger": {"active": 0, "required": [2, 4]},
            "Knight": {"active": 0, "required": [2, 4, 6]},
            "Ranger": {"active": 0, "required": [2, 4]},
            "Shapeshifter": {"active": 0, "required": [3]},
            "Sorcerer": {"active": 0, "required": [3, 6]},
            "Demon": {"active": 0, "required": [2, 4, 6]},
            "Dragon": {"active": 0, "required": [2]},
            "Exile": {"active": 0, "required": [1]},
            "Glacial": {"active": 0, "required": [2, 4, 6]},
            "Imperial": {"active": 0, "required": [2, 4]},
            "Ninja": {"active": 0, "required": [1, 4]},
            "Noble": {"active": 0, "required": [3, 6]},
            "Phantom": {"active": 0, "required": [2]},
            "Pirate": {"active": 0, "required": [3]},
            "Robot": {"active": 0, "required": [1]},
            "Void": {"active": 0, "required": [3]},
            "Wild": {"active": 0, "required": [2, 4]},
            "Yordle": {"active": 0, "required": [3, 6]},
        }

    def addChampion(self, champion, pos_idx):
        """
        Adds champion to internal board representation and updates synergies. Duplicate champions will not proc additional synergies.
        """
        self.position[pos_idx] = champion
        if not champion.name in self.champions:
            for champ_origin in champion.origin:
                self.active_synergies[champ_origin]["active"] += 1
            for champ_class in champion.classes:
                self.active_synergies[champ_class]["active"] += 1
            self.champions[champion.name] = 1
        else:
            self.champions[champion.name] += 1

    def removeChampion(self, champion):
        """
        Removes champion from internal board representation and updates synergies. Removing duplicate will not change synergies.
        """
        if champion.name in self.champions:
            if champions[champion.name] == 1:
                for champ_origin in champion.origin:
                    self.active_synergies[champ_origin]["active"] -= 1
                for champ_class in champion.classes:
                    self.active_synergies[champ_class]["active"] -= 1
                self.champions.pop(champion.name)
            else:
                self.champions[champion.name] -= 1

    def printActive(self):
        """
        Prints all existing synergies of represented champions.
        """
        for synergy in self.active_synergies:
            if self.active_synergies[synergy]["active"] > 0:
                print(synergy + ": " + str(self.active_synergies[synergy]["active"]))

    def printSearching(self):
        """
        To do: print existing synergies ordered by least additions to requirement.
        """
        for synergy in self.active_synergies:
            pass

    def getChampions(self):
        """
        Returns the champions set.
        """
        return self.champions
