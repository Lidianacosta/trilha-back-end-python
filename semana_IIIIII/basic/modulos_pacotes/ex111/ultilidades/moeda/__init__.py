
def aumentar(m, por, formatar=False):
    res = m * (1 + por/100)
    return res if not formatar else moeda(res)


def diminuir(m, por, formatar=False):
    res = m * (1 - por/100)
    return res if not formatar else moeda(res)


def dobro(m, formatar=False):
    res = m*2
    return res if not formatar else moeda(res)


def metade(m, formatar=False):
    res = m / 2
    return res if not formatar else moeda(res)


def moeda(m, formato='R$'):
    return f'{formato} {m:.2f}'.replace('.', ',')


def resumo(m, a, d):
    print('='*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('='*35)
    print(f'{"  Valor analisado:":<20} {moeda(m):<10}')
    print(f'{"  Dobro do valor:":<20} {dobro(m, True):<10}')
    print(f'{"  Metade do valor:":<20} {metade(m, True):<10}')
    print(f'{f"  {a}% de aumento:":<20} {aumentar(m, a, True):<10}')
    print(f'{f"  {d}% de redução:":<20} {diminuir(m, d, True):<10}')

    print('='*35)


def leia_float(msn):

    try:
        return float(input(msn))
    except ValueError as error:
        print(error)
        return leia_float('Digite apenas numeros: ')
