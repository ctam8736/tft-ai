class Field:
    def __init__(self):
        self.champions = {}
        self.board_position = [None] * 21
        self.board_used = 0
        self.board_capacity = 1
        self.bench_position = [None] * 9
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

    def addChampionToBoard(self, champion, pos_idx):
        """
        Adds champion to internal board representation and updates synergies. Duplicate champions will not proc additional synergies.
        """
        self.board_position[pos_idx] = champion
        if not champion.name in self.champions:
            for champ_origin in champion.origin:
                self.active_synergies[champ_origin]["active"] += 1
            for champ_class in champion.classes:
                self.active_synergies[champ_class]["active"] += 1
            self.champions[champion.name] = 1
        else:
            self.champions[champion.name] += 1

    def removeChampionFromBoard(self, champion):
        """
        Removes champion from internal board representation and updates synergies. Removing duplicate will not change synergies.
        """
        for idx, champ in enumerate(board_position):
            if champ == champion:
                board_position[idx] = None
        if champion.name in self.champions:
            if champions[champion.name] == 1:
                for champ_origin in champion.origin:
                    self.active_synergies[champ_origin]["active"] -= 1
                for champ_class in champion.classes:
                    self.active_synergies[champ_class]["active"] -= 1
                self.champions.pop(champion.name)
            else:
                self.champions[champion.name] -= 1

    def addChampionToBench(self, champion):
        """
        Adds champion to internal bench representation at first open slot.
        """
        for pos_idx, pos in enumerate(position):
            if pos is None:
                bench_position[pos_idx] = champion
                if not champion.name in self.champions:
                    self.champions[champion.name] = 1
                else:
                    self.champions[champion.name] += 1
                break

    def removeChampionFromBench(self, champion):
        """
        Removes champion from internal bench representation, prioritizing first.
        """
        for idx, champ in enumerate(bench_position):
            if champ == champion:
                bench_position[idx] = None
        if champion.name in self.champions:
            if champions[champion.name] == 1:
                self.champions.pop(champion.name)
            else:
                self.champions[champion.name] -= 1

    def hasEmptySpaces(self):
        """
        To do: returns whether the field has an empty bench or board slot.
        """
        if self.board_used < self.board_capacity:
            return True
        for champ in self.bench_position:
            if champ is None:
                return True
        return False

