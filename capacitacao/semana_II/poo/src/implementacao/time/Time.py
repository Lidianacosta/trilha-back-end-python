class Time:
    def __init__(self, nome):
        self.__nome = nome.title()
        self.lista_jogadores = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @nome.getter
    def nome(self):
        return self.__nome

    def inserir_jogador(self, jogador):
        self.lista_jogadores.append(jogador)

    def listar_jogadores(self):
        for jogador in self.lista_jogadores:
            print(f'nome:{jogador.nome}, idade: {jogador.idade}')
