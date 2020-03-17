from random import choice, choices
import resources
from scaling import create_scaling, from_scale


class Location:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.subtype = ""
        self.size = ""
        self.magic_level = ""
        self.magic_type = ""
        self.ecology = ""
        self.subareas = []
        self.population = ""
        self.make_random()

    def make_random(self):
        self.type = choice(resources.locationType)
        self.size = from_scale(create_scaling("small", "big"))
        self.subtype = choice(resources.location[self.type])
        self.name = choice(resources.locationName)
        self.magic_level = from_scale(create_scaling("faint", "dense"))
        self.magic_type = choice(resources.elements + ["neutral"])
        self.subareas = choices(resources.sublocation[self.type], k=self.size[0]+3)

    def __str__(self):
        return "\n".join(str(k) + " : " + str(v) if k != "subareas" else str(k) + " : " + "\n\n".join(str(i) for i in v)
                         for k, v in vars(self).items())


class Subarea:
    def __init__(self, name, types="general"):
        self.name = name
        self.size = ""
        self.type = types
        self.magic_level = ""
        self.magic_type = ""
        self.make_random()

    def make_random(self):
        self.size = from_scale(create_scaling("small", "big"))
        self.magic_level = from_scale(create_scaling("faint", "dense"))
        self.magic_type = choice(resources.elements + ["neutral"])

    def __str__(self):
        return "[" + self.name + "]\n" + "\n".join(str(k) + " : " + str(v) for k, v in vars(self).items())

class Worship(Subarea):
    def __init__(self, name, god):
        super(name, types="place of worship")
        self.god = god
