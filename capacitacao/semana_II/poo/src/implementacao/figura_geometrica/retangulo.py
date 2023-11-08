from figura_geometrica import Figura_geometrica


class Retangulo(Figura_geometrica):

    def calcula_area(self, altura, largura):
        self.area = altura * largura

    def calcula_perimetro(self, altura, largura):
        self.perimetro = 2 * (altura + largura)
