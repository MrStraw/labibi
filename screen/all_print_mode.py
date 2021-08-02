from tkinter import Canvas

from numpy import ndarray

from models import Labyrinthe


def print_mode(laby: Labyrinthe, canvas: Canvas, mode: str = 'lab'):
    pixel_len = laby.pixel_len
    for lignes in laby.tableau:
        for case in lignes:
            y_carre = case.ligne * pixel_len
            x_carre = case.colone * pixel_len
            couleur = ''
            if not case.path:
                couleur = 'black'
            elif case is laby.depart or case is laby.arrive:
                couleur = 'red'
            else:
                if mode == 'lab' or mode == '':
                    couleur = 'white'
                elif mode == 'solution':
                    if case.solution == 1:
                        couleur = 'green'
                    else:
                        couleur = 'white'
                elif mode == 'impasse':
                    if case.full_path:
                        couleur = 'white'
                    else:
                        couleur = 'grey'
                elif mode == 'tout chemins':
                    if case.solution == 1:
                        couleur = 'green'
                    elif case.full_path:
                        couleur = 'white'
                    else:
                        couleur = 'grey'

            canvas.create_rectangle(x_carre, y_carre, x_carre + pixel_len, y_carre + pixel_len,
                                    outline=couleur, fill=couleur)
    return canvas
