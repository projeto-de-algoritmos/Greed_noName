import random

def randomGenerator(_list, size):
    list = _list
    for count in range(0, size):
        list.append(random.randint(1, 20))

    return list