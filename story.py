from Weapon import make_complete_weapon
from god import create_animal_gods_complex
from libraryOfThings import *
from random import *
from Location import *
import resources


def make_collapsible(hashid, title, content):
    return "$a href=\"#" + hashid + "\" class=\"btn btn-info\" data-toggle=\"collapse\"%" + title + "$/a%" + \
           "$p id=\"" + hashid + "\" class=\"collapse\"%" + content + "$p%"

loc = ""
for i in range(10):
    lll = Location()
    loc += str(i) + ")\n " + make_collapsible(lll.name, lll.name,  str(lll))

gods = "\n\n".join(str(i) + ")\n " +
               make_collapsible(g.animal, g.animal, g.summary())
                for g, i in zip(create_animal_gods_complex(8), range(8)))
gods = gods.replace("<", "")
gods = gods.replace(">", "")
gods = gods.replace("$", "<")
gods = gods.replace("%", ">")
weapon = ""
for i in range(20):
    w = make_complete_weapon()
    weapon += str(i) + ")\n "+(make_collapsible(str(hash(w.fullname())), w.fullname(), w.describe())) + "\n"

loc = loc.replace("\n", "<br>\n")
loc = loc.replace("$", "<")
loc = loc.replace("%", ">")

gods = gods.replace("\n", "<br>\n")

weapon = weapon.replace("\n", "<br>\n")
weapon = weapon.replace("$", "<")
weapon = weapon.replace("%", ">")

l = [("location", loc), ("gods", gods), ("weapons", weapon)]

makeHtml(l, "Story.html")

#save_to_file(s, "Location.txt")


