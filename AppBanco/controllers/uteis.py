# Criar 3 operações bancárias: depósito, saque e extrato.

# Menu pra escolher
def mostrar_menu():
    menu = '''
    Escolha:
    [d] depósitar
    [s] sacar
    [e] extrato
    [x] sair
    '''
    opcao = input(menu)
    return opcao

def depositar(saldo, extrato):
    valor = float(input('Digite o valor do depósito: R$ '))
    if valor > 0 :
        saldo += valor  # equivale a saldo + valor
        resultado = f'Depósito de R$ {valor} confirmado!\nSaldo: R$ {saldo}'
        print(resultado)
        extrato += f"Depósito de R$ {valor}! Saldo atualizado: R$ {saldo}\n"
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