numero = int(input('digite um numero inteiro: '))
base = int(input(
    'digite a base da conversão 1 - binario, 2 - octal ou 3 - hexadecimal\nbase: '
))

if base == 1:
    print(f'{numero} em binario: {bin(numero)}')
elif base == 2:
    print(f'{numero} em binario: {oct(numero)}')
elif base == 3:
    print(f'{numero} em binario: {hex(numero)}')

else:
    print('valor invalido!')
