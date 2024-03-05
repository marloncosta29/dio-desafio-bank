menu = """
    Menu
    (1) Depositar
    (2) Sacar
    (3) Extrato
    (4) Sair
"""

balance = 0
withdraw_count = 0
limit = 500
statement = ""

WITHDRAW_LIMIT = 3

while True:
    option = input(menu)

    if option == '1':
        value = float(input("Digite o valor a ser depositado: "))
        if(value > 0):
            balance += value
            statement += f"Depósito de {value:.2f}\n"
        else:
            print('Operação falhou - O valor informado é invalido')

    elif option == '2':
        value = float(input("Digite o valor a ser sacado: "))
        is_valid = value > 0
        has_limit = value < balance
        exceeded_limit = value > limit
        can_withdraw = withdraw_count < WITHDRAW_LIMIT

        if(not is_valid):
            print('Operação falhou - O valor digitado é invalido')
        elif(not has_limit):
            print('Operação falhou - Saldo insuficiente')
        elif(not can_withdraw):
            print('Operação falhou - Limite de saque atingido')
        elif(exceeded_limit):
            print('Operação falhou - Limite de saque excedido')
        else:
            balance -= value
            statement += f"Saque no valor de {value:.2f}\n"
            withdraw_count += 1
    elif option == '3':
        print("\n**********EXTRATO**********")
        print("Nao foram realizados movimentações" if not statement else statement)
        print(f"Saldo: {balance:.2f}")
        print("\n***************************")

    elif option == '4':
        break
    else:
        print('Escolha uma opção valida')
