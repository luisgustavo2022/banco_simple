class Conta:
    def __init__(self, codigo, nome):
        self._codigo = codigo
        self._nome = nome
        self._saldo = 0
    def Depositar(self, dep):
        self._saldo = self._saldo + dep
    def Sacar(self, saq):
        self._saldo = self._saldo - saq
    def Saldo(self):
        print(self._saldo)
