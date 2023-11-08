
def aumentar(m, por):
    return m * (1 + por/100)


def diminuir(m, por):
    return m * (1 - por/100)


def dobro(m):
    return m*2


def metade(m):
    return m / 2


def moeda(m, formato='R$'):
    return f'{formato} {m:.2f}'.replace('.', ',')
