class Bench:
    def __init__(self):
        self.champions = {}
        self.position = [None] * 9

    def addChampion(self, champion):
        """
        Adds champion to internal bench representation.
        """
        for pos_idx, pos in enumerate(position):
            if pos is None:
                position[pos_idx] = champion
                if not champion.name in self.champions:
                    self.champions[champion.name] = 1
                else:
                    self.champions[champion.name] += 1
                break

    def removeChampion(self, champion):
        """
        Removes champion from internal bench representation.
        """
        if champion.name in self.champions:
            if champions[champion.name] == 1:
                self.champions.pop(champion.name)
            else:
                self.champions[champion.name] -= 1

    def getChampions(self):
        """
        Returns the champions set.
        """
        return self.champions
