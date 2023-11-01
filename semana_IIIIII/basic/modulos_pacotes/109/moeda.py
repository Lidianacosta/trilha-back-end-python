
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
