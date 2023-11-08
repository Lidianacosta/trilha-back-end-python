from random import randint


def cria_pergunta(operador) -> dict:

    a = randint(1, 100)
    b = randint(1, 100)

    if operador == '/':
        resposta = a/b

        opcoes = [
            randint(1, 100)/randint(1, 10),
            randint(1, 100)/randint(1, 10),
            randint(1, 100)/randint(1, 10)
        ]
    else:

        if operador == '+':
            resposta = a + b

        if operador == '-':
            resposta = a - b

        opcoes = [
            randint(resposta - 10, resposta + 10),
            randint(resposta - 10, resposta + 10),
            randint(resposta - 10, resposta + 10)
        ]

    opcoes.append(resposta)

    opcoes.sort()

    return {
        'pergunta': f"Quanto é {a} {operador} {b}?",
        'opções': opcoes,
        'resposta': resposta,
    }


perguntas = []

perguntas.append(cria_pergunta('+'))
perguntas.append(cria_pergunta('-'))
perguntas.append(cria_pergunta('/'))


for pergunta in perguntas:
    print(f'Pergunta: {pergunta.get("pergunta")}')
    print()
    for pos, opcao in enumerate(pergunta['opções']):
        print(str(pos) + ')', f'{opcao:.2f}')

    escolha = int(input('Escolha uma opção: '))

    if pergunta['opções'][escolha] == pergunta['resposta']:
        print('Acertou')
    else:
        print('Errou')
        print('Resposta:', f'{pergunta["resposta"]:.2f}')

    print()
