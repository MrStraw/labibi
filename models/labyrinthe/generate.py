import random
from time import sleep

from numpy import ndarray
import tkinter as tk

from models import Case
from steps import init_grid, mesure_distance, resoudre_lab, clean_impasses
from utils import find_next_path, int_to_grad_hexa


def generate(laby):
    canvas = laby.canvas
    # canvas.update()
    # return

    # ----- Création du tableau
    laby.tableau = init_grid(laby.width, laby.height)
    tableau = laby.tableau
    list_next_paths = find_next_path(tableau)
    grad_crea = int_to_grad_hexa(int(((tableau.shape[0] - 1) / 2) * ((tableau.shape[1] - 1) / 2)))

    # ----- Affichage de base, tout les carrés de couleur
    for lignes in tableau:
        for case in lignes:
            y_carre = case.ligne * laby.pixel_len
            x_carre = case.colone * laby.pixel_len
            if case.path:
                couleur = grad_crea[case.path.couleur - 1]
            else:
                couleur = 'black'
            canvas.create_rectangle(x_carre, y_carre, x_carre + laby.pixel_len, y_carre + laby.pixel_len,
                                    outline=couleur, fill=couleur)
    canvas.update()

    # ----- crée et fusione les chemins
    while laby.depart.path is not laby.arrive.path:
        # prend une case et ses deux voisins
        path = list_next_paths.pop()
        l = path[0]
        c = path[1]
        c0: Case = tableau[l, c]
        if path[2] == '-':
            c1: Case = tableau[l, c - 1]
            c2: Case = tableau[l, c + 1]
        else:
            c1: Case = tableau[l - 1, c]
            c2: Case = tableau[l + 1, c]
        # fusionne les chemins si non identiques
        if c1.path is not c2.path:
            if len(c1.path) > len(c2.path):
                c_win = c1
                c_loose = c2
            else:
                c_win = c2
                c_loose = c1
            c_loose.path.add_case(c0)
            # redessine par dessus le canvas pour actualiser le chemin
            for case in c_loose.path.cases:
                y_carre = case.ligne * laby.pixel_len
                x_carre = case.colone * laby.pixel_len
                couleur = grad_crea[c_win.path.couleur - 1]
                canvas.create_rectangle(x_carre, y_carre, x_carre + laby.pixel_len, y_carre + laby.pixel_len,
                                        outline=couleur, fill=couleur)
            c_win.path.fusion(c_loose.path)

        # casse le mur malgre tout pour faire un laby complexe
        elif random.random() > 0.9:
            c1.path.add_case(c0)
            couleur = grad_crea[c0.path.couleur - 1]
            y_carre = c0.ligne * laby.pixel_len
            x_carre = c0.colone * laby.pixel_len
            canvas.create_rectangle(x_carre, y_carre, x_carre + laby.pixel_len, y_carre + laby.pixel_len,
                                    outline=couleur, fill=couleur)

        sleep(0.001)
        canvas.update()

    # ----- Del les chemins non accèssibles
    for lignes in tableau:
        for case in lignes:
            if case.path and case.path is not laby.depart.path:
                case.path = None

    # ----- calcul des chemins et co
    mesure_distance(laby)
    resoudre_lab(laby)
    clean_impasses(laby)
    laby.grad_color = int_to_grad_hexa(laby.arrive.distance)

    # ----- Calcul du canvas de base
    # canvas = laby.canvas
    # canvas.update()
    # sleep(3)
    # for case in laby.depart.path.cases:
    #     y_carre = case.ligne * laby.pixel_len
    #     x_carre = case.colone * laby.pixel_len
    #     canvas.create_rectangle(x_carre, y_carre, x_carre + laby.pixel_len, y_carre + laby.pixel_len,
    #                             outline='white', fill='white')
    #     canvas.update()
