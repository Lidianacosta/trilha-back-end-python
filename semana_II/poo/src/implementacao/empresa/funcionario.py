class Funcionario:
    def __init__(self, nome, salario, cargo):
        self._nome = nome.title()
        self.salario = salario
        self.cargo = cargo.title()

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
    def salario(self):
        self._salario

    @salario.setter
    def salario(self, salario):
        if salario > 0:
            self._salario = salario

    @salario.getter
    def salario(self):
        return self._salario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo.title()

    @cargo.getter
    def cargo(self):
        return self._cargo
