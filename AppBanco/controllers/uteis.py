# Criar 3 operações bancárias: depósito, saque e extrato.

# Menu pra escolher
from AppBanco.controllers import Deposito
from AppBanco.controllers.Transacao import Transacao
from AppBanco.models.Conta_corrente import Conta_corrente


def mostrar_menu():
    menu = '''
    Escolha:
    [nu] Novo Usuário
    [c] Criar Conta Corrente
    [d] depositar
    [s] sacar
    [e] extrato
    [x] sair
    '''
    opcao = input(menu)
    return opcao

def novo_usuario():
    nome = input('Digite seu nome: ')
    print(f'Bem vindo {nome}')

def nova_conta():
    numero = input('Digite o número da conta: ')
    cliente = input('Digite o nome do cliente: ')
    conta = Conta_corrente(numero, cliente)
    print(f'Conta criada com sucesso!')

def depositar(saldo, extrato):
    valor = float(input('Digite o valor do depósito: R$ '))
    if valor > 0 :
        deposito = Transacao.Registrar(valor)
        '''
        saldo += valor  # equivale a saldo + valor
        resultado = f'Depósito de R$ {valor} confirmado!\nSaldo: R$ {saldo}'
        print(resultado)
        extrato += f"Depósito de R$ {valor}! Saldo atualizado: R$ {saldo}\n"
        '''
    return saldo, extrato


def sacar(quantidade_de_saques, saldo, extrato):
    valor = float(input('Digite o valor do saque: R$ '))
    if quantidade_de_saques > 0:
        if valor <= saldo:
            saldo -= valor
            print(f'Saque de R$ {valor} confirmado!\nSaldo: R$ {saldo}')
            extrato += f'Saque de R$ {valor}! Saldo atualizado: R$ {saldo}\n'
        else:
            print(f'Infelizmente não será possível sacar o dinheiro por falta de saldo\nSaldo: R$ {saldo}')
    else:
        print(f'Infelizmente não será possível sacar o dinheiro por limite de saques')
    return saldo, extrato

def mostrar_extrato():
    pass