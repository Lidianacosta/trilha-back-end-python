
jogador = {}
gols_nas_partidas = []

jogador['nome'] = input('digite o nome: ')

jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

total_gols = 0

for i in range(0, jogos):
    gols = int(input(f'Quantos gols fez na partida {i +1}? '))
    total_gols += gols
    gols_nas_partidas.append(gols)

jogador['gols'] = gols_nas_partidas[:]
jogador['total de gols'] = total_gols
print('-=-'*20)
print(jogador)
print('-=-'*20)
for key, item in jogador.items():
    print(f'{key}: {item}')
print('-=-'*20)

print(f'{"Placar de gols":=^40}')
print(f'O/A jogador/jogadora {jogador["nome"]} jogou {jogos} partidas.')

for pos, gols in enumerate(jogador['gols']):
    print(f'{f"=>Na partida {pos+1}, fez {gols} gols.": ^40}')

print(f'Foi um total de {jogador["total de gols"]} gols.')
