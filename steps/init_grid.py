import numpy as np

from models import Case, Path
from utils import create_colors


def init_grid(largeur: int, hauteur: int):

    nb_wall = int(((largeur-1)/2) * ((hauteur-1)/2))
    colors = create_colors(nb_wall)

    tableau = np.zeros((hauteur, largeur), dtype=Case)
    for x in range(hauteur):
        for y in range(largeur):
            if not x % 2:  # pair
                tableau[x, y] = Case(x, y, tableau)
            else:
                if x % 2 and y % 2:
                    c = Case(x, y, tableau)
                    p = Path(colors.pop())
                    p.add_case(c)
                    tableau[x, y] = c
                else:
                    tableau[x, y] = Case(x, y, tableau)

    path_depart: Path = tableau[1, 1].path
    case_depart: Case = tableau[1, 0]
    path_depart.add_case(case_depart)
    case_depart.is_depart = True

    path_arrive: Path = tableau[hauteur-2, largeur-2].path
    case_arrive: Case = tableau[hauteur-2, largeur-1]
    path_arrive.add_case(case_arrive)
    case_arrive.is_arrive = True

    return tableau
