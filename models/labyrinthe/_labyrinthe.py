import tkinter as tk
from numpy import zeros

from models import Case
from .generate import generate


class Labyrinthe:
    def __init__(self, width: int, height: int, pixel_len: int, canvas: tk.Canvas):
        if width < 5 or height < 5:
            raise Exception('Tableau trop petit')
        elif not width % 2:
            width += 1
        elif not height % 2:
            height += 1

        self.grad_color = []
        self.width: int = width
        self.height: int = height
        self.pixel_len: int = pixel_len
        self.canvas = canvas
        self.tableau = zeros((height, width))

    def generate(self):
        generate(self)

    @property
    def depart(self) -> Case:
        return self.tableau[1, 0]

    @property
    def arrive(self) -> Case:
        return self.tableau[self.height - 2, self.width - 1]

    @property
    def cases(self):
        cases = []
        for lignes in self.tableau:
            for case in lignes:
                cases.append(case)
        return cases
