
jogador = {}
lista_jogadores = []
gols_nas_partidas = []

while True:
    print('-'*60)
    jogador['nome'] = input('digite o nome: ').title()

    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    total_gols = 0

    for i in range(0, jogos):
        gols = int(input(f'Quantos gols fez na partida {i +1}? '))
        total_gols += gols
        gols_nas_partidas.append(gols)

    jogador['gols'] = gols_nas_partidas[:]
    jogador['total de gols'] = total_gols
    lista_jogadores.append(jogador.copy())
    jogador.clear()
    gols_nas_partidas.clear()

    sair = input('Quer continuar adicionando jogadores? [S|N] ').upper()

    if sair != 'S':
        break

print('-=-'*20)

print(f'{"Placar de gols":=^60}')
print(f'{"Cod":<5} {"Nome":<25} {"Gols":<20} {"Total":<10}')
print('-'*60)
for key, item in enumerate(lista_jogadores):
    print(
        f'{key:<5}',
        f'{item["nome"]:<25}',
        f'{str(item["gols"]):<20}',
        f'{item["total de gols"]:<10}'
    )

print('='*60)
while True:
    print('-'*60)

    try:
        escolha = input(
            'Deseja mostra os dado de Algum jogador diga o código dele '
            'ou [S] para sair: '
        )

        if escolha in 'sS':
            print('Programa encerrado')
            break

        cod = int(escolha)
        jogador = lista_jogadores[cod].copy()

        print(F'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for partida, gols in enumerate(jogador['gols']):
            print(f'   No jogo {partida+1} fez {gols} gol/gols.')

    except ValueError:
        print('Código invalido')
    except IndexError:
        print('O jogado não existe')
