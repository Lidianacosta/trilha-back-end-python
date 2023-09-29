nome = input('Qual é seu nome? ')
print("Oi {:20}!".format(nome))
print("Oi {:>20}!".format(nome))
print("Oi {:<20}!".format(nome))  # faz o mesmo efeito do primeiro
print("Oi {:^20}!".format(nome))
print("Oi {:=^20}!".format(nome))


n1 = int(input('Diga um valor: '))
n2 = int(input('Diga outro valor: '))

print('''A soma é {}, o produto é {} e a divião é {:.3f},
a divisão inteira = {}, resto da divisão = {} e a pontecia = {}
'''.format(n1+n2, n1*n2, n1/n2, n1//n2, n1 % n2, n1**n2))
