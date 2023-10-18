from random import randint

tupla = randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10)

print(f'números sorteados: {tupla}')
print(f'maior valor presente: {max(tupla)}')
print(f'menor valor presente: {min(tupla)}')
