import textwrap

def menu():
    menu = """\n
        >>>>>>>>Menu<<<<<<<
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar contas
        [nu]\tNovo usuario
        [q]\tSair
        => """
    return input(textwrap.dedent(menu))

def depositar(balance, value, statement, /):
    if(value > 0):
        balance += value
        statement += f"Depósito de\t\t{value:.2f}\n"
        print('\n === depósito realizado com sucesso')
    else:
        print('Operação falhou - O valor informado é invalido')
    return balance, statement

def sacar(*, balance, value, statement, limit, withdraw_count, withdraw_limit):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_wthdraw = withdraw_count > withdraw_limit

    if exceeded_balance:
        print("\n@@@ Operação falhou - Saldo insuficiente. @@@")
    elif exceeded_limit:
        print("\n@@@ Operação falhou - Limite ecedido. @@@")
    elif exceeded_wthdraw:
        print("\n@@@ Operação falhou - Numero de saques excedido. @@@")
    elif value > 0:
        balance -= value
        statement += f"Saque:\t\tR$ {value:.2f}\n"
        withdraw_count += 1
        print('\n=== Saque realizado com sucesso ===')
    else:
        print("\n@@@ Operação falhou - valor invalido. @@@")
    
    return balance, statement

def show_statement(balance, /, *, statement):
    print("\n=====EXTRATO=====")
    print("Não foram realizados movimentações" if not statement else statement)
    print(f"\nSaldo:\t\tR$ {balance:.2f}")
    print("\n=================")

def create_user(users: list):
    cpf = input("Informe o cof (somente numeros): ")
    user = filter_user(cpf=cpf, users=users)

    if user:
        print("\n@@@ Usuario ja existe no sistema @@@@")
        return

    name = input("Informe o nome completo: ")
    date_of_birth = input("Informe a data de nascimento: ")
    address = input("Informe o endereco completo: ")

    users.append({"name": name, "date_of_birth": date_of_birth, "cpf": cpf, "address": address})
    print("=== Usuário criado com sucesso! ===")

def filter_user(cpf, users):
    filtred_users = [user for user in users if user['cpf'] == cpf]
    return filtred_users[0] if filtred_users else None

def create_account(agency, account_number, users: list):
    cpf = input("Informe o cpf: ")
    user = filter_user(cpf=cpf, users=users)

    if user:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agency, "numero_conta": account_number, "usuario": user}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def list_accounts(accounts: list):
    for ac in accounts:
        line = f"""\
            Agência:\t{ac['agencia']}
            C/C:\t\t{ac['numero_conta']}
            Titular:\t{ac['usuario']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))

def main():
    WITHDRAW_LIMIT = 3
    AGENCY = '0001'

    balance = 0
    limit = 500
    statement = ""
    withdraw_count = 0
    users = []
    accounts = []

    
    while True:
        option = menu()


        if option == 'd':
            value = float(input("Digite o valor a ser depositado: "))
            balance, statement = depositar(balance, value, statement)
        elif option == 's':
            value = float(input("Digite o valor a ser sacado: "))
            balance, statement = sacar(balance=balance, value=value, limit=limit, statement=statement, withdraw_count=withdraw_count, withdraw_limit=WITHDRAW_LIMIT)
        elif option == 'e':
            show_statement(balance, statement=statement)
        elif option == 'nc':
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)
            if(account):
                accounts.append(account)

        elif option == 'lc':
            list_accounts(accounts=accounts)
        elif option == 'nu':
            create_user(users=users)
        elif option == 'q':
            break
        else:
            print('Escolha uma opção valida')

main()