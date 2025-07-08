estoque_bebida = {}

estoque_alimento = {}

def estoque_bebida_ativa() -> bool:
    sinal = False
    for estoque in estoque_bebida:
        if estoque_bebida[estoque][6]:
            sinal = True

    return sinal

def estoque_alimento_ativo() -> bool:
    sinal = False
    for estoque in estoque_alimento:
        if estoque_alimento[estoque][6]:
            sinal = True

    return sinal

def mostrar_bebidas_ativas():
    for bebida in estoque_bebida:
        if estoque_bebida[bebida][6]:
            print("╔══════════════════════════════════════╗")
            print(f"║ id: {estoque_bebida[bebida][0]:<33}║")
            print(f"║ PRODUTO: {estoque_bebida[bebida][1]:<28}║")
            print(f"║ MARCA: {estoque_bebida[bebida][2]:<30}║")
            print(f"║ CAPACIDADE: {estoque_bebida[bebida][3]:<25}║")
            print(f"║ EMBALAGEM: {estoque_bebida[bebida][4]:<26}║")
            print(f"║ QUANTIDADE: {estoque_bebida[bebida][5]:<26}║")
            print("╚══════════════════════════════════════╝\n")

def mostrar_alimentos_ativos():
    for alimento in estoque_alimento:
        if estoque_alimento[alimento][6]:
            print("╔══════════════════════════════════════╗")
            print(f"║ ID: {estoque_alimento[alimento][0]:<34}║")
            print(f"║ PRODUTO: {estoque_alimento[alimento][1]:<28}║")
            print(f"║ MARCA: {estoque_alimento[alimento][2]:<30}║")
            print(f"║ CAPACIDADE: {estoque_alimento[alimento][3]:<25}║")
            print(f"║ EMBALAGEM: {estoque_alimento[alimento][4]:<26}║")
            print(f"║ QUANTIDADE: {estoque_alimento[alimento][5]:<26}║")
            print("╚══════════════════════════════════════╝\n")

def mostrar_bebida_e_alimento_ativos():
    print("╔════════════════════╗")
    print("║ (1) Bebidas        ║")
    print("║ (2) Alimentos      ║")
    print("╚════════════════════╝")

    listagem = input("╔════════════════════════════════════════════╗\n"
                     "║ Deseja visualizar qual produto?:           ║\n"
                     "╚════════════════════════════════════════════╝\n> ")

    if listagem == '1':
        if estoque_bebida_ativa():
            mostrar_bebidas_ativas()
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════╗")
            print("║ Não possui bebidas no estoque!            ║")
            print("╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

    elif listagem == '2':
        if estoque_alimento_ativo():
            mostrar_alimentos_ativos()
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════╗")
            print("║ Não possui alimentos no estoque!          ║")
            print("╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

def adicionar_bebida_nova():
    produto = input("╔════════════════════════════════════════════╗\n"
                    "║ Digite o tipo da bebida:                   ║\n"
                    "╚════════════════════════════════════════════╝\n> ").upper()
    marca = input(f"╔════════════════════════════════════════════╗\n"
                  f"║ Digite a marca do {produto}:".ljust(44) + "║\n"
                  "╚════════════════════════════════════════════╝\n> ").upper()
    capacidade = input(f"╔════════════════════════════════════════════╗\n"
                       f"║ Digite os ml do {produto}:".ljust(44) + "║\n"
                       "╚════════════════════════════════════════════╝\n> ")
    embalagem = input(f"╔════════════════════════════════════════════╗\n"
                      f"║ Digite o embalagem do {produto}:".ljust(44) + "║\n"
                      "╚════════════════════════════════════════════╝\n> ").upper()

    id = str(len(estoque_bebida))
    estoque_bebida[id] = [id, produto, marca, capacidade, embalagem, 0, True]

    print("╔════════════════════════════════════════════╗")
    print("║ Bebida cadastrada com sucesso!            ║")
    print("╚════════════════════════════════════════════╝")
    input("╔════════════════════════════════════════════╗\n"
          "║ Pressione <enter> para retornar ao menu    ║\n"
          "╚════════════════════════════════════════════╝")

def adicionar_alimento_novo():
    produto = input("╔════════════════════════════════════════════╗\n"
                    "║ Digite o tipo de alimento:                 ║\n"
                    "╚════════════════════════════════════════════╝\n> ").upper()
    marca = input(f"╔════════════════════════════════════════════╗\n"
                  f"║ Digite a marca do {produto}:".ljust(44) + "║\n"
                  "╚════════════════════════════════════════════╝\n> ").upper()
    capacidade = input(f"╔════════════════════════════════════════════╗\n"
                       f"║ Digite os gramas do {produto}:".ljust(44) + "║\n"
                       "╚════════════════════════════════════════════╝\n> ")
    embalagem = input(f"╔════════════════════════════════════════════╗\n"
                      f"║ Digite o embalagem do {produto}:".ljust(44) + "║\n"
                      "╚════════════════════════════════════════════╝\n> ").upper()

    id = str(len(estoque_alimento))
    estoque_alimento[id] = [id, produto, marca, capacidade, embalagem, 0, True]

    print("╔════════════════════════════════════════════╗")
    print("║ Alimento cadastrado com sucesso!          ║")
    print("╚════════════════════════════════════════════╝")
    input("╔════════════════════════════════════════════╗\n"
          "║ Pressione <enter> para retornar ao menu    ║\n"
          "╚════════════════════════════════════════════╝")

def subtrair_produtos_bebidas():
    if estoque_bebida_ativa():
        mostrar_bebidas_ativas()

        id_selecionado = input("╔════════════════════════════════════════════╗\n"
                               "║ Digite o id do produto:                   ║\n"
                               "╚════════════════════════════════════════════╝\n> ")
        saida = int(input("╔════════════════════════════════════════════╗\n"
                          "║ Digite a quantidade de saída do produto:  ║\n"
                          "╚════════════════════════════════════════════╝\n> "))

        if saida <= estoque_bebida[id_selecionado][5]:
            estoque_bebida[id_selecionado][5] -= saida
        elif saida > estoque_bebida[id_selecionado][5]:
            while saida > estoque_bebida[id_selecionado][5]:
                print("╔════════════════════════════════════════════╗")
                print("║ Essa bebida não possui esse estoque!      ║")
                print("╚════════════════════════════════════════════╝")
                print(f"╔════════════════════════════════════════════╗")
                print(f"║ Selecione um valor entre 0 e {estoque_bebida[id_selecionado][5]:<20}║")
                print("╚════════════════════════════════════════════╝")
                saida = int(input("> "))
            estoque_bebida[id_selecionado][5] -= saida
    else:
        print("╔════════════════════════════════════════════╗")
        print("║ Não há nenhuma bebida ativa no estoque!   ║")
        print("╚════════════════════════════════════════════╝")
        input("╔════════════════════════════════════════════╗\n"
              "║ Pressione <enter> para retornar ao menu    ║\n"
              "╚════════════════════════════════════════════╝")
        return

    print("╔════════════════════════════════════════════╗")
    print("║ Saída com sucesso!                        ║")
    print("╚════════════════════════════════════════════╝")
    print(f"╔════════════════════════════════════════════╗")
    print(f"║ Agora o produto id:{estoque_bebida[id_selecionado][0]} possui "
          f"{estoque_bebida[id_selecionado][5]} unidades em estoque ║")
    print("╚════════════════════════════════════════════╝")
    input("╔════════════════════════════════════════════╗\n"
          "║ Pressione <enter> para retornar ao menu    ║\n"
          "╚════════════════════════════════════════════╝")

def subtrair_produtos_alimentos():
    if estoque_alimento_ativo():
        mostrar_alimentos_ativos()

        id_selecionado = input("╔════════════════════════════════════════════╗\n"
                               "║ Digite o id do produto:                   ║\n"
                               "╚════════════════════════════════════════════╝\n> ")
        saida = int(input("╔════════════════════════════════════════════╗\n"
                          "║ Digite a quantidade de saída do produto:  ║\n"
                          "╚════════════════════════════════════════════╝\n> "))

        if saida <= estoque_alimento[id_selecionado][5]:
            estoque_alimento[id_selecionado][5] -= saida

            print("╔════════════════════════════════════════════╗")
            print("║ Saída com sucesso!                        ║")
            print("╚════════════════════════════════════════════╝")
            print(f"╔════════════════════════════════════════════════════════════╗")
            print(f"║ Agora o produto id:\"{estoque_alimento[id_selecionado][0]}\" possui "
                  f"{estoque_alimento[id_selecionado][5]} unidades em estoque ║")
            print("╚════════════════════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

        elif saida > estoque_alimento[id_selecionado][5]:
            while saida > estoque_alimento[id_selecionado][5]:
                print("╔════════════════════════════════════════════╗")
                print("║ Estoque insuficiente para retirada!       ║")
                print("╚════════════════════════════════════════════╝")
                print(f"╔════════════════════════════════════════════╗")
                print(f"║ Selecione um valor entre 0 e {estoque_alimento[id_selecionado][5]:<20}║")
                print("╚════════════════════════════════════════════╝")
                saida = int(input("> "))

            estoque_alimento[id_selecionado][5] -= saida

            print("╔════════════════════════════════════════════╗")
            print("║ Saída com sucesso!                        ║")
            print("╚════════════════════════════════════════════╝")
            print(f"╔════════════════════════════════════════════════════════════╗")
            print(f"║ Agora o produto id:\"{estoque_alimento[id_selecionado][0]}\" possui "
                  f"{estoque_alimento[id_selecionado][5]} unidades em estoque ║")
            print("╚════════════════════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

    else:
        print("╔════════════════════════════════════════════╗")
        print("║ Não há nenhum alimento ativo no estoque!  ║")
        print("╚════════════════════════════════════════════╝")
        input("╔════════════════════════════════════════════╗\n"
              "║ Pressione <enter> para retornar ao menu    ║\n"
              "╚════════════════════════════════════════════╝")

def entrada_de_produtos():
    print("╔══════════════════════════════╗")
    print("║     ENTRADA DE PRODUTOS      ║")
    print("╚══════════════════════════════╝")
    print("╔════════════════════╗")
    print("║ (1) Bebida         ║")
    print("║ (2) Alimentos      ║")
    print("╚════════════════════╝\n")

    tipo = input("> ")

    if tipo == '1':
        if estoque_bebida_ativa():
            mostrar_bebidas_ativas()

            id_selecionado = input("╔════════════════════════════════════════════╗\n"
                                   "║ Digite o id do produto:                   ║\n"
                                   "╚════════════════════════════════════════════╝\n> ")
            entrada = int(input("╔════════════════════════════════════════════╗\n"
                                "║ Digite a quantidade de entrada:           ║\n"
                                "╚════════════════════════════════════════════╝\n> "))
            estoque_bebida[id_selecionado][5] += entrada

            print("╔════════════════════════════════════════════════════════════╗")
            print(f"║ Adicionado com sucesso!                                    ║")
            print(f"║ Agora o produto id: {estoque_bebida[id_selecionado][0]} possui "
                  f"{estoque_bebida[id_selecionado][5]} unidades em estoque ║")
            print("╚════════════════════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════╗")
            print("║ Não há nenhuma bebida ativa no estoque!   ║")
            print("╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

    elif tipo == '2':
        if estoque_alimento_ativo():
            mostrar_alimentos_ativos()

            id_selecionado = input("╔════════════════════════════════════════════╗\n"
                                   "║ Digite o id do produto:                   ║\n"
                                   "╚════════════════════════════════════════════╝\n> ")
            entrada = int(input("╔════════════════════════════════════════════╗\n"
                                "║ Digite a quantidade de entrada:           ║\n"
                                "╚════════════════════════════════════════════╝\n> "))
            estoque_alimento[id_selecionado][5] += entrada

            print("╔════════════════════════════════════════════════════════════╗")
            print(f"║ Adicionado com sucesso!                                    ║")
            print(f"║ Agora o produto id: {estoque_alimento[id_selecionado][0]} possui "
                  f"{estoque_alimento[id_selecionado][5]} unidades em estoque ║")
            print("╚════════════════════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════╗")
            print("║ Não há nenhum alimento ativo no estoque!  ║")
            print("╚════════════════════════════════════════════╝")
            input("╔════════════════════════════════════════════╗\n"
                  "║ Pressione <enter> para retornar ao menu    ║\n"
                  "╚════════════════════════════════════════════╝")

def saida_de_produtos():
    print("╔══════════════════════════════╗")
    print("║      SAÍDA DE PRODUTOS       ║")
    print("╚══════════════════════════════╝")
    print("╔════════════════════╗")
    print("║ (1) Bebida         ║")
    print("║ (2) Alimentos      ║")
    print("╚════════════════════╝")

    tipo = input("> ")

    if tipo == '1':
        subtrair_produtos_bebidas()

    elif tipo == '2':
        subtrair_produtos_alimentos()