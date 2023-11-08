preco = float(input('qual o preço do produto? R$ '))

print(
    'o produto custava R$ {:0.2f}, com o desconto de 5% vai sair por R$ {:0.2f}'
    .format(preco, preco * 0.95))
