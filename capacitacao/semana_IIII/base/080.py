
lista_numeros = []

print('digite 5 números')

for i in range(1, 6):
    numero = int(input(f'digite {i}º número: '))
    if not lista_numeros or numero >= lista_numeros[-1]:
        lista_numeros.append(numero)
    else:
        for i, n in enumerate(lista_numeros):
            if numero <= n:
                lista_numeros.insert(i, numero)
                break
    print(f'o numero foi adicionado na posição {lista_numeros.index(numero)}')

print(f'lista: {lista_numeros}')
