class ContaBancaria:
  teste = 'teste'
  def __init__(self, nome, saldo=0.0) -> None:
    self.titular = nome
    self.saldo = saldo

  def __str__(self) -> str:
    return f'titular da conta: {self.titular}'

  @property
  def saldo(self):
    return self._saldo

  @saldo.setter
  def saldo(self, valor):
    self._saldo = valor

  @saldo.getter
  def saldo(self):
    return self._saldo

  @property
  def titular(self):
    return self._titular

  @titular.setter
  def titular(self, nome):
    self._titular = nome

  @titular.getter
  def titular(self):
    return self._titular

  