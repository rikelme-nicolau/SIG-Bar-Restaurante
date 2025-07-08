clientes_dados = {}
atributos = {
            1: 'nome',
            2: 'CPF',
            3: 'email',
            4: 'telefone',
            5: 'nascimento'
}

### validador de cpf desenvolvido por flavius

def data_valida(data):
    try:
        # faz o split e transforma em números
        dia, mes, ano = map(int, data.split('/'))

        # mes ou ano inválido, retorna False
        if mes < 1 or mes > 12 or ano <= 0:
            return False

        # verifica qual o último dia do mês
        if mes in (1, 3, 5, 7, 8, 10, 12):
            ultimo_dia = 31
        elif mes == 2:
            if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                ultimo_dia = 29
            else:
                ultimo_dia = 28
        else:
            ultimo_dia = 30

        # verifica se o dia é válido
        if dia < 1 or dia > ultimo_dia:
            return False

        return True
    except ValueError:
        return False

def validaCPF(cpf):
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0
    if tam != 11:
        return False
    for i in range(11):
        if (cpf[i]<'0')or(cpf[i]>'9'):
            return False
    for i in range(9):
        soma += (int(cpf[i])*(10 - i))
    d1 = 11 - (soma % 11)
    if (d1 == 10 or d1 == 11):
        d1 = 0
    if d1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += (int(cpf[i]) * (11 - i))
    d2 = 11 - (soma % 11)
    if (d2 == 10 or d2 == 11):
        d2 = 0
    if d2 != int(cpf[10]):
        return False
    return True

def verificar_clientes_ativos() -> bool:
    atividade = False
    for cliente in clientes_dados:
        if clientes_dados[cliente][6]:
            atividade = True
    return atividade

def verificar_clientes_desativados():
    atividade = False
    for cliente in clientes_dados:
        if not clientes_dados[cliente][6]:
            atividade = True
    return atividade

def mostrar_clientes_ativos():
    for cliente in clientes_dados:
        if clientes_dados[cliente][6]:
            print("╔══════════════════════════════════════╗")
            print(f"║ id: {clientes_dados[cliente][0]:<33}║")
            print(f"║ Nome: {clientes_dados[cliente][1]:<31}║")
            print(f"║ CPF: {clientes_dados[cliente][2]:<32}║")
            print(f"║ Email: {clientes_dados[cliente][3]:<30}║")
            print(f"║ Telefone: {clientes_dados[cliente][4]:<28}║")
            print(f"║ Nascimento: {clientes_dados[cliente][5]:<26}║")
            print("╚══════════════════════════════════════╝\n")

def mostrar_clientes_desativados():
    for cliente in clientes_dados:
        if not clientes_dados[cliente][6]:
            print("╔══════════════════════════════════════╗")
            print(f"║ id: {clientes_dados[cliente][0]:<33}║")
            print(f"║ Nome: {clientes_dados[cliente][1]:<31}║")
            print(f"║ CPF: {clientes_dados[cliente][2]:<32}║")
            print(f"║ Email: {clientes_dados[cliente][3]:<30}║")
            print(f"║ Telefone: {clientes_dados[cliente][4]:<28}║")
            print(f"║ Nascimento: {clientes_dados[cliente][5]:<26}║")
            print("╚══════════════════════════════════════╝\n")

def cadastrar_cliente():
    print("╔══════════════════════╗")
    print("║ Cadastrar cliente    ║")
    print("╚══════════════════════╝")


    nome = input("╔══════════════════════╗\n║ Nome:                ║\n╚══════════════════════╝\n> ")

    if nome == '':
        while nome == '':
            nome = input("╔══════════════════════╗\n║ Nome:                ║\n╚══════════════════════╝\n> ")

    cpf = input("╔══════════════════════╗\n║ CPF:                 ║\n╚══════════════════════╝\n> ")

    if not validaCPF(cpf):
        while not validaCPF(cpf):
            cpf = input("╔══════════════════════╗\n║ CPF:                 ║\n╚══════════════════════╝\n> ")



    email = input("╔══════════════════════╗\n║ Email:               ║\n╚══════════════════════╝\n> ")
    telefone = input("╔══════════════════════╗\n║ Telefone:            ║\n╚══════════════════════╝\n> ")
    nascimento = input("╔══════════════════════════════╗\n║ Data de Nascimento xx/xx/xxx:          ║\n╚══════════════════════════════╝\n> ")

    if not data_valida(nascimento):
        while not data_valida(nascimento):
            nascimento = input(
                "╔══════════════════════════════╗\n║ Data de Nascimento:          ║\n╚══════════════════════════════╝\n> ")


    id_cliente = str(len(clientes_dados))
    clientes_dados[id_cliente] = [id_cliente, nome, cpf, email, telefone, nascimento, True]

    print("╔════════════════════════════════════╗")
    print("║ Cliente cadastrado com sucesso!   ║")
    print("╚════════════════════════════════════╝")
    input("╔════════════════════════════════════════════════╗\n"
          "║ Pressione <enter> para retornar ao menu principal ║\n"
          "╚════════════════════════════════════════════════╝")

def gerenciar_cliente():
    print("╔════════════════════════════╗")
    print("║     Gerenciar cliente      ║")
    print("╚════════════════════════════╝")
    print("╔════════════════════════════════════════════╗")
    print("║ (1) Visualizar clientes ativos            ║")
    print("║ (2) Excluir clientes                      ║")
    print("║ (3) Ativar clientes                       ║")
    print("║ (4) Alterar informação clientes           ║")
    print("╚════════════════════════════════════════════╝")

    cliente_select = input("> ")

    if cliente_select == '1':
        if verificar_clientes_ativos():
            mostrar_clientes_ativos()
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════╗")
            print("║ Sem clientes ativos no momento... ║")
            print("╚════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

    elif cliente_select == '2':
        if verificar_clientes_ativos():
            mostrar_clientes_ativos()
            selecionado = input("╔════════════════════════════════════╗\n"
                                "║ Digite o ID do cliente a excluir:  ║\n"
                                "╚════════════════════════════════════╝\n> ")
            clientes_dados[selecionado][6] = False
            print(f"╔════════════════════════════════════════════╗")
            print(f"║ Cliente {clientes_dados[selecionado][1]} foi desativado ║")
            print(f"╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════╗")
            print("║ Sem clientes ativos no momento... ║")
            print("╚════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

    elif cliente_select == '3':
        if verificar_clientes_desativados():
            mostrar_clientes_desativados()
            id_ativar = input("╔════════════════════════════════════════════╗\n"
                              "║ Qual ID do cliente que deseja ativar?:     ║\n"
                              "╚════════════════════════════════════════════╝\n> ")
            clientes_dados[id_ativar][6] = True
            print("╔════════════════════════════════════╗")
            print("║ Cliente ativado com sucesso!      ║")
            print("╚════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════╗")
            print("║ Sem clientes desativados no momento ║")
            print("╚════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

    elif cliente_select == '4':
        if verificar_clientes_ativos():
            mostrar_clientes_ativos()
            selecionado = input("╔════════════════════════════════════╗\n"
                                "║ Digite o ID do cliente:            ║\n"
                                "╚════════════════════════════════════╝\n> ")

            print(f"╔════════════════════════════════════════════╗")
            print(f"║ Cliente {selecionado} selecionado com sucesso! ║")
            print(f"╚════════════════════════════════════════════╝")

            print("╔════════════════════════════════════╗")
            print("║ Onde deseja fazer a alteração?     ║")
            print("║ (1) Nome                           ║")
            print("║ (2) CPF                            ║")
            print("║ (3) Email                          ║")
            print("║ (4) Telefone                       ║")
            print("║ (5) Nascimento                     ║")
            print("╚════════════════════════════════════╝")

            alterar = int(input("> "))

            print(f"╔════════════════════════════════════╗")
            print(f"║ Ok, digite o novo {atributos[alterar]}{' ' * (28 - len(atributos[alterar]))}║")
            print(f"╚════════════════════════════════════╝")
            novo = input("> ")
            clientes_dados[selecionado][alterar] = novo

            print("╔════════════════════════════════════╗")
            print("║ Mudança feita com sucesso!        ║")
            print("╚════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════╗")
            print("║ Sem clientes ativos no momento... ║")
            print("╚════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")