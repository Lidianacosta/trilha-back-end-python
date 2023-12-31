from programa import Programa


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return (f'{self.__class__.__name__}: {self.nome}, '
                f'Duração: {self.duracao}, '
                f'Ano: {self.ano}, '
                f'Likes: {self.likes}'
                )
