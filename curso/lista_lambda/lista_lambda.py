from copy import deepcopy

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print('ultilizado list comprehension', )
print()

nova_lista = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
]

nova_lista.sort(key=lambda item: item['nome'])

print('Lista original')
print(*produtos, sep='\n')
print()

print('Lista com o preço com 10% de aumento')
print(*nova_lista, sep='\n')
print()


print('ultilizado deepcopy')
print()

nova_lista = sorted(deepcopy(produtos), key=lambda item: item['nome'])

for produto in nova_lista:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

print('Lista original')
print(*produtos, sep='\n')
print()

print('Lista com o preço com 10% de aumento')
print(*nova_lista, sep='\n')
print()


produtos_ordenados_por_nome = deepcopy(produtos)

print('Ordenado por nome (reverse)')
produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')

print()
produtos_ordenados_por_preco = deepcopy(produtos)

print('Ordenado por preço (menor para maior)')
produtos_ordenados_por_preco.sort(key=lambda item: item['preco'])
print(*produtos_ordenados_por_preco, sep='\n')
print()
