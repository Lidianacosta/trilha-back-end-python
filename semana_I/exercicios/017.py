from math import pow

a = float(input('digite o cateto adjacente: '))
b = float(input('digite o cateto oposto: '))

print('A hipotenusa é {}'.format((pow(a, 2) + pow(b, 2))/2))
