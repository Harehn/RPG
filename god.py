from resources import *
from language import *
from filing import *
from scaling import *
from libraryOfThings import *
from Weapon import *

class God:
    def __init__(self):
        self.title = []
        self.gender = choice(list(zip(["male", "female", "genderless"], list(range(3)))))
        self.power_level = from_scale(create_scaling("weak", "strong"))
        self.disappeared = choice([True, False])
        self.cruelty = from_scale(create_scaling("kind", "cruel"))
        self.following = from_scale(create_scaling("small", "large"))
        self.interference = from_scale(create_scaling("rarely", "Often"))
        self.favourite_color = choice(colors)
        self.belief = choice([(0, "monotheist"), (1, "polytheist")])
        self.elements = sample(elements, choice(range(3)) + 1)
        self.weapons = complex_weapon(self.favourite_color, choice(weapons), choice(self.elements))
        self.opponents = []
        self.opponents_titles = []
        self.allies = []
        self.allies_titles = []
        self.factions = ""
        self.symbol = ""

        self.champions = []
        self.rituals = []

    def __str__(self):
        return "\n".join(str(k) + " : " + str(v) for k, v in vars(self).items())

    def summary(self):
        return "\n".join(str(k) + " : " + str(v) for k, v in vars(self).items() if v)

    def set_ally(self, god2):
        if god2 in self.allies or self.opponents:
            return False
        else:
            god2.allies.append(self)
            god2.allies_titles.append(self.title[0])
            self.allies.append(god2)
            self.allies_titles.append(god2.title[0])
            return True

    def set_opponent(self, god2):
        if god2 in self.allies or self.opponents:
            return False
        else:
            god2.opponents.append(self)
            god2.opponents_titles.append(self.title[0])
            self.opponents.append(god2)
            self.opponents_titles.append(god2.title[0])
            return True

    # god, follower, impartial, enemy??
    def describe(self):
        description = choice(introductions_for_gods)
        description += "His holy name is " + self.title[0] if self.title else "unknown"
        description += ". "
        if self.title[:-1] and make_choice():
            description += "Followers also call him " + listing(self.title[1:])
            description += ". "
        self.disappeared

        return description


class AnimalGod(God):
    def __init__(self, animal):
        super().__init__()
        self.title.extend(make_god_titles(animal))
        self.animal = animal

    def send_animal(self):
        return "Giant " + self.favourite_color + " " + self.animal


def create_animal_gods(num):
    return [AnimalGod(animal) for animal in sample(animals, num)]


def save_list_to_file(lgods, file_name ="gods.txt"):
    save_to_file("\n\n".join(str(i) for i in lgods), file_name)


def create_allies(lgods, num):
    for i in range(num):
        buddies = sample(lgods, 2)
        success = False
        while not success:
            success = buddies[0].set_ally(buddies[1])
            success = True


def create_opponents(lgods, num):
    for i in range(num):
        buddies = sample(lgods, 2)
        success = False
        while not success:
            success = buddies[0].set_opponent(buddies[1])
            success = True


def make_2_factions(lgods):
    lgods[0].factions = 1
    faction1 = [lgods[0]]
    faction2 = []
    for god in lgods[:-1]:
        if make_choice():
            god.set_ally(lgods[0])
            god.factions = 1
            faction1.append(god)
        else:
            god.set_opponent(lgods[0])
            god.factions = 2
            faction2.append(god)
    return faction1, faction2


def make_relationships(lgods):
    if make_choice():
        make_2_factions(lgods)
    else:
        create_allies(lgods, choice(range(int(len(lgods)/2))))
        create_opponents(lgods, choice(range(int(len(lgods)/2))))


def create_animal_gods_complex(num):
    gods = create_animal_gods(num)
    make_relationships(gods)
    return gods


def get_good_bad(lgods):
    good = [x for x in lgods if x.cruelty[1] < 3]
    bad = [x for x in lgods if x.cruelty[1] > 3]
    indifferent = [x for x in lgods if x.cruelty[1] == 3]
    return good, bad, indifferent

