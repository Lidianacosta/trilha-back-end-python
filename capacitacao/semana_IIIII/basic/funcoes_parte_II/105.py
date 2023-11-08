
def notas(*n, situacao=False) -> dict:
    """ analisa as notas de varios alunos e a situação.

    Args:
        n (tuple): tuple de floats que as notas
        situacao (bool, optional): descreve a situação como
        boa, ou razoável. Defaults to False.

    Returns:
        dict: devolve um dicionario com as informações maior nota,
    total de notas, media das notas e dependendo do parametro situação retorna
    a situação da turma
    """
    maior_nota = 0
    media = 0

    for i in n:
        media += i
        if i > maior_nota:
            maior_nota = i

    media /= len(n)

    if situacao:

        s = 'Boa' if media >= 7 else 'Razoável' if media >= 4 else 'Ruim'

        return {
            'total de notas': len(n),
            'maior nota': maior_nota,
            'media': media,
            'situação': s
        }
    else:
        return {
            'total de notas': len(n),
            'maior nota': maior_nota,
            'media': media
        }


resp = notas(5, 6, 7, 8, 9, 7)
print(resp)
help(notas)
