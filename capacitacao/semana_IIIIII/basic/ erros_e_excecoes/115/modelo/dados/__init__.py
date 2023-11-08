

def cadastrar() -> dict:

    print('Informações')
    nome = ler_nome()
    idade = ler_idade()

    return {'nome': nome, 'idade': idade}


def ler_nome() -> str:

    msn = 'Nome: '

    while True:
        nome = input(msn).strip()

        nome = nome.replace('.', '')

        if not nome.isdigit():
            return nome.title()
        msn = 'Informe um nome válido: '


def ler_idade() -> int:

    while True:
        idade = ler_int('Idade: ')

        if idade <= 0:
            print(f'Idade inválida: {idade}', msn=True)
            continue

        return idade


def menu():
    print(
        f'{"  Menu  ":=^32}',
        f'{  "1 - Listar Pessoas"}',
        f'{  "2 - Cadastrar Pessoa"}',
        f'{  "3 - sair"}',
        f'{"="*32}',
        sep='\n'
    )


def ler_int(msn):
    try:
        valor = int(input(msn))

        return valor
    except ValueError:
        print(f'valor inválido: {valor}')
        return ler_int('Insira uma valor válido: ')


def listar_pessoas(lista):

    for pessoa in lista:
        print(f'Nome: {pessoa["nome"]}, idade: {pessoa["idade"]}')
