lista_numeros = list()  # ou []

print('digite 5 numeros')

for i in range(0, 5):
    numero = int(input(f'número para a posição {i}: '))
    lista_numeros.insert(i, numero)  # append

maior = max(lista_numeros)
menor = min(lista_numeros)


print(
    f'O maior valor é {maior} e está na/nas posição ', end=' ')
for i in range(0, 5):
    if lista_numeros[i] == maior:
        print(f'{i}', end='... ')

print()

print(
    f'O menor valor é {menor} e está na posição', end=' ')
for i in range(0, 5):
    if lista_numeros[i] == menor:
        print(f'{i}', end='... ')

print()
