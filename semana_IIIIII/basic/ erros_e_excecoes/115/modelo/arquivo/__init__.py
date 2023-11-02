
def ler() -> list:
    linhas = []
    pessoa = {}
    lista_pessoas = []

    try:
        with open('/workspaces/trilha-back-end-python/pessosa.txt',
                  encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        with open('pessosa.txt', encoding="utf-8", mode='w') as arquivo:
            print('criando arquivo')
            return lista_pessoas

    for p in linhas:
        nome, idade = p.split(';')
        pessoa['nome'] = nome
        pessoa['idade'] = int(idade)

        lista_pessoas.append(pessoa.copy())
        pessoa.clear()

    return lista_pessoas


def gravar(lista) -> None:

    with open('/workspaces/trilha-back-end-python/pessosa.txt', encoding="utf-8", mode='w') as arquivo:
        for pessoa in lista:
            print(arquivo.write(f'{pessoa["nome"]};{pessoa["idade"]}\n',))
