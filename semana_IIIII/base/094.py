
pessoa = dict()
pessoas = list()
mulheres = []
media_idade = 0

while True:
    pessoa['nome'] = input('Nome: ').title()
    pessoa['sexo'] = input('Sexo: [F|M] ').upper()
    pessoa['idade'] = int(input('Idade: '))

    media_idade += pessoa['idade']

    pessoas.append(pessoa.copy())
    pessoa.clear()

    sair = input('deseja continuar? [S|N] ').upper()

    if sair != 'S':
        break

media_idade /= len(pessoas)

print('-=-'*20)

print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média das idades é de {media_idade:.2f} anos.')

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

print('- As mulheres cadastradas foram:', end=' ')
print(*mulheres, sep=', ', end='.\n')

print('- Lista das pessoas que estão acima da média: ')

for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        print(
            f'\nNome: {pessoa["nome"]}; '
            f'Sexo: {pessoa["sexo"]}; '
            f'Idade: {pessoa["idade"]};'
        )
