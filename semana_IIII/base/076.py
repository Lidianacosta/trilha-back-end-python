
produtos_precos = ('lápis', 1.17,
                   'borracha', 2.00,
                   'caderno', 15.50,
                   'estojo', 25.30
                   )


print(produtos_precos)

print('-'*40)
print(f'{"Tabela de Produtos": ^37}')
print('-'*40)

for i in range(0, len(produtos_precos), 2):
    print(f'{produtos_precos[i]:.<30} R$ {produtos_precos[i+1]:>7.2f}')
