from os import system
from random import randint
from time import sleep
from operator import itemgetter

system('clear')

lista_jogadores = []
jogador = {}

for i in range(0, 4):
    jogador['nome'] = 'jogador' + str(i+1)
    jogador['valor'] = randint(1, 6)
    print(f'O {jogador["nome"]} valor o valor {jogador["valor"]}')
    lista_jogadores.append(jogador.copy())
    sleep(1)

print('-=-'*20)

ranking = sorted(lista_jogadores, key=itemgetter('valor'), reverse=True)
print('== RANKING DOS JOGADORES ==')
for pos, jogador in enumerate(ranking):
    print(f' {pos+1}º lugar {jogador["nome"]} com {jogador["valor"]}')
