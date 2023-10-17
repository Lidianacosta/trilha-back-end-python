from empresa import Empresa
from funcionario import Funcionario


empresa = Empresa("coca cola")

print(f"nome {empresa.nome}")

empresa.cadastrar_funcionario(Funcionario('luiz otavio', 1000, 'empacotador'))

empresa.listar_funcionarios()
