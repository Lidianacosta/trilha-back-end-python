
from os import system

pessoas = []
dados = []

maior = menor = 0

while True:
    print('digite os dados da pessoa')
    dados.append(str(input('Nome: ')).title())
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    print('Pessoa adicionada')

    resposta = input('Quer continuar adicionando? [S|N]: ')
    if resposta in 'Nn':
        break

system('clear')

print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso é {maior}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'({pessoa[0]})', end=' ')
print()

print(f'O maior peso é {menor}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'({pessoa[0]})', end=' ')
print()

print('Dados das Pessoas')
for pessoa in pessoas:
    print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]}')
