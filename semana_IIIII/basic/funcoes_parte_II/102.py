
def fatorial(num, show=False):
    """calcula o fatorial e o exibe na tela.

    Args:
        num (int): numero que deve ser calculado o fatorial.
        show (bool, optional): mostra o processo do calculo do fatorial
        quando for true. Defaults to False.
    """

    fat = 1

    if show:
        c = 'x'
        for i in range(num, 0, -1):
            if i == 1:
                c = '='
            print(i, c, end=' ')
            fat *= i
        print(f'{fat}')
    else:
        for i in range(num, 0, -1):
            fat *= i
        print(f'{fat}')


fatorial(5, True)
help(fatorial)
