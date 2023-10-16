class Jogador:
    def __init__(self, nome, idade):
        self._nome = nome.title()
        self._idade = idade

    @property
    def nome(self):
        self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @nome.getter
    def nome(self):
        return self._nome

    @property
    def idade(self):
        self._idade

    @idade.setter
    def idade(self, idade):
        if idade > 0:
            self._idade = idade

    @idade.getter
    def idade(self):
        return self._idade
