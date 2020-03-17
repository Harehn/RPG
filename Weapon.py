from resources import colors, weapons, elements, grades, i_have_the_power
from random import *
from elements import make_elemental_blessing
from filing import save_to_file

class complex_weapon:
    def __init__(self):
        self.color = choice(colors)
        self.weapon = choice(weapons)
        self.element = choice(elements)
        self.blessing = None
        self.maker = ""
        self.history = ""
        self.ego = None
        self.grade = ""
        self.requirement = None

    def __init__(self, c, weapon, el):
        self.color = c
        self.weapon = weapon
        self.element = el
        self.blessing = None
        self.ego = None
        self.grade = ""
        self.requirement = None

    def __str__(self):
        return self.color + " " + self.weapon + (" of " + self.element if self.element else "")

    def fullname(self):
        return self.grade + " " + str(self)

    def describe(self):
        toreturn = "[" + self.fullname() + "]\n"
        toreturn += "A " + self.grade + " " + self.weapon + ". "
        toreturn += (choice(i_have_the_power) + " " + self.element + ". ")if self.element else ""
        toreturn += ("It can deal and mitigate elemental damage of " + self.element + ". ") if self.element else ""
        toreturn += ("It also contains a blessing\n" + str(self.blessing)) if self.blessing else ""
        return toreturn

    def profile(self):
        return self.element



def make_rand_weapon():
    return complex_weapon(choice(colors), choice(weapons), choice(elements + [None]))


def make_complete_weapon():
    w = make_rand_weapon()
    w.grade = choice(grades)
    w.blessing = make_elemental_blessing(choice(elements))
    return w

'''
s = ""
for i in range(20):
    s += (make_complete_weapon().describe()) + "\n"


save_to_file(s, "random_weapons.txt")
'''
