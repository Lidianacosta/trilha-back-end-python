
def maior(*num):
    maior_numero = 0

    for i in num:
        if i > maior_numero:
            maior_numero = i
    print('-=-'*20)
    print('Analizando os valores passados...')
    print(*num, sep=", ", end='. ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior_numero}.')


maior(1, 2, 3, 4, 5)
