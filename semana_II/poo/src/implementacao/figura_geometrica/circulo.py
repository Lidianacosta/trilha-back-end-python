from figura_geometrica import Figura_geometrica


class Circulo(Figura_geometrica):

    def calcula_area(self, raio):
        self.area = raio**2 * 3.14

    def calcula_perimetro(self, raio):
        self.perimetro = raio*2*3.14
