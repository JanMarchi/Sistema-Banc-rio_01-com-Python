import textwrap


class ContaBancaria:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0


def menu():
    menu_text = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_text))


def depositar(conta, valor):
    if valor > 0:
        conta.saldo += valor
        conta.extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def sacar(conta, valor):
    excedeu_saldo = valor > conta.saldo
    excedeu_limite = valor > conta.limite
    excedeu_saques = conta.numero_saques >= 3

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        conta.saldo -= valor
        conta.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        conta.numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        numero_conta = len(contas) + 1
        conta = ContaBancaria(agencia="0001", numero_conta=numero_conta, usuario=usuario)
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas():
    for conta in contas:
        linha = f"""\
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero_conta}
            Titular:\t{conta.usuario['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


usuarios = []
contas = []


def main():
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            depositar(contas[-1], valor) if contas else print("\n@@@ Nenhuma conta encontrada. @@@")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            sacar(contas[-1], valor) if contas else print("\n@@@ Nenhuma conta encontrada. @@@")

        elif opcao == "e":
            exibir_extrato(contas[-1]) if contas else print("\n@@@ Nenhuma conta encontrada. @@@")

        elif opcao == "nu":
            criar_usuario()

        elif opcao == "nc":
            criar_conta()

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
