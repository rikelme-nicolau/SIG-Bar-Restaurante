import estoque

menu_dados = {}

def verificar_existe_prato():
    verificar = False
    for prato in menu_dados:
        if menu_dados[prato][0]:
            verificar = True
    return verificar

def visualizar_pratos():
    print("╭════════════════════════════════════════════════════════╮")
    print("│     Lista de Pratos Cadastrados                        │")
    print("╰════════════════════════════════════════════════════════╯")

    if not menu_dados:
        print("╭────────────────────────────────────────────────────────╮")
        print("│ Nenhum prato cadastrado no momento.                    │")
        print("╰────────────────────────────────────────────────────────╯")
    else:
        for prato in menu_dados:
            print("╭────────────────────────────────────────────────────────╮")
            print(f"│ ID do Prato: {menu_dados[prato][1]}")
            print(f"│ Nome:       {menu_dados[prato][2]}")
            print("╰────────────────────────────────────────────────────────╯")


def cadastrar_prato():
    if estoque.estoque_alimento_ativo():
        estoque.mostrar_alimentos_ativos()
        nome = input("╔════════════════════════════════════════════╗\n"
                     "║ Digite o nome do prato:                   ║\n"
                     "╚════════════════════════════════════════════╝\n> ").upper()

        alimento = input("╔════════════════════════════════════════════╗\n"
                         "║ Digite o id do alimento:                  ║\n"
                         "╚════════════════════════════════════════════╝\n> ")
        quantidade = int(input("╔════════════════════════════════════════════╗\n"
                               "║ Digite a quantidade usada no prato:       ║\n"
                               "╚════════════════════════════════════════════╝\n> "))

        id_prato = str(len(menu_dados))
        menu_dados[id_prato] = [True, id_prato, nome, [alimento, quantidade]]

        print("╔════════════════════════════════════════════════════════════╗")
        print(f"║ {estoque.estoque_alimento[alimento][1]} foi adicionado ao {nome} utilizando {quantidade} de produto. ║")
        print("╚════════════════════════════════════════════════════════════╝")

        loop = input("╔════════════════════════════════════════════╗\n"
                     "║ Deseja adicionar mais algum alimento?     ║\n"
                     "╚════════════════════════════════════════════╝\n> ").lower()

        while loop == 'sim':
            if estoque.estoque_alimento_ativo():
                estoque.mostrar_alimentos_ativos()

                alimento = input("╔════════════════════════════════════════════╗\n"
                                 "║ Digite o id do alimento:                  ║\n"
                                 "╚════════════════════════════════════════════╝\n> ")
                quantidade = int(input("╔════════════════════════════════════════════╗\n"
                                       "║ Digite a quantidade usada no prato:       ║\n"
                                       "╚════════════════════════════════════════════╝\n> "))

                menu_dados[id_prato].append([alimento, quantidade])
                print("╔════════════════════════════════════════════════════════════╗")
                print(f"║ {estoque.estoque_alimento[alimento][2]} foi adicionado ao {nome} utilizando {quantidade} de produto. ║")
                print("╚════════════════════════════════════════════════════════════╝")

                loop = input("╔════════════════════════════════════════════╗\n"
                             "║ Deseja adicionar mais algum alimento?     ║\n"
                             "╚════════════════════════════════════════════╝\n> ").lower()

        print("╔════════════════════════════════════════════╗")
        print("║ Prato cadastrado com sucesso!             ║")
        print("╚════════════════════════════════════════════╝")
        input("╔════════════════════════════════════════════╗\n"
              "║ Pressione <enter> para continuar           ║\n"
              "╚════════════════════════════════════════════╝")

    else:
        print("╔════════════════════════════════════════════╗")
        print("║ Nenhum alimento no estoque!               ║")
        print("╚════════════════════════════════════════════╝")
        input("╔════════════════════════════════════════════╗\n"
              "║ Pressione <enter> para continuar           ║\n"
              "╚════════════════════════════════════════════╝")