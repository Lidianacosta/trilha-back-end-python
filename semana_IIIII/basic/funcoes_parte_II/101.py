

def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 0:
        return f'Idade invalida: {idade}'

    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO."

    if idade >= 16 and idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
