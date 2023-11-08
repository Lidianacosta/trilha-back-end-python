numero_1 = float(input('digite um numero: '))
numero_2 = float(input('digite outro numero: '))

if numero_1 > numero_2:
    print(f'{numero_1=} émaior que {numero_2=}')
elif numero_1 < numero_2:
    print(f'{numero_2=} émaior que {numero_1=}')
elif numero_2 == numero_1:
    print(f'{numero_1=} e {numero_2=} são iguais')
