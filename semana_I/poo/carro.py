class Carro():
  def __init__(self, modelo, marca):
    self.modelo = modelo
    self.marca = marca

    print('o modelo criado foi modelo: {}, marca : {}'.format(self.modelo, self.marca))

  
  def __str__(self) -> str:
    return f"modelo: {self.modelo}, marca : {self.marca}"

  @classmethod
  def info(cls):
    print('''Automóvel ou carro é um veículo motorizado com rodas usado 
para transporte.A maioria das definições de carro diz que eles correm
basicamente em estradas,acomodam de uma a oito pessoas, têm quatro pneus e,
principalmente,transportam pessoas em vez de mercadorias.''')