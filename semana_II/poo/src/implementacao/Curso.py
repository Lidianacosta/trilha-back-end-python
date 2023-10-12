class Curso:
    def __init__(self, nome):
        self.__nome = nome
        self.lista_alunos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @nome.getter
    def nome(self):
        return self._nome
