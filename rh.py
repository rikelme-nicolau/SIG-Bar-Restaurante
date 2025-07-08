import clientes

rh_dados = {}

cargos = {
    '1': 'Cozinheiro',
    '2': 'Garçom',
    '3': 'Barman',
    '4': 'Balconista',
    '5': 'Gerente'
            }

def verificar_funcionario_ativo():
    verificar = False
    for funcionario in rh_dados:
        if rh_dados[funcionario][5]:
            verificar = True
    return verificar

def verificar_funcionario_desativado():
    verificar = False
    for funcionario in rh_dados:
        if not rh_dados[funcionario][5]:
            verificar = True
    return verificar

def cadastrar_funcionario():
    print("╔══════════════════════════════╗")
    print("║   Cadastrar Funcionário      ║")
    print("╚══════════════════════════════╝")

    nome = input("╔════════════════════════════════════════════╗\n"
                 "║ Digite o nome do funcionário:             ║\n"
                 "╚════════════════════════════════════════════╝\n> ")

    if nome == '':
        while nome == '':
            nome = input("╔════════════════════════════════════════════╗\n"
                         "║ Digite o nome do funcionário:             ║\n"
                         "╚════════════════════════════════════════════╝\n> ")


    data_nascimento = input("╔════════════════════════════════════════════╗\n"
                            "║ Digite a data de nascimento (DD/MM/AAAA): ║\n"
                            "╚════════════════════════════════════════════╝\n> ")

    if not clientes.data_valida(data_nascimento):
        while not clientes.data_valida(data_nascimento):
            data_nascimento = input("╔════════════════════════════════════════════╗\n"
                                    "║ Digite a data de nascimento válida (DD/MM/AAAA): ║\n"
                                    "╚════════════════════════════════════════════╝\n> ")


    cpf = input("╔════════════════════════════════════════════╗\n"
                "║ Digite o CPF:                             ║\n"
                "╚════════════════════════════════════════════╝\n> ")

    if not clientes.validaCPF(cpf):
        while not clientes.validaCPF(cpf):
            cpf = input("╔════════════════════════════════════════════╗\n"
                        "║ Digite o CPF válido:                      ║\n"
                        "╚════════════════════════════════════════════╝\n> ")

    print("╔════════════════════════════════════╗")
    print("║ Qual o cargo exercido?            ║")
    print("║ (1) Cozinheiro                    ║")
    print("║ (2) Garçom                        ║")
    print("║ (3) Barman                        ║")
    print("║ (4) Balconista                    ║")
    print("║ (5) Gerente                       ║")
    print("╚════════════════════════════════════╝")

    cargo = input("> ")

    if cargo not in cargos.keys():
        cargo = input("> ")


    id_funcionario = str(len(rh_dados))
    rh_dados[id_funcionario] = [id_funcionario, nome, data_nascimento, cpf, cargos[cargo], True]

    print("╔════════════════════════════════════════════╗")
    print("║ Funcionário cadastrado com sucesso!       ║")
    print("╚════════════════════════════════════════════╝")
    input("╔════════════════════════════════════════════╗\n"
          "║ Pressione <enter> para retornar ao menu    ║\n"
          "╚════════════════════════════════════════════╝")

def gerenciar_funcionario():
    print("╔══════════════════════════════╗")
    print("║     RH | Gerenciar           ║")
    print("╚══════════════════════════════╝")
    print("╔══════════════════════════════╗")
    print("║ (1) Visualizar funcionários  ║")
    print("║ (2) Desativar funcionários   ║")
    print("║ (3) Ativar funcionários      ║")
    print("╚══════════════════════════════╝")

    rh_select = input("> ")

    if rh_select == '1':
        if verificar_funcionario_ativo():
            for funcionario in rh_dados:
                if rh_dados[funcionario][5]:
                    print("╔══════════════════════════════════════╗")
                    print(f"║ ID: {rh_dados[funcionario][0]:<33}║")
                    print(f"║ Nome: {rh_dados[funcionario][1]:<31}║")
                    print(f"║ Nascimento: {rh_dados[funcionario][2]:<25}║")
                    print(f"║ CPF: {rh_dados[funcionario][3]:<32}║")
                    print(f"║ Cargo: {rh_dados[funcionario][4]:<30}║")
                    print("╚══════════════════════════════════════╝\n")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════╗")
            print("║ Ainda não há funcionários ativos!         ║")
            print("╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

    elif rh_select == '2':
        if verificar_funcionario_ativo():
            for funcionario in rh_dados:
                if rh_dados[funcionario][5]:
                    print("╔══════════════════════════════════════╗")
                    print(f"║ ID: {rh_dados[funcionario][0]:<33}║")
                    print(f"║ Nome: {rh_dados[funcionario][1]:<31}║")
                    print("╚══════════════════════════════════════╝")
            id_desativar = input("╔════════════════════════════════════════════╗\n"
                                 "║ Digite o ID do funcionário a desativar:   ║\n"
                                 "╚════════════════════════════════════════════╝\n> ")
            rh_dados[id_desativar][5] = False
            print(f"╔════════════════════════════════════════════╗")
            print(f"║ Funcionário {id_desativar} desativado!     ║")
            print(f"╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════╗")
            print("║ Ainda não há funcionários ativos!         ║")
            print("╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

    elif rh_select == '3':
        if verificar_funcionario_desativado():
            for funcionario in rh_dados:
                if not rh_dados[funcionario][5]:
                    print("╔══════════════════════════════════════╗")
                    print(f"║ ID: {rh_dados[funcionario][0]:<33}║")
                    print(f"║ Nome: {rh_dados[funcionario][1]:<31}║")
                    print("╚══════════════════════════════════════╝")
            id_ativar = input("╔════════════════════════════════════════════╗\n"
                              "║ Digite o ID do funcionário a ativar:      ║\n"
                              "╚════════════════════════════════════════════╝\n> ")
            rh_dados[id_ativar][5] = True
            print(f"╔════════════════════════════════════════════╗")
            print(f"║ Funcionário {id_ativar} ativado!           ║")
            print(f"╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════╗")
            print("║ Ainda não há funcionários desativados!    ║")
            print("╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")