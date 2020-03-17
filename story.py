from Weapon import make_complete_weapon
from god import create_animal_gods_complex
from libraryOfThings import *
from random import *
from Location import *
import resources


loc = ""
for i in range(10):
    loc += str(i) + ")\n " + str(Location()) + '\n----------------------------\n'

gods = "\n\n".join(str(i) + ")\n " + g.summary() for g, i in zip(create_animal_gods_complex(8), range(8)))
gods = gods.replace("<", "")
gods = gods.replace(">", "")
weapon = ""
for i in range(20):
    weapon += str(i) + ")\n "+(make_complete_weapon().describe()) + "\n"
loc = loc.replace("\n", "<br>\n")
gods = gods.replace("\n", "<br>\n")
weapon = weapon.replace("\n", "<br>\n")
l = [("location", loc), ("gods", gods), ("weapons", weapon)]

makeHtml(l, "Story.html")

#save_to_file(s, "Location.txt")


