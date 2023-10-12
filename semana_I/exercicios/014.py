temperatura = float(input('informe a temperatura em °C: '))
conversao = (temperatura * 9 / 5) + 32
print('a temperatura {:0.2f}°C corresponde a {:0.2f}°F'.format(
    temperatura, conversao))
