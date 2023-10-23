matrix = []

temp = []

for i in range(0, 3):
    temp.append(int(input(f'digite um valor para[{i}, {0}]: ')))
    temp.append(int(input(f'digite um valor para[{i}, {1}]: ')))
    temp.append(int(input(f'digite um valor para[{i}, {2}]: ')))

    matrix.append(temp[:])
    temp.clear()

del temp

print('\n', '-='*20, end='\n\n')

for linha in matrix:
    print(f'[ {linha[0]} ] [ {linha[1]} ] [ {linha[2]} ]')
