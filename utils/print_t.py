from models import Case


def print_t(tableau, mode: str = 'couleur'):
    l_ligne = tableau.shape[0]
    l_colone = tableau.shape[1]

    if mode == 'couleur':
        print(tableau)

    elif mode == 'distance':
        arrive: Case = tableau[l_ligne - 2, l_colone - 1]
        t = len(str(arrive.distance))
        s = ''
        for lignes in tableau:
            s += '\n'
            for case in lignes:
                s2 = ''
                if case.is_arrive:
                    s2 += "A"
                elif case.is_depart:
                    s2 += "D"
                elif case.path:
                    if case.distance == 0:
                        s2 += '*'
                    else:
                        s2 += str(case.distance)
                else:
                    s2 += ' '

                while len(s2) < t:
                    if case.is_arrive:
                        s2 += "A"
                    elif case.is_depart:
                        s2 += "D"
                    elif case.path:
                        if case.distance == 0:
                            s2 += '*'
                        else:
                            s2 = '0' + s2
                    else:
                        s2 += ' '
                s += s2 + ' '
        print(s)

    else:
        s = ''
        for ligne in tableau:
            s += '\n'
            for case in ligne:
                if not case.path:
                    wall_neig = search_wall_around(case)
                    if wall_neig == [1, 0, 1, 0]:
                        s += '═══'
                    elif wall_neig == [1, 0, 0, 0]:
                        s += ' ══'
                    elif wall_neig == [0, 0, 1, 0]:
                        s += '══ '
                    elif wall_neig == [0, 1, 0, 0] or wall_neig == [0, 0, 0, 1] or wall_neig == [0, 1, 0, 1]:
                        s += ' ║ '
                    elif wall_neig == [1, 0, 0, 1]:
                        s += ' ╚═'
                    elif wall_neig == [0, 0, 1, 1]:
                        s += '═╝ '
                    elif wall_neig == [0, 1, 1, 0]:
                        s += '═╗ '
                    elif wall_neig == [1, 1, 0, 0]:
                        s += ' ╔═'
                    elif wall_neig == [1, 0, 1, 1]:
                        s += '═╩═'
                    elif wall_neig == [1, 1, 1, 0]:
                        s += '═╦═'
                    elif wall_neig == [1, 1, 0, 1]:
                        s += ' ╠═'
                    elif wall_neig == [1, 1, 1, 1]:
                        s += '═╬═'
                    elif wall_neig == [0, 1, 1, 1]:
                        s += '═╣ '
                    elif wall_neig == [0, 0, 0, 0]:
                        s += ' ■ '
                else:
                    if mode == 'lab':
                        s += '   '
                    elif mode == 'solution':
                        if case.solution == 1:
                            s += ' · '
                        else:
                            s += '   '
                    elif mode == 'full_path':
                        if case.solution == 1:
                            s += ' · '
                        elif case.full_path:
                            s += '   '
                        else:
                            s += ' x '
        print(s)


def search_wall_around(case: Case):
    tableau = case.tableau
    l_ligne = tableau.shape[0]
    l_colone = tableau.shape[1]
    tableau = case.tableau
    if case.loc == (0, 0):
        return [1, 0, 1, 0]
    if case.loc == (2, 0):
        return [0, 1, 1, 0]
    if case.loc == (l_ligne - 3, l_colone - 1):
        return [1, 0, 0, 1]
    if case.loc == (l_ligne - 1, l_colone - 1):
        return [1, 0, 1, 0]

    tuples = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    liste_voisin = [0, 0, 0, 0]
    for i, t in enumerate(tuples):
        ligne_v = t[0] + case.ligne
        colone_v = t[1] + case.colone
        try:
            case_voisine: Case = tableau[ligne_v, colone_v]
        except IndexError:
            continue
        if 0 > ligne_v > l_ligne - 1 or 0 > colone_v > l_colone - 1:
            continue
        if not case_voisine.path:
            liste_voisin[i] = 1
        if case.ligne == 0:
            liste_voisin[3] = 0
        if case.colone == 0:
            liste_voisin[2] = 0
    return liste_voisin
