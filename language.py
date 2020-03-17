from re import *
import re
from random import *
punctuation = "\':,-.!()?\";"

texting = {
    "l": "7",
    "i": "1",
    "m": "nn",
    "e": "3",
    "d": "b",
    "b": choice(["d", "8", "6"]),
    "o": "0",
    "s": "5",
    "w": "vv",
}

d = {
    0: lambda w: w.upper(),
    1: lambda w: w.lower(),
    2: lambda w: spongeBob(w),
    3: lambda w: w + "...",
    4: lambda w: w + "!" * (choice(range(7)) + 1),
    5: lambda w: w * (choice(range(7)) + 1),
    6: lambda w: "".join([texting[i] if (i in texting) else i for i in w]),
    7: lambda w: w[::-1],
    8: lambda w: "".join(sample(list(w), len(w))),
    9: lambda w: choice(list("!?.,\'\":;-_/[]{}()")).join(list(w)),
    4: lambda w: w + "?" * (choice(range(7)) + 1),

    # ---- Non words
    10: lambda w: "".join([choice(["X", "x"]) for i in range(choice(range(8)))]) + "x",
    11: lambda w: " " + "".join([str(choice(range(9))) for i in range(choice(range(4)))]) + " ",
    12: lambda w: spongeBob("haha" * choice(range(5))),
    13: lambda w: choice(list("Hh")) + spongeBob(("mm" * choice(range(7)))),

}

def listing(l):
    if len(l) > 3:
        return listing(sample(l,3))
    if len(l) > 1:
        return ",".join(l[:-1]) + " and " + l[-1]
    else:
        return l[0]


def plural(word):
    if word[-2:] == "ey":
        return word + "s"
    if word[-1] in "hxs":
        return word + "es"
    elif word[-1] in "y":
        return word[:-1] + "ies"
    else:
        return word + "s"


def make_male(s):
    l = re.split('(\W)' , s)


def make_god_titles(obj):
    titles = ["God of " + plural(obj),
              "The Great " + obj.capitalize() + " God",
              "Lord of " + plural(obj),
              "The Great " + obj.capitalize() + " Lord",
              "The One who governs over " + plural(obj),
              "The One who presides over " + plural(obj)]
    return titles


def crazy(word):


    #return [d[i](word) for i in range(14)]
    return "".join([choice(d)(word) + choice(["" * 3] + [" ", "."] * 7 + ["\n"]) + " " for i in range(100)])


def synonym(word):
    return word


def spongeBob(word):
    return "".join([choice([i.upper(), i.lower()]) for i in word])

#print(crazy("Exterminate"))