
SAIR = False

lista_numeros = []
numeros_pares = []
numeros_impares = []

print('digite valores para serem adicionados na lista')

while not SAIR:
    numero = input('digite um valor: ')
    try:
        numero = int(numero)
        if numero not in lista_numeros:
            lista_numeros.append(numero)
            print('número adicionado a lista')
        else:
            print('O número já está na lista')

    except ValueError:
        print('a lista só aceita números')

    finally:
        escolha = input('Quer continuar adicionando? [S|N]: ')
        if escolha.upper() == 'S':
            SAIR = False
        else:
            SAIR = True

lista_numeros.sort()

for numero in lista_numeros:
    if not numero % 2:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)


print(f'números adicionados: {lista_numeros}')
print(f'números pares: {numeros_pares}')
print(f'números ímpares: {numeros_impares}')
