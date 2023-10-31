
def leia_int(msn):

    try:
        return int(input(msn))
    except ValueError as error:
        print(error)
        return leia_int('Digite apenas numeros: ')


print('Voce digitou o numero:', leia_int('digite um numero inteiro: '))
