termo = int(input('digite o primeiro termo da PA: '))
razao = int(input('digite a razão: '))

for i in range(1, 11):
    print(f'A{i}:', termo)
    termo += razao
print('\n')
