from screeninfo import get_monitors
import tkinter as tk

from models import Labyrinthe, Case
from .all_print_mode import print_mode


def screen_lab(pixel_len: int = 20):
    length = 0
    s_height = 0
    s_width = 0

    window = tk.Tk()
    window.title("auto labyrinthe")
    window.configure(background='black')

    # Recherche du plus grand écran
    for m in get_monitors():
        m_length = m.height * m.width
        if m_length > length:
            length = m_length
            s_width = m.width
            s_height = m.height
    s_height -= 60
    s_width -= 30
    window.geometry(f"{s_width}x{s_height}")

    # Création du canva
    nb_p_width = int(s_width / pixel_len)
    nb_p_height = int(s_height / pixel_len)
    c_width = nb_p_width * pixel_len + pixel_len
    c_height = nb_p_height * pixel_len + pixel_len
    canvas = tk.Canvas(window, width=c_width, height=c_height, bg='black')
    canvas.pack()

    # Création du tableau
    print(nb_p_width, nb_p_height)  # TODO
    laby = Labyrinthe(nb_p_width, nb_p_height, pixel_len, canvas)

    # Menu
    menu = tk.Menu(window)
    menu_print = tk.Menu(menu, tearoff=0)
    menu_print.add_command(label="Créer un nouveau labyrinthe", command=lambda: generate(laby, canvas))
    menu_print.add_separator()
    menu_print.add_command(label="Classique", command=lambda: print_mode(laby, 'l'))
    menu_print.add_command(label="Solution", command=lambda: print_mode(laby, 'solution'))
    menu_print.add_command(label="Voir les impasses", command=lambda: print_mode(laby, 'impasse'))
    menu_print.add_command(label="Tous les chemins", command=lambda: print_mode(laby, 'tout chemins'))
    menu_print.add_command(label="Gradiant des distances", command=lambda: print_mode(laby, 'distance'))
    menu_print.add_command(label="Tout les chemins en gradiant", command=lambda: print_mode(laby, 'grad sans impasse'))
    menu.add_cascade(label="Print mode", menu=menu_print)

    window.config(menu=menu)
    window.mainloop()


def generate(laby: Labyrinthe, canvas: tk.Canvas):
    laby.generate()
    print_mode(laby)
