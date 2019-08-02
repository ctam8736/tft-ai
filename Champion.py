import json


class Champion:

    # static champion data for easy synergy and stat access

    with open("Synergies.json", "r") as file:
        synergies = json.load(file)

    with open("stats.json", "r") as file:
        stats = json.load(file)

    def __init__(self, name, star_level):
        if name in self.synergies:
            self.name = name
            self.star_level = star_level
            self.tier = self.synergies[name]["Tier"]
            self.origin = self.synergies[name]["Origin"]
            self.classes = self.synergies[name]["Classes"]
            self.items = [None] * 3
        else:
            print("'" + name + "' is not a valid TFT champion.")
            self.name = None
            self.star_level = 0
            self.tier = None
            self.origin = None
            self.classes = None
            self.items = [None] * 3

    """
    def __eq__(self, other):
        if isinstance(other, Champion):
            return self.name == other.name and self.tier == other.tier and self.items == other.items
    """

    def __str__():
        return name + ": Star Level " + str(star_level)

