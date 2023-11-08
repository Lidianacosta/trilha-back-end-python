class Animal:
    def __init__(self):
        self.nome = None
        self.classnome = self.__class__.__name__

    def domir(self):
        print(f'O {self.classnome} {self.nome} esta domindo'if self.nome is not
              None else f'O {self.classnome} esta dormindo')

    def comer(self):
        print(f'O {self.classnome} {self.nome} esta comendo'if self.nome is not
              None else f'O {self.classnome} esta comendo')
