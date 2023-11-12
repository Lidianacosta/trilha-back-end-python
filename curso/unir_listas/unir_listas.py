# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest


def unir_listas(lista1, lista2):

    if len(lista1) < len(lista2):
        nova_lista = [(item, lista2[pos]) for pos, item in enumerate(lista1)]
    else:
        nova_lista = [(item, lista1[pos]) for pos, item in enumerate(lista2)]

    return nova_lista


lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estados = ['BA', 'SP', 'MG', 'RJ']

print(unir_listas(lista_cidades, lista_estados))
print(list(zip(lista_cidades, lista_estados)))
print(list(zip_longest(lista_cidades, lista_estados, fillvalue="sem cidade")))

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

soma_listas = [(x + y) for x, y in zip(l1, l2)]
print(soma_listas)  # [2, 4, 6, 8]

soma_listas = [(x + y) for x, y in zip_longest(l1, l2, fillvalue=0)]
print(soma_listas)  # [2, 4, 6, 8, 5, 6, 7]
