from AppBanco.controllers.uteis import *

saldo = 0
extrato = ""
limite_de_saque = 500
quantidade_de_saques = 3

def main():
    global saldo
    global extrato
    while True:
        opcao = mostrar_menu()    
        if opcao == 'x': break
        elif opcao == 'd': saldo, extrato = depositar(saldo, extrato)
        elif opcao == 's': saldo, extrato = sacar(quantidade_de_saques, saldo, extrato)
        elif opcao == 'e': print(extrato)
        else : print('Opção inválida!')

main()