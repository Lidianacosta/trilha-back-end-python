class Funcionario:
    def __init__(self, nome=None, salario=0.0, cargo=None):
        self._nome = nome
        self._salario = salario
        self._cargo = cargo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @nome.getter
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        self._salario = valor

    @salario.getter
    def salario(self):
        return self._salario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @cargo.getter
    def cargo(self):
        return self._cargo
