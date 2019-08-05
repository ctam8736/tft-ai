import math


class Resources:

    checkpoints = [2, 2, 6, 10, 18, 30, 46, 64]

    def __init__(self):
        self.level = 1
        self.xp = 0
        self.gold = 0

    def increaseXpBy(self, n):
        xp += n
        while level < 9 and xp > checkpoints[self.level - 1]:
            xp -= checkpoints[self.level - 1]
            level += 1

    def increaseGoldBy(self, n):
        self.gold += n

    def currentInterest(self):
        return math.floor(min(self.gold, 50) / 10)
