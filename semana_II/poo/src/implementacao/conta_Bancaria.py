class ContaBancaria:

    def __init__(self, saldo=0.0):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @saldo.getter
    def saldo(self):
        return self.__saldo
