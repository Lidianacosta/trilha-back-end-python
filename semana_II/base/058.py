from random import randint

sair = False
palpites = 0

while not sair:
    palpites += 1
    numero_aleatorio = randint(0, 10)

    numero_jogador = int(input('tente adivinha o numero entre 0 e 5: '))

    if (numero_aleatorio == numero_jogador):
        print('vc venceu!\\n')
        sair = True
    else:
        print(f'vc perdeu!\nO numero pensado foi: {numero_aleatorio}\n')

print('foram nessesarios {} para vc acertar!'.format(palpites))
