print('digite 4 números interios')
numero_1 = int(input('primeiro número:'))
numero_2 = int(input('segundo número:'))
numero_3 = int(input('primeiro número:'))
numero_4 = int(input('primeiro número:'))

numeros = numero_1, numero_2, numero_3, numero_4

print(numeros)


pares = 0

for numero in numeros:
    if not numero % 2:
        pares += 1


print(f'o valor 9 foi digitado {numeros.count(9)} vezes')
print(
    f'o primeiro número 3 foi digitado na posição {numeros.index(3)}'
    if 3 in numeros else 'não foi digitado nenhum número 3')
print(f'Dos 4 números digitados {pares} são pares')
