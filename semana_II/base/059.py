numero_1 = float(input('digite um  numero: '))
numero_2 = float(input('digite outro numero: '))

sair = False

while not sair:

    print('''
  [1]- somar
  [2]- multiplicar
  [3]- maior
  [4]- novos numeros
  [5]- sair do programa
  ''')

    escolha = int(input('digite um opção: '))
    print()

    if escolha == 1:
        print(f'a soma é {numero_1 + numero_2}', end='\n')
    elif escolha == 2:
        print(f'a multiplicação  é {numero_1 * numero_2}')
    elif escolha == 3:
        print(f'{numero_1} é maior'
              if numero_1 > numero_2 else f'{numero_2} é maior')
    elif escolha == 4:
        numero_1 = float(input('digite um  numero: '))
        numero_2 = float(input('digite outro numero: '))
    elif escolha == 5:
        sair = True
    else:
        print('opção invalida')

print('programa finalizado', )
