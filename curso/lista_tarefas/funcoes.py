import json
from os import system


def desfazer(t, r):
    if not t:
        print('Nada a desfazer')
        return

    r.append(t.pop())


def refazer(lista, ref):
    if not ref:
        print('Nada a refazer')
        return

    lista.append(ref.pop())


def listar(lista):
    if not lista:
        print('A lista está vazia')
        return

    print()
    print('Tarefas:')
    for item in lista:
        print(' - '+item)

    print()


def adicionar(tarefa, lista):
    if not tarefa.strip():
        print('voce não digitou nada')
        return

    lista.append(tarefa)
    listar(lista)


def limpar_terminal():
    system('clear')


def ler_lista(caminho):
    lista = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            lista = json.load(arquivo)
    except FileNotFoundError:
        gravar_lista(lista, caminho)

    return lista


def gravar_lista(lista, caminho):

    with open(caminho, 'w', encoding='utf8',) as arquivo:
        json.dump(lista, arquivo, indent=2, ensure_ascii=False)
