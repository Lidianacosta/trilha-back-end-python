# escreva um programa que receba um valor em metros
# e o exiba convertido em centímetros e milimetros

cm = 100
mm = 1000
dam = 0.1
hm = 0.01
km = 0.001

v = float(input('digite um numero para fazer a conversão: '))

print('''o valor em metro é {}, em centímetro {} e em milimetro {},
{}dam
{}hm
{}km
'''.format(v, v*cm, v*mm, v*dam, v*hm, v*km))
