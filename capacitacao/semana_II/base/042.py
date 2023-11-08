lado_1 = int(input('qual o comprimento do lado?: '))
lado_2 = int(input('qual o comprimento do lado?: '))
lado_3 = int(input('qual o comprimento do lado?: '))

if (abs(lado_2 - lado_3) < lado_1 and lado_1 < (lado_2 + lado_3)) or (abs(lado_1 - lado_3) < lado_2 and lado_2 < (lado_1 + lado_3)) or (abs(lado_2 - lado_1) < lado_3 and lado_3 < (lado_2 + lado_1)):
    if lado_3 == lado_1 and lado_1 == lado_2:
        print(
            f'o triangulo formado pelos lados{lado_1, lado_2, lado_3} é equilatero')
    elif lado_2 == lado_1 or lado_1 == lado_3 or lado_3 == lado_2:
        print(
            f'o triangulo formado pelos lados{lado_1, lado_2, lado_3} é isóciles')
    else:
        print(
            f'o triangulo formado pelos lados{lado_1, lado_2, lado_3} é escaleno')

else:
    print(f'os lados{lado_1, lado_2, lado_3} não formam um triangulo')
