class Programa:

    lista = []

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @nome.getter
    def nome(self):
        return self._nome

    @classmethod
    def adicionar_programa_a_lista(cls, programa):
        cls.lista.append(programa)

    @classmethod
    def listar_programas(cls):
        for programa in cls.lista:
            print(f'{programa.__class__.__name__} : {programa.nome}')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} : {self.nome}'
