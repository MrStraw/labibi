from models import Case


def resoudre_lab(laby):
    case_arrive: Case = laby.arrive
    case_arrive.solution = 1
    find(case_arrive)


def find(case):
    choosen = None
    for voisin in case.voisins:
        if not voisin.path or voisin.solution == -1:
            continue
        if not voisin.solution:
            if choosen is None:
                choosen = voisin
            elif voisin.distance < choosen.distance:
                choosen.solution = -1
                choosen = voisin
    if choosen:
        choosen.solution = 1
        if not choosen.is_depart:
            find(choosen)
