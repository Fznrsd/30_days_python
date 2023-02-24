from random import random, randint
import random
import string



def random_user_id():
    a = randint(100000, 999999)
    return a


def random_user():
    rad1 = []
    for i in range(6):
        rand = random.choice(string.ascii_letters + string.digits)
        rad1.append(rand)
    return rad1


def user_id_gen_by_user():
    rad1 = []
    x1 = eval(input("fst no.: "))
    x2 = eval(input("2nd no.: "))
    for x in range(x1):
        for i in range(x2):
            rand = random.choice(string.ascii_letters + string.digits)
            rad1.append(rand)
        rad1.append("\n")
    y = "".join(rad1)
    print(y)


def list_of_clr(typ, numbr):
    rad1 = []
    if typ == "hexa":
        x1 = 6
    if typ == "rgb":
        x1 = 3    
    for x in range(numbr):
        for i in range(x1):
            rand = random.choice(string.hexdigits)
            rad1.append(rand)
        rad1.append("\n")
    y = "".join(rad1)
    print(y)


def shuffle_list(lst):
    random.shuffle(lst)
    print(lst)


def aray():
    ar = []
    for w in range(7):
        x3 = randint(0, 9)
        ar.append(x3)
    return ar


