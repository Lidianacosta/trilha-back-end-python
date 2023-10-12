# crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostro quantos dólares ela pode comprar
# 1 real brasileiro é igual a 0,20 dólares
# 1 dollar é igual a 5,04 reais brasileiros
# 1 euro é igual a 5,34 reais brasileiros


dinheiro = float(input('informe seu saldo em reais: R$ '))

print("com R$ {:0.2f} reais você pode comprar R$ {:0.2f} dólares "
      .format(dinheiro, dinheiro/5.04))
print("com R$ {:0.2f} reais você pode comprar R$ {:0.2f} euro "
      .format(dinheiro, dinheiro/5.34))
