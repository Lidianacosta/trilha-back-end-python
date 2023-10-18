soma = 0

for i in range(1, 501, 2):
    if not i % 3:
        print(i, end='  ')
        soma += i
print('\n')
print("A soma dos numeros inpares multiplos de 3 é: {}".format(soma))
print('\n')
print(50 * '-')
print('\n')
soma = 0
for i in range(1, 501):
    if not i % 3 and i % 2:
        print(i, end='  ')
        soma += i
print('\n')
print("A soma dos numeros inpares multiplos de 3 é: {}".format(soma))
