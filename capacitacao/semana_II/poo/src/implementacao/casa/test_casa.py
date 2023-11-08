from casa import Casa

casa = Casa("Lidiana")

print(casa.proprietario)
print('ocupado'if casa.banheiro.ocupado else 'desocupado')
