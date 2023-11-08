
from time import sleep


def contador(ini: int, fim: int, passo: int):
    print('-=-'*15)
    print(f'Contagem de {ini} até {fim} em {passo}' if passo > 0
          else f'Contagem de {ini} até {fim} em {passo*-1}'
          )

    if passo == 0:
        passo = 1

    if ini > fim and passo > 0:
        passo *= -1
        fim += -1
    elif passo < 0:
        fim += -1
    else:
        fim += 1

    for i in range(ini, fim, passo):
        print(i, end=' ')
        sleep(0.5)
    print('Fim!')
    sleep(0.5)


contador(1, 10, 1)
contador(10, 0, 2)

print('-=-'*20)
print('digite os intevalos e o passo')
inicio = int(input('inicio:'))
f = int(input('fim:'))
pas = int(input('passo:'))

contador(inicio, f, pas)
print()
