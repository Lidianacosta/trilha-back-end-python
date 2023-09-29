# tipos primitivos

# exercicial da aula 4
n1 = int(input('digite um numero: '))
n2 = int(input('digite mais um nmero: '))
s = n1 + n2
print('A soma vale', s)
print('A soma vale {}'.format(s))

n1 = input('digite um valor: ')
print(type(n1))

n2 = int(input('digite um valor: '))
print(type(n2))


n1 = int(input('digite um numero: '))
n2 = int(input('digite mais um nmero: '))
print('a soma de {} + {} = {}'.format(n1, n2, n1+n2))

n = bool(input('digite um numero: '))
print(n)  # se tiver algo dentro retorna true se nao false

n = input('digite algo: ')
print(n.isalnum())
