#from god import *
from Location import Subarea
from filing import *

colors = [i[0] for i in load_dict("_colors.txt")["colors"]]
animals = [i[0] for i in load_dict("_animals.txt")["animals"]]
elements = [i[0] for i in load_dict("_elements.txt")["elements"]]
# Need to add the ability to use magic
effects = [i[0] for i in load_dict("_elements.txt")["effects"]]

i_have_the_power = [i[0] for i in load_dict("_elements.txt")["I_have_the_power"]]
i_have_the_power1 = [s + " the power of " for s in i_have_the_power]
i_have_the_power2 = [s + " the element of " for s in i_have_the_power]
i_have_the_power = i_have_the_power1 + i_have_the_power2 + i_have_the_power


weapons = [i[0] for i in load_dict("_weapons.txt")["weapons"]]
grades = [i[0] for i in load_dict("_grades.txt")["grades"]]

locationType = ["populated_areas", "wilderness"]
populated_areas = [i[0] for i in load_dict("_places.txt")["populated_areas"]]
wilderness = [i[0] for i in load_dict("_places.txt")["wilderness"]]
location = {
    "populated_areas": populated_areas,
    "wilderness": wilderness
}
locationName = [i[0] for i in load_dict("_places.txt")["names"]]
everything = [colors, animals, elements, weapons, grades]
sublocations_populated = [Subarea(i[0]) for i in load_dict("_places.txt")["subareas_for_populated_areas"]]
sublocations_wilderness = [Subarea(i[0]) for i in load_dict("_places.txt")["subareas_for_wilderness_areas"]]
guilds = [Subarea(i[0] + " guild", "guilds") for i in load_dict("_jobs.txt")["types"]]
stores = [Subarea(i[0] + " store", "stores") for i in load_dict("_places.txt")["stores"]]
worship = [Subarea(i[0], "place of worship") for i in load_dict("_places.txt")["place_of_worship"]]
towers = [Subarea(i[0] + " towers", "guilds") for i in elements]
sublocations_populated += guilds + stores + worship
sublocations_wilderness += worship
sublocation = {
    "populated_areas": sublocations_populated,
    "wilderness": sublocations_wilderness
}
#  ___GOD____
introductions_for_gods = ["He is one of the many gods that inhabit this world. ",
                          "Praise be to Him! ",
                          "Open your ears and listen to his story. ",
                          "He is a divine being. "]
introductions_for_animal_gods = []
