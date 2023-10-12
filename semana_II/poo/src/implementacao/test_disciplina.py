from Disciplina import Disciplina

from Professor import Professor

professor = Professor('samuel')
disciplina = Disciplina('arquitetura')

disciplina.professor = professor

print(disciplina.nome)
# print(disciplina.professor.nome)
