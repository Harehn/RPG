

class Blessing:
    def __init__(self, title="", giver=None):
        self.title = title
        self.given_by = giver
        self.effect = None
        self.power = None

    def __str__(self):
        to_return = "[" + self.title + "]\n"
        if self.given_by:
            to_return += "Given by " + self.given_by
        if self.effect:
            to_return += "\n" + self.effect + "\n"
        return to_return

class Curse:
    def __init__(self):
        self.title = ""
        self.given_by = None
        self.effect = None