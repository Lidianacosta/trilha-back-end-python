from modelos import Pleno, Junior, Senior

lucas = Junior('lucas')
lucas.busca_perguntas_sem_resposta()
lucas.mostrar_tarefas()

ana = Pleno('ana')
ana.busca_perguntas_sem_resposta()
ana.busca_cursos_do_mes()

ana.mostrar_tarefas()

print(ana)


maria = Senior('maria')
maria.busca_perguntas_sem_resposta()
maria.busca_cursos_do_mes()

maria.mostrar_tarefas()

print(maria)
