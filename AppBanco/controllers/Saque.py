from controllers.Transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self):
        # Lógica para registrar o saque
        pass
