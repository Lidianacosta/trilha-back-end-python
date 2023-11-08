from Aluno import Aluno
from Curso import Curso

curso = Curso('ti')

aluno_1 = Aluno('lidiana')

curso.lista_alunos.append(aluno_1)
print(curso.nome)
print(curso.lista_alunos[0].nome)
