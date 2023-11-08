
def exibe_placar(nome='<Desconhecido>', gols=0):

    print(f'O jogador {nome} fez {gols} gols.')


jogador = {}

n = input('nome: ')
g = input('gols: ')

if n == '':
    if g.isdigit():
        exibe_placar(gols=g)
    else:
        exibe_placar()
else:
    if g.isdigit():
        exibe_placar(n, g)
    else:
        exibe_placar(n)
