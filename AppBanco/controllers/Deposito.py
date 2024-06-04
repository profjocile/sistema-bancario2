from AppBanco.controllers.Transacao import Transacao
from AppBanco.models.Conta import Conta


class Depositar(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def Registrar(self, conta: Conta):
        print(f"Depositando R$ {self.valor}")
        saldo += self.valor  # equivale a saldo + valor
        resultado = f'Depósito de R$ {self.valor} confirmado!\nSaldo: R$ {saldo}'
        print(resultado)
        extrato += f"Depósito de R$ {self.valor}! Saldo atualizado: R$ {saldo}\n"

