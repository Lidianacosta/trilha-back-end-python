
SAIR = False

lista_numeros = []

print('digite valores para serem adicionados na lista')

while not SAIR:
    numero = input('digite um valor: ')
    try:
        numero = float(numero)
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
print(f'números adicionados: {lista_numeros}')
