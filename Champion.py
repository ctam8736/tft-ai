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
            self.position = ["", 0]
            self.items = [None] * 3
        else:
            # print("'" + name + "' is not a valid TFT champion.")
            self.name = None

    """
    def __eq__(self, other):
        if isinstance(other, Champion):
            return self.name == other.name and self.tier == other.tier and self.items == other.items
    """

    def __str__(self):
        if self.name is None:
            return "Empty champion."
        return self.name + ": " + str(self.star_level)
