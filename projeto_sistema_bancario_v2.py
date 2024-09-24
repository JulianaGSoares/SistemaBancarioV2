def menu():
    menu_text = """
    ============ MENU =============
    [1]\tCadastrar novo usuário
    [2]\tCriar conta
    [3]\tListar contas
    [4]\tDepositar
    [5]\tSacar
    [6]\tVisualizar extrato
    [0]\tSair

    Digite sua opção => """
    return input(menu_text)

def criar_novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado em outro usuário!".center(50,))
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário cadastrado com sucesso!".center(50, '='))

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Conta cadastrada com sucesso!".center(50, '='))
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
        print("Usuário não encontrado.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        cadastro = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(cadastro)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print()
        print(extrato)

    else:
        print("Falha na operação! Informe um valor válido.".center(50,))

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_por_saque, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_por_saque
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente para completar a operação!".center(50,))

    elif excedeu_limite:
        print("Valor máximo por saque -> R$ 500.00".center(50,))

    elif excedeu_saques:
        print("Limites de saques diários já foram atingidos!".center(50,))
            
    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        print(extrato)

    else:
        print("Valor inválido, tente novamente!".center(50, '*'))
            
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print()
    print("EXTRATO".center(50,'='))
    print(f" Saldo: R$ {saldo:.2f} ".center(50,'='))
    print()

def main():
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            criar_novo_usuario(usuarios)
        
        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            contas.append(conta)

        elif opcao == "3":
            listar_contas(contas)     
        
        elif opcao == "4":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "5":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_por_saque=LIMITE_POR_SAQUE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "6":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "0":
         print()
         print(" Tenha um ótimo dia! ".center(50,))
         print()
         break
        
        else:
         print("Operação inválida. Selecione novamente uma das opções.".center(50,))


main()
