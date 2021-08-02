import random


def create_colors(nb: int):
    pile = []
    for i in range(1, nb+1):
        pile.append(i)
    random.shuffle(pile)
    return pile
