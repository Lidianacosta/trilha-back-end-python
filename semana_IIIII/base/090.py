
aluno = {}

aluno['nome'] = input('digite o nome do aluno: ')
aluno['media'] = float(input('digite a média do aluno: '))
aluno['situacao'] = 'Aprovado' if aluno['media'] >= 7.0 else 'Reprovado'

print(aluno)

for key, dado in aluno.items():
    print(key, ': ', dado, sep='')
