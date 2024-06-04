from abc import ABC, abstractmethod

from AppBanco.models.Conta import Conta

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta):
        pass
