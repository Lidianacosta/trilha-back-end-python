from random import randint

lista_jokenpo = ['pedra', 'papel', 'tesoura']
numero_aleatorio = randint(0, 2)
jogada_pensada = lista_jokenpo[numero_aleatorio]

print('vamos jogar jokenpô')
jogada = input('qual sua jogada: ')

if jogada in lista_jokenpo:
    if jogada == jogada_pensada:
        print('empate')
    elif (jogada == lista_jokenpo[0] and jogada_pensada == lista_jokenpo[2]) or (jogada == lista_jokenpo[1] and jogada_pensada == lista_jokenpo[0]) or (jogada == lista_jokenpo[2] and jogada_pensada == lista_jokenpo[1]):
        print('vc ganhou')
    else:
        print('vc perdeu')
else:
    print('a jogada não existe')
