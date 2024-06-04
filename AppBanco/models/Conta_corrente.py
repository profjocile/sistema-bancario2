from AppBanco.models.Conta import Conta


class Conta_corrente(Conta):
    def __init__(self, _numero, _cliente, limite = 500, limite_saques = 3):
        super().__init__(_numero, _cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar():
        pass