
def ajuda(cmd):
    help(cmd)


def titulo(msn):
    print('~'*(len(msn)+4))
    print(' ', msn, '  ')
    print('~'*(len(msn)+4))


while True:
    titulo('Manual de Bibliotecas e Funções')
    comando = input('Função ou Biblioteca: ')

    if comando.upper() == "FIM":
        break

    ajuda(comando)
