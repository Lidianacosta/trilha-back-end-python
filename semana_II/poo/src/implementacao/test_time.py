from Time import Time
from jogador import Jogador

time = Time('flamengo')
print(f'nome do time: {time.nome}')

time.inserir_jogador(Jogador('Bruno Henrique', 30))
time.inserir_jogador(Jogador('arascaeta', 30))
time.inserir_jogador(Jogador('gabigol', 30))
time.listar_jogadores()
