from retangulo import Retangulo
from circulo import Circulo

circulo = Circulo()
retangulo = Retangulo()

circulo.calcula_area(5)
circulo.calcula_perimetro(5)

retangulo.calcula_area(2, 5)
retangulo.calcula_perimetro(2, 5)

print(circulo.area)
print(f'{circulo.perimetro :.2f}')
print(f'{retangulo.area :.2f}')
print(retangulo.perimetro)
