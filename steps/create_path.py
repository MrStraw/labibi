import random

from models import Case
from utils import find_next_path


def create_path(laby):
    tableau = laby.tableau
    paths = find_next_path(tableau)
    while paths:
        path = paths.pop()
        l = path[0]
        c = path[1]
        c0: Case = tableau[l, c]

        if path[2] == '-':
            c1: Case = tableau[l, c-1]
            c2: Case = tableau[l, c+1]

        else:
            c1: Case = tableau[l-1, c]
            c2: Case = tableau[l+1, c]

        if c1.couleur != c2.couleur:
            c1.path.fusion(c2.path)
            c1.path.add_case(c0)
        else:
            if random.random() > 0.9:
                c1.path.add_case(c0)

