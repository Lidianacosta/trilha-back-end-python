expressao = input('digite uma expressão: ')

if expressao.count('(') == expressao.count(')'):
    print('expressão válida')
else:
    print('expressão inválida')
