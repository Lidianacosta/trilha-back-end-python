
def area(largura, comprimento) -> None:
    print(
        f'A area de um terreno com {largura:.2f} de largura',
        f'e {comprimento:.2f} comprimento é {largura * comprimento:.2f}m²'
    )


def main():
    area(4.5, 8)
    area(comprimento=4.5, largura=8)


if __name__ == main():
    main()
