from models.path import Path


class Case:

    def __init__(self, ligne: int, colone: int, tableau, path: Path = None):
        self.__loc: (int, int) = (ligne, colone)
        self.path: Path = path
        self._is_depart_or_arrive: int = 2
        self.distance: int = 0
        self.solution: int = 0
        self.full_path: bool = False
        self.tableau = tableau

    def __repr__(self):
        if not self.couleur:
            return '++'
        if self.couleur < 10:
            return '0' + str(self.couleur)
        return str(self.couleur)

    def __str__(self):
        if self.is_depart:
            s2 = '  depart = True\n'
        elif self.is_arrive:
            s2 = '  arrive = True\n'
        else:
            s2 = '\n'
        s = f"Case :\n" \
            f"  position: {self.ligne}, {self.colone}\n" \
            f"  couleur: {self.couleur}\n" \
            f"  solution: {self.solution}\n" \
            f"  distance: {self.distance}\n" + s2 + '\n'
        return s

    @property
    def ligne(self):
        return self.__loc[0]

    @property
    def colone(self):
        return self.__loc[1]

    @property
    def loc(self):
        return self.__loc

    @property
    def couleur(self):
        if self.path:
            return self.path.couleur
        return 0

    @property
    def is_depart(self):
        if not self._is_depart_or_arrive:
            return True
        return False

    @is_depart.setter
    def is_depart(self, value: bool):
        if value:
            self._is_depart_or_arrive = 0
        else:
            self._is_depart_or_arrive = 2

    @property
    def is_arrive(self):
        if self._is_depart_or_arrive == 1:
            return True
        return False

    @is_arrive.setter
    def is_arrive(self, value: bool):
        if value:
            self._is_depart_or_arrive = 1
        else:
            self._is_depart_or_arrive = 2

    @property
    def voisins(self):
        tuples = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        voisins = []
        for t in tuples:
            try:
                case_voisine: Case = self.tableau[t[0] + self.ligne, t[1] + self.colone]
            except IndexError:
                continue
            voisins.append(case_voisine)
        return voisins
