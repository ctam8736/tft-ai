from Champion import Champion


class Field:
    def __init__(self):
        self.champions = {}
        self.board_position = [None] * 21
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
        if not champion:
            return
        self.board_position[pos_idx] = champion
        champion.position = ["board", pos_idx]
        if not champion.name in self.champions:
            for champ_origin in champion.origin:
                self.active_synergies[champ_origin]["active"] += 1
            for champ_class in champion.classes:
                self.active_synergies[champ_class]["active"] += 1
            self.champions[champion.name] = {champion.star_level: [champion]}
        else:
            if not champion.star_level in self.champions[champion.name]:
                self.champions[champion.name][champion.star_level] = [champion]
            else:
                self.champions[champion.name][champion.star_level].append(champion)

    def removeChampionFromBoard(self, champion):
        """
        Removes champion from internal board representation and updates synergies. Removing duplicate will not change synergies.
        """
        if not champion:
            return
        for idx, champ in enumerate(self.board_position):
            if champ == champion:
                self.board_position[idx] = None
        if champion.name in self.champions:
            if len(champions[champion.name]) == 1:
                for champ_origin in champion.origin:
                    self.active_synergies[champ_origin]["active"] -= 1
                for champ_class in champion.classes:
                    self.active_synergies[champ_class]["active"] -= 1
                self.champions.pop(champion.name)
            else:
                if len(champions[champion.name][champion.star_level]) == 1:
                    self.champions[champion.name].pop(champion.star_level)
                else:
                    self.champions[champion.name][champion.star_level].remove(champion)

    def addChampionToBench(self, champion):
        """
        Adds champion to internal bench representation at first open slot.
        """
        if not champion:
            return
        for pos_idx, pos in enumerate(self.bench_position):
            if pos is None:
                self.bench_position[pos_idx] = champion
                champion.position = ["bench", pos_idx]
                if not champion.name in self.champions:
                    self.champions[champion.name] = {champion.star_level: [champion]}
                else:
                    if not champion.star_level in self.champions[champion.name]:
                        self.champions[champion.name][champion.star_level] = [champion]
                    else:
                        self.champions[champion.name][champion.star_level].append(
                            champion
                        )
                        if (
                            len(self.champions[champion.name][champion.star_level]) == 3
                            and champion.star_level > 0
                            and champion.star_level < 3
                        ):
                            print("3 champions of star level " + str(champion.star_level) + " found.")
                            # change to different star
                            upgraded_champ = Champion(
                                champion.name, champion.star_level + 1
                            )
                            prev_position = self.champions[champion.name][
                                champion.star_level
                            ][0].position
                            for champ in self.champions[champion.name][
                                champion.star_level
                            ].copy():
                                if champ.position[0] == "board":
                                    self.removeChampionFromBoard(champ)
                                else:
                                    self.removeChampionFromBench(champ)
                            if prev_position[0] == "board":
                                self.addChampionToBoard(upgraded_champ, prev_position[1])
                            else:
                                self.addChampionToBench(upgraded_champ)
                break

    def removeChampionFromBench(self, champion):
        """
        Removes champion from internal bench representation, prioritizing first.
        """
        if not champion:
            return
        for idx, champ in enumerate(self.bench_position):
            if champ == champion:
                self.bench_position[idx] = None
        if champion.name in self.champions:
            if len(self.champions[champion.name]) == 1:
                self.champions.pop(champion.name)
            else:
                if len(self.champions[champion.name][champion.star_level]) == 1:
                    self.champions[champion.name].pop(champion.star_level)
                else:
                    self.champions[champion.name][champion.star_level].remove(champion)

    def hasEmptySpaces(self):
        """
        To do: returns whether the field has an empty bench slot.
        """
        for champ in self.bench_position:
            if champ is None:
                return True
        return False

    def __str__(self):
        return (
            "Bench: "
            + str(list(map(str, self.bench_position)))
            + "\nBoard: "
            + str(self.board_position)
        )
