
SAIR = False

lista_numeros = []

print('digite valores para serem adicionados na lista')

while not SAIR:
    numero = int(input('digite um valor: '))

    lista_numeros.append(numero)
    print('número adicionado a lista')

    escolha = input('Quer continuar adicionando? [S|N]: ')
    if escolha.upper() == 'S':
        SAIR = False
    else:
        SAIR = True

lista_numeros.sort(reverse=True)
print(f'foi adicionado {len(lista_numeros)} números')
print(f'números adicionados: {lista_numeros}')
print('O números 5 está na lista' if 5 in lista_numeros
      else 'O numero 5 não está na lista')
