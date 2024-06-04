from Transacao import Transacao

class Depositar(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def Registrar(self):
        print(f"Depositando R$ {self.valor}")
