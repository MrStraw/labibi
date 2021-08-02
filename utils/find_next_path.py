import random


def find_next_path(tableau):
    l_ligne = tableau.shape[0]
    l_colone = tableau.shape[1]
    pile = []

    for x in range(2, l_ligne - 2, 2):
        for y in range(1, l_colone, 2):
            pile.append((x, y, '|'))

    for x in range(1, l_ligne, 2):
        for y in range(2, l_colone - 2, 2):
            pile.append((x, y, '-'))

    random.shuffle(pile)
    return pile
