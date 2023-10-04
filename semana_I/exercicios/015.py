dias = float(input('Quantos dias com o carro? '))

km = float(input('Quantos km rodados? '))

print('total a ser pago: R$ {:0.2f}'.format(dias * 60 + km * 0.15))
