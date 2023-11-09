
def duplicatas(lista):

    qtd_repeticoes = len(lista) - len(set(lista))

    if not qtd_repeticoes:
        return 0, None

    conjunto = set()

    for pos, item in enumerate(lista):
        conjunto.add(item)

        if len(conjunto) != pos + 1:
            return qtd_repeticoes, item


lista_de_listas_de_items = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    ['ana', 'lidiana', 'luiz', 'ana', 'julia'],
    ['lidiana', 'luiz', 'ana', 'julia'],
]


for lista_items in lista_de_listas_de_items:

    repeticoes, primeiro_repetido = duplicatas(lista_items)

    if primeiro_repetido is not None:
        print(
            f'Lista: {lista_items}',
            f'Repetições: {repeticoes}',
            f'Primeiro item repetido: {primeiro_repetido}',
            sep='\n'
        )
    else:
        print(f'Lista: {lista_items}\nRepetições: {repeticoes}', sep='\n')

    print()
