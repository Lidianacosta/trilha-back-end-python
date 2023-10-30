from random import randint


def sorteia_numeros() -> list:
    numeros = []
    cont = 0
    while cont != 5:
        numeros.append(randint(1, 10))
        cont += 1

    print('Os numeros sorteados foram: ', end='')
    print(*numeros, sep=', ', end='.\n')
    return numeros


def soma_par(num) -> None:
    soma = 0
    for i in num:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos numeros pares é {soma}')


n = sorteia_numeros()
soma_par(n)
