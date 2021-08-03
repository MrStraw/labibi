class Path:

    def __init__(self, couleur: int):
        self.couleur = couleur
        self.__cases = []
        self.__lenght = 0

    def __len__(self):
        return self.__lenght

    def add_case(self, case):
        self.__cases.append(case)
        self.__lenght += 1
        case.path = self

    @property
    def cases(self):
        return self.__cases

    def fusion(self, other):
        for case in other.cases:
            case.path = self
            self.__cases.append(case)
        self.__lenght += other.__lenght
        del other
