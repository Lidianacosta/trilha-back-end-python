# from modelo import IdadeError
from modelo import arquivo, dados

lista_pessoas = arquivo.ler()


while True:

    dados.menu()
    escolha = dados.ler_int('opção: ')

    if escolha == 1:
        dados.listar_pessoas(lista_pessoas)
    elif escolha == 2:
        lista_pessoas.append(dados.cadastrar())
    elif escolha == 3:
        arquivo.gravar(lista_pessoas)
        break
    else:
        print('escolha inválida')
