from resources import *
from random import *
from resources import weapons, elements
import resources

# keep_doing(lamda ()->save(...))
def keep_doing(action, start_msg="Starting Program...", msg="Continue?"):
    print(start_msg)
    while input(msg+"(Y/N)").upper() == "Y":
        action()


def make_choice():
    return choice([True, False])


#keep_doing(lambda: print("hello"))



