class Disciplina:
    def __init__(self, nome):
        self.__nome = nome
        self.__professor = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @nome.getter
    def nome(self):
        return self._nome

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, p):
        self._professor = p

    @professor.getter
    def professor(self):
        return self._professor
