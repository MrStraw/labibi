from numpy import ndarray

from models import Case
from steps import init_grid, create_path, mesure_distance, resoudre_lab, clean_impasses


class Labyrinthe:
    def __init__(self, width: int, height: int, pixel_len: int):
        if width < 5:
            width = 5
        elif not width % 2:
            width += 1
        if height < 5:
            height = 5
        elif not height % 2:
            height += 1

        self.width: int = width
        self.height: int = height
        self.pixel_len: int = pixel_len
        self.tableau: ndarray = init_grid(self.width, self.height)

        self.set_table(False)

    def set_table(self, reset=True):
        if reset:
            self.tableau: ndarray = init_grid(self.width, self.height)
        create_path(self)
        mesure_distance(self)
        resoudre_lab(self)
        clean_impasses(self)

    @property
    def depart(self) -> Case:
        return self.tableau[1, 0]

    @property
    def arrive(self) -> Case:
        return self.tableau[self.height - 2, self.width - 1]
