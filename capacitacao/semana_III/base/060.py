numero = int(input('digite um numero: '))

fat = 1
cont = numero
print(f'{numero}! = ', end='')
while cont != 1:
    print(f'{cont}x', end='')
    fat *= cont
    cont -= 1
print('1 =', fat)
