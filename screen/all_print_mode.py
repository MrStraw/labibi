from tkinter import Canvas

from models import Labyrinthe


def print_mode(laby: Labyrinthe, mode: str = ''):
    canvas = laby.canvas
    grad = laby.grad_color

    canvas.delete()
    for case in laby.cases:
        y_carre = case.ligne * laby.pixel_len
        x_carre = case.colone * laby.pixel_len
        couleur = 'white' if case.path else 'black'
        canvas.create_rectangle(x_carre, y_carre, x_carre + laby.pixel_len, y_carre + laby.pixel_len,
                                outline='', fill=couleur)

    for case in laby.depart.path.cases:
        couleur = 'white'
        y_carre = case.ligne * laby.pixel_len
        x_carre = case.colone * laby.pixel_len

        if mode == 'solution':
            if case.solution == 1:
                couleur = grad[case.distance - 1]

        elif mode == 'impasse':
            if not case.full_path:
                couleur = 'grey'

        elif mode == 'tout chemins':
            if case.solution == 1:
                couleur = grad[case.distance - 1]
            elif not case.full_path:
                couleur = 'grey'

        elif mode == 'distance':
            if case.distance:
                couleur = grad[case.distance - 1]

        elif mode == 'grad sans impasse':
            if case.full_path and case.distance:
                couleur = grad[case.distance - 1]

        canvas.create_rectangle(x_carre, y_carre, x_carre + laby.pixel_len, y_carre + laby.pixel_len,
                                outline='', fill=couleur)
    canvas.update()
