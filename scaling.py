from random import *


# TODO : Add superlative
# has 6 levels with [3] as normal
def create_scaling(low, high):
    return ["very " + low, "quite " + low, low, "average", high, "quite " + high, "very " + high]


def from_scale(scaling):
    c = choice(range(len(scaling)))
    return c, scaling[c]

