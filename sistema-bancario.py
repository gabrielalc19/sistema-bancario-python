# Sistema Bancário em Python

# Variáveis principais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Menu de operações
menu = """
========== NU-PANK ==========
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
=> """

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print(f"O valor excede o limite de R$ {limite:.2f} por saque.")
        elif excedeu_saques:
            print("Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")
        else:
            print("Valor inválido.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================\n")

    elif opcao == "0":
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break

    else:
        print("Opção inválida. Selecione uma opção válida.")
