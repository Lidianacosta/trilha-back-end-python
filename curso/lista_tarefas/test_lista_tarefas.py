# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

from funcoes import adicionar, desfazer, gravar_lista, \
    ler_lista, listar, refazer, limpar_terminal


CAMINHO = 'curso/lista_tarefas/' + 'lista_tarefas.json'

lista_tarefas = ler_lista(CAMINHO)
lista_refazer = []

comandos = {
    'listar': lambda: listar(lista_tarefas),
    'desfazer': lambda: desfazer(lista_tarefas, lista_refazer),
    'refazer': lambda: refazer(lista_tarefas, lista_refazer),
    'clear': limpar_terminal
}

while True:
    print('comandos: listar, refazer, desfazer, sair.')
    escolha = input('Digite uma tarefa ou comando: ').lower()

    if escolha == 'sair':
        break

    if escolha in comandos:
        comandos.get(escolha)()
    else:
        adicionar(escolha, lista_tarefas)
        lista_refazer.clear()


gravar_lista(lista_tarefas, CAMINHO)
