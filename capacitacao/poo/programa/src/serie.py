from programa import Programa


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return (f'{self.__class__.__name__}: {self.nome}, '
                f'Temporadas: {self.temporadas}, '
                f'Ano: {self.ano}, '
                f'Likes: {self.likes}'
                )
