pessoa_mais_velha_nome = ""
idade_homem_mais_velha = 0
soma_idade = 0
mulheres_acima_20 = 0

for i in range(1, 2):
    print('pessoa N° {}'.format(i))
    nome = input('digite seu nome: ')
    idade = int(input('digite sua idade: '))
    sexo = input('digite seu sexo f ou m: ')

    soma_idade += idade
    if sexo == "f" and idade < 20:
        mulheres_acima_20 + 1
    if idade > idade_homem_mais_velha and sexo == 'm':
        pessoa_mais_velha_nome = nome

print(f'A media das idades é {soma_idade/4}\n',
      f'O homem mais velho é {pessoa_mais_velha_nome}\n'if idade_homem_mais_velha else 'não foi lido o nome de nenhum homem\n'
      f'Tem {mulheres_acima_20} mulheres abaixo dos 20 anos\n'
      )
