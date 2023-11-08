
def leia_float(msn):

    try:
        valor = input(msn).replace(',', '.')
        return float(valor)
    except ValueError:
        print(f'Erro: dinheiro não aceito: {valor}')
        return leia_float('Digite apenas numeros: ')
