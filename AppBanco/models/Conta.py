'''
Classe conta A classe conta deve ter:
saldo;
número;
agência;
cliente;
e histórico;
todos como atributos da classe e são privados 
4 métodos: saldo - não recebe nenhum argumento ele retorna float; nova conta - é um método que cria uma conta (método de fábrica) então ele vai receber um cliente e o número da conta que pode ser um temporário, e tem retornar o objeto contra; a operação de sacar - recebe um valor que é float e retorna um boleano; e o depositar recebe um valor que é float e retorna boleano, para que se a operação aconteceu com sucesso ou falha retorna True se deu certo sacar, e caso se não depositar retorna falso, se deu errado e não depositar, por falso se deu errado também.
'''

from AppBanco.models.Historico import Historico


class Conta:
    def __init__(self, _numero, _cliente):
        self._saldo = 0
        self._número
        self._agência = "001"
        self._cliente = _cliente
        self._histórico = Historico()

    def saldo(self):
        return self._saldo
    
    def nova_conta():
        pass

    def sacar():
        pass

    def depositar():
        pass
    