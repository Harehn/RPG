from god import *
from libraryOfThings import *
from language import *
from filing import *
from resources import *



def try1():
    gods = create_animal_gods(12)
    create_allies(gods, 3)
    save_to_file("\n\n".join(i.summary() for i in gods), "gods1.txt")


def try2():
    gods = create_animal_gods_complex(8)
    save_to_file("\n\n".join(i.summary() for i in gods), "gods2.txt")
    return gods


# save_object(try2(), "gods.pkl")
def describing_gods():
    gods = create_animal_gods_complex(12)

    print(gods[0].describe())


def doing_plurals():
    print("\n".join(map(plural, animals)))


def list_elements():
    print("\n".join([i + " aura" for i in elements]))


def sort_file():
    d = load_dict("_weapons.txt")
    d["weapons"].sort()
    save("_weapons.txt", d)


def rand_weapons():
    return " ".join([choice(colors), choice(weapons), "of", choice(elements)])


def weapons():
    wp = {"weapons": [rand_weapons() for i in range(23)]}
    save("random_weapons.txt", wp)

    print(wp)


#describing_gods()
#list_elements()

