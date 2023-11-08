class Empresa:
    def __init__(self, nome):
        self._nome = nome.title()
        self._funcionarios = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @nome.getter
    def nome(self):
        return self._nome

    def cadastrar_funcionario(self, funcionario):
        self._funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self._funcionarios:
            print(
                f'nome:{funcionario.nome}, '
                f'cargo: {funcionario.cargo}, '
                f'salario: {funcionario.salario}'
            )
