class Path:

    def __init__(self, couleur: int):
        self.couleur = couleur
        self.__cases = []

    def add_case(self, case):
        self.__cases.append(case)
        case.path = self

    @property
    def cases(self):
        return self.__cases

    def fusion(self, other):
        for case in other.cases:
            case.path = self
            self.__cases.append(case)
        del other
