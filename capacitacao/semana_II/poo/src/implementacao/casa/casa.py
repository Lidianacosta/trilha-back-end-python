from banheiro import Banheiro
from quarto import Quarto
from cozinha import Cozinha


class Casa:
    def __init__(self, proprietario):
        self._proprietario = proprietario
        self.banheiro = Banheiro()
        self.cozinha = Cozinha()
        self.quarto = Quarto()

    @property
    def proprietario(self):
        return self._proprietario

    @proprietario.setter
    def proprietario(self, proprietario):
        self._proprietario = proprietario

    @proprietario.getter
    def proprietario(self):
        return self._proprietario
