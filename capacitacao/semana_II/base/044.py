print(
    '''oferecemos como metodo de pagamento os seguintes serviços:
  
              dinheiro - cheque - cartão
  ''')

valor_produto = float(input('qual o valor do produto?: '))
metodo_pagamento = input('Qual vai ser o metodo de pagamento?: ')

if metodo_pagamento == 'dinheiro' or metodo_pagamento == 'cheque':
    print(
        f'o valor a ser pago {valor_produto} '
        f'com 10% de desconto fica {valor_produto*0.9:.2f}'
    )
elif metodo_pagamento == 'cartão':
    print('\n\tà vista ou pacelamos em ate 10 vezes\n')
    metodo_pagamento_cartão = input('Qual vai ser o metodo de pagamento?: ')

    if metodo_pagamento_cartão == 'à vista':
        print(
            f'o valor a ser pago {valor_produto} '
            f'com 50% de desconto fica {valor_produto*0.95:.2f}'
        )
    elif metodo_pagamento_cartão == '2':
        print(
            f'o valor a ser pago: {valor_produto:.2f}'
        )
    elif metodo_pagamento_cartão.isdigit() and int(metodo_pagamento_cartão) <= 10 and int(metodo_pagamento_cartão) > 0:
        valor_pagar = float(valor_produto) * 1.2
        print(
            f'o valor de {valor_produto} em {metodo_pagamento_cartão}x '
            f'no cartão com juros de 20% fica {valor_pagar:.2f} '
            f'e o valor das pacelas ficam {valor_pagar/float(metodo_pagamento_cartão):.2f}x{metodo_pagamento_cartão}'
        )
    else:
        print('metodo de pagamento não disponivel')
else:
    print('metodo de pagamento não disponivel')
