
from datetime import datetime

ANO_ATUAL = datetime.now().year

pessoa = {}

pessoa['nome'] = input('Nome: ')
pessoa['idade'] = ANO_ATUAL - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if pessoa['ctps']:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + \
        ((pessoa['contratação'] + 35) - ANO_ATUAL)

print('-=-'*20)

if pessoa['ctps']:
    print(f'Nome: {pessoa["nome"]}\n'
          f'idade: {pessoa["idade"]}\n'
          f'ctps: {pessoa["ctps"]}\n'
          f'contratação: {pessoa["contratação"]}\n'
          f'salário: {pessoa["salário"]}\n'
          f'aposentadoria: {pessoa["aposentadoria"]}\n'
          )
else:
    print(f'Nome: {pessoa["nome"]}\n'
          f'idade: {pessoa["idade"]}\n'
          f'Não possui carteira de trabalho\n'
          )
