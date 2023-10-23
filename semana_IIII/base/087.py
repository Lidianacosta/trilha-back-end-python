matrix = []

temp = []

for i in range(0, 3):
    temp.append(int(input(f'digite um valor para[{i}, {0}]: ')))
    temp.append(int(input(f'digite um valor para[{i}, {1}]: ')))
    temp.append(int(input(f'digite um valor para[{i}, {2}]: ')))

    matrix.append(temp[:])
    temp.clear()

del temp

pares = 0

for linha in matrix:
    for numero in linha:
        if numero % 2 == 0:
            pares += numero

soma_terceira_coluna = 0

for linha in matrix:
    soma_terceira_coluna += linha[2]

maior_segunda_linha = 0

for numero in matrix[1]:
    if numero > maior_segunda_linha:
        maior_segunda_linha = numero

print('-='*20)
for linha in matrix:
    print(f'[ {linha[0]} ] [ {linha[1]} ] [ {linha[2]} ]')

print('-='*20)

print(f'A soma de todos os pares: {pares}')
print(f'A soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha: {maior_segunda_linha}')
