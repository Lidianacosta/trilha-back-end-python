class Ponto:

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def mostra_ponto(self):  # usa a instância
    print(f'P({self.x},{self.y})')

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, x):
    self._x = x

  @x.getter
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, y):
    self.y = y

  @y.getter
  def y(self):
    return self._y
