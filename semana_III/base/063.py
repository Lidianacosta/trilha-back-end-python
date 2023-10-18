numero = int(input('digite um numero: '))
cont = 0
termo_1 = 1
termo_2 = 1
aux = 0

print(0, termo_1, termo_2, sep='->', end='->')

while cont != numero:
    aux = termo_1 + termo_2
    termo_1 = termo_2
    termo_2 = aux
    if cont == numero-1:
        print(termo_2)
    else:
        print(termo_2, end='->')
    cont += 1
