# test code borrowed from Sequal32

import json

with open("Synergies.json", "r") as file:
    synergies = json.load(file)

with open("stats.json", "r") as file:
    stats = json.load(file)

print(synergies)
print(stats)
