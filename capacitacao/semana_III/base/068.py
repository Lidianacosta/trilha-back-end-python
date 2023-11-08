from random import randint

jogada_pensada = randint(0, 10)

vitorias = 0

while True:

    escolha = input('escolha par ou impar: ')
    jogada = int(input('faça sua jogada: '))

    verifica = (jogada + jogada_pensada) / 2

    if escolha == 'impar' and verifica != 0:
        vitorias += 1
        print('você ganhou')
    elif escolha == 'par' and verifica == 0:
        print('você ganhou')
        vitorias += 1
    else:
        print(f'{jogada} + {jogada_pensada} = {jogada_pensada + jogada}')
        print(f'você perdeu e teve um total de {vitorias} vitórias')

        break
