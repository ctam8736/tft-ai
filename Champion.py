import json


class Champion:

    with open("Synergies.json", "r") as file:
        synergies = json.load(file)

    with open("stats.json", "r") as file:
        stats = json.load(file)

    def __init__(self, name, star_level):
        try:
            self.name = name
            self.star_level = star_level
            self.tier = self.synergies[name]["Tier"]
            self.origin = self.synergies[name]["Origin"]
            self.classes = self.synergies[name]["Classes"]
            self.items = []
        except KeyError:
            print("'" + name + "' is not a valid TFT champion.")

