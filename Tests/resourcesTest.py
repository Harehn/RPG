import unittest

from filing import load_dict
from resources import colors, animals, elements, effects, i_have_the_power, weapons, grades


class MyTestCase(unittest.TestCase):
    c = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Brown', 'Magenta', 'Tan', 'Cyan', 'Olive', 'Maroon',
         'Navy', 'Aquamarine', 'Turquoise', 'Silver', 'Lime', 'Teal', 'Indigo', 'Violet', 'Pink', 'Black', 'White',
         'Gray', 'Grey']

    a = ['alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat', 'cheetah', 'chicken', 'chimpanzee', 'cow',
         'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'elephant', 'fish', 'fly', 'fox', 'frog', 'giraffe',
         'goat', 'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo', 'kitten', 'lion', 'lobster', 'monkey',
         'octopus', 'owl', 'panda', 'pig', 'rabbit', 'rat', 'scorpion', 'seal', 'shark', 'sheep', 'snail', 'snake',
         'spider', 'squirrel', 'tiger', 'turtle', 'wolf', 'zebra']

    e = ['fire', 'wind', 'water', 'ice', 'earth', 'darkness', 'light', 'blood', 'lightning', 'nature', 'poison',
         'psychic', 'curse', 'divine', 'shadow']

    eff = ['Increases the attack power of', 'Grants you an aura of', 'Increases your resistance to',
           'Decreases the damage gained from', 'Decreases the use of mana when using the element of',
           'Makes your scent more favourable to spirits of', 'Allows you to use some mana to send a ball of',
           'Allows you to use some mana to send an arrow of', 'Allows you to use some mana to create a sword of',
           'You can now cast faster spells of', 'Occasionally leads you to sources of power of',
           'You can use this blessing to increase another blessing of']
    power = ['It is imbued with the power of ', 'It contains the power of ', 'It has inside of it the power of ',
             'It has the power of ', 'It is enchanted with the power of ', 'It emits the faint aura of the power of ',
             'It has been bestowed the aura of the power of ', 'One can sense in it the aura of the power of ',
             'It is imbued with the element of ', 'It contains the element of ', 'It has inside of it the element of ',
             'It has the element of ', 'It is enchanted with the element of ',
             'It emits the faint aura of the element of ',
             'It has been bestowed the aura of the element of ', 'One can sense in it the aura of the element of ',
             'It is imbued with', 'It contains', 'It has inside of it', 'It has', 'It is enchanted with',
             'It emits the faint aura of', 'It has been bestowed the aura of', 'One can sense in it the aura of']
    w = ['Batons', 'Battle axe', 'Caltrops', 'Crossbow', 'Daggers', 'Falchion Sword', 'Flail', 'Greatsword', 'Halberd',
         'Lance', 'Longbow', 'Longsword', 'Mace', 'MorningStar', 'Scimitar', 'Spear', 'Sword', 'Warhammer']
    g = ['Broken', 'Common', 'Uncommon', 'Rare', 'Epic', 'Mythic', 'Legendary', 'Divine']

    def test_load_dict(self):
        self.assertEqual(colors, self.c)
        self.assertEqual(animals, self.a)
        self.assertEqual(elements, self.e)
        self.assertEqual(effects, self.eff)
        self.assertEqual(i_have_the_power, self.power)
        self.assertEqual(weapons, self.w)
        self.assertEqual(grades, self.g)


if __name__ == '__main__':
    unittest.main()
