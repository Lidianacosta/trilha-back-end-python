# def soma(x):
#   def interna(y):
#     return x + y
#   return interna

# def multiplica(x):
#   def interna(y):
#     return x * y
#   return interna


def soma(x):
    return lambda y: x + y


def multiplica(x):
    return lambda y: x * y


def cria_funcao(funcao, *args):
    return funcao(*args)


multiplica_por_10 = cria_funcao(multiplica, 10)
soma_por_5 = cria_funcao(soma, 5)

print('range de 1 a 10 multiplicados por 10')
for i in range(1, 11):
    print(multiplica_por_10(i), end=' ')

print()

print('range de 1 a 10 somados com 5')
for i in range(1, 11):
    print(soma_por_5(i), end=' ')

print()
