
alunos = []
dados = []
notas = []


while True:
    print('digite os dados do Aluno')
    dados.append(str(input('Nome: ')).title())
    notas.append(float(input('nota 01: ')))
    notas.append(float(input('nota 02: ')))

    media = (notas[0] + notas[1])/2
    dados.append(notas[:])
    dados.append(media)
    alunos.append(dados[:])
    notas.clear()
    dados.clear()
    print('Aluno cadastrado')

    resposta = input('Quer continuar adicionando? [S|N]: ')
    if resposta in 'Nn':
        break

del dados
del notas

print('-=-'*20)

print(f'{"pos":<6}{"Nome":<20}{"Média":>10}')
print('-'*40)

for pos, aluno in enumerate(alunos):

    print(f'{pos:<6}{aluno[0]:<20}{aluno[2]:>8.1f}')


while True:
    print('='*40)
    try:
        pos = int(input(
            'digite  o posição do Aluno que deseja mostra as notas '
            'ou sair [S]: '
        ))

        print(f'Aluno/a: {alunos[pos][0]}\nNotas: {alunos[pos][1]}')

    except ValueError:
        print('Exercução finalizada')
        break
    except IndexError:
        print('Não tem nenhun aluno nesta posição')
