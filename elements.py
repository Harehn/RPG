from resources import elements, effects
from blessing import *
from scaling import *


def make_elemental_blessing(el, power=from_scale(create_scaling("weak", "strong"))):
    b = Blessing(str(power[1]) + " blessing of " + el, el)
    b.effect = choice(effects) + " " + el
    return b

'''
for i in range(10):
    print(make_elemental_blessing(choice(elements)))
'''

