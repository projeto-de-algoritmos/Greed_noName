import random

def random_insert(_list, amount):
    for index in range(amount):
        _list.append(random.randint(1,amount))
    random.shuffle(_list)
    return _list