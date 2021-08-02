from models import Case


def mesure_distance(laby):
    case_depart: Case = laby.depart
    case_arrive: Case = laby.arrive
    tableau = laby.tableau
    # temps que la case arrive n'est pas mesuré, on parcour tout le tableau
    # et on ajoute +1 au case adjacentes qui sont un chemin
    case_depart.distance = 1
    cpt = 0
    while not case_arrive.distance:
        cpt += 1
        for ligne in tableau:
            for case in ligne:
                if case.distance == cpt:
                    for voisin in case.voisins:
                        if not voisin.path or voisin.distance:
                            continue
                        voisin.distance = cpt + 1
