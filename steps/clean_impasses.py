def clean_impasses(laby):
    tableau = laby.tableau

    # First clean, on ajoute les chemins:
    for lignes in tableau:
        for case in lignes:
            if case.path:
                case.full_path = True

    # nettoyage
    stop = 0
    while stop != 2:
        stop += 1
        for lignes in tableau:
            for case in lignes:
                if not case.full_path:
                    continue
                if case is laby.depart or case is laby.arrive:
                    continue
                nb_voisin = 0
                for voisin in case.voisins:
                    if voisin.full_path:
                        nb_voisin += 1
                if nb_voisin <= 1:
                    case.full_path = False
                    stop = 0
