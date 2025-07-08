import clientes
import menu
import estoque

id_pagamentos = {}

def adicionar_id_pagamento_novo():
    sinal = True
    while sinal:
        try:
            novo_id = int(input("╔════════════════════════════════════════════════════╗\n"
                                "║ Digite o ID do pagamento que será adicionado:     ║\n"
                                "╚════════════════════════════════════════════════════╝\n> "))
            sinal = False
        except ValueError:
            print("╔══════════════════════════════╗")
            print("║ Digite um valor inteiro.     ║")
            print("╚══════════════════════════════╝")

    if str(novo_id) not in id_pagamentos.keys():
        id_pagamentos[str(novo_id)] = [str(novo_id), False]
        print("╔══════════════════════════════╗")
        print("║ ID adicionado com sucesso!   ║")
        print("╚══════════════════════════════╝")
        input("╔════════════════════════════════════╗\n"
              "║ Pressione <enter> para continuar... ║\n"
              "╚════════════════════════════════════╝")
    else:
        print("╔══════════════════════╗")
        print("║ ID existente!         ║")
        print("╚══════════════════════╝")

def remover_id_pagamento_existente():
    mostrar_id_pagamento()

    print("╔════════════════════════════════════════════╗")
    id = input("║ Digite o ID do pagamento que será removido: ")
    print("╠════════════════════════════════════════════╣")

    if id not in id_pagamentos:
        while id not in id_pagamentos:
            id = input("║ ID inválido. Digite um ID válido: ")
            print("╠════════════════════════════════════════════╣")

    del id_pagamentos[id]

    print("║ ID removido com sucesso!                  ")
    print("╚════════════════════════════════════════════╝")
    input("Pressione <enter> para continuar...")

def add_pedido_bebida(id_pagamento):
    estoque.mostrar_bebidas_ativas()

    print("╔════════════════════════════════════════════╗")
    id_bebida = input("║ Digite o ID da bebida: ")
    print("╠════════════════════════════════════════════╣")

    if id_bebida not in estoque.estoque_bebida:
        while id_bebida not in estoque.estoque_bebida:
            id_bebida = input("║ ID inválido. Digite um ID válido: ")
            print("╠════════════════════════════════════════════╣")

    sinal = True
    while sinal:
        try:
            quantidade = int(input("║ Digite a quantidade do pedido: "))
            sinal = False
        except ValueError:
            print("║ Valor inválido. Digite um número inteiro.")
            print("╠════════════════════════════════════════════╣")

    if estoque.estoque_bebida[id_bebida][5] >= quantidade:

        id_pagamentos[id_pagamento] = [id_pagamento, True, [id_bebida, quantidade]]

        estoque.estoque_bebida[id_bebida][5] -= quantidade

        print("╔════════════════════════════════════════════╗")
        print("║ Deseja cadastrar outra bebida?            ║")
        print("║ (1) Sim                                   ║")
        print("║ (2) Não                                   ║")
        print("╚════════════════════════════════════════════╝")
        loop = input()

        while loop not in ['1', '2']:
            print("╔════════════════════════════════════════════╗")
            print("║ Opção inválida. Deseja cadastrar outra?   ║")
            print("║ (1) Sim                                   ║")
            print("║ (2) Não                                   ║")
            print("╚════════════════════════════════════════════╝")
            loop = input()

        if loop == '1':
            while loop == '1':
                estoque.mostrar_bebidas_ativas()
                print("╔════════════════════════════════════════════╗")
                id_bebida = input("║ Digite o ID da bebida: ")
                print("╠════════════════════════════════════════════╣")

                if id_bebida not in estoque.estoque_bebida:
                    while id_bebida not in estoque.estoque_bebida:
                        id_bebida = input("║ ID inválido. Digite um ID válido: ")
                        print("╠════════════════════════════════════════════╣")

                sinal = True
                while sinal:
                    try:
                        quantidade = int(input("║ Digite a quantidade do pedido: "))
                        sinal = False
                    except ValueError:
                        print("║ Valor inválido. Digite um número inteiro.")
                        print("╠════════════════════════════════════════════╣")

                if estoque.estoque_bebida[id_bebida][5] >= quantidade:
                    id_pagamentos[id_pagamento].append([id_bebida, quantidade])
                    estoque.estoque_bebida[id_bebida][5] -= quantidade

                    print("╔════════════════════════════════════════════╗")
                    print("║ Deseja cadastrar outra bebida?            ║")
                    print("║ (1) Sim                                   ║")
                    print("║ (2) Não                                   ║")
                    print("╚════════════════════════════════════════════╝")
                    loop = input()

                    while loop not in ['1', '2']:
                        print("╔════════════════════════════════════════════╗")
                        print("║ Opção inválida. Deseja cadastrar outra?   ║")
                        print("║ (1) Sim                                   ║")
                        print("║ (2) Não                                   ║")
                        print("╚════════════════════════════════════════════╝")
                        loop = input()
                else:
                    print("╔════════════════════════════════════════════╗")
                    print("║ Sem estoque para esse pedido              ║")
                    print("╚════════════════════════════════════════════╝")
                    input("Pressione <enter> para continuar")

                print("╔════════════════════════════════════════════╗")
                print("║ Deseja cadastrar outro pedido?            ║")
                print("║ (1) Sim                                   ║")
                print("║ (2) Não                                   ║")
                print("╚════════════════════════════════════════════╝")
                desejo = input()

                while desejo not in ['1', '2']:
                    print("╔════════════════════════════════════════════╗")
                    print("║ Opção inválida. Deseja cadastrar outro?   ║")
                    print("║ (1) Sim                                   ║")
                    print("║ (2) Não                                   ║")
                    print("╚════════════════════════════════════════════╝")
                    desejo = input()

                if desejo == '1':
                    add_pedido()
                else:
                    print("╔════════════════════════════════════════════╗")
                    print("║ Pedido cadastrado com sucesso!            ║")
                    print("╚════════════════════════════════════════════╝")
                    input("Pressione <enter> para continuar")

        elif loop == '2':
            print("╔════════════════════════════════════════════╗")
            print("║ Deseja cadastrar outro pedido?            ║")
            print("║ (1) Sim                                   ║")
            print("║ (2) Não                                   ║")
            print("╚════════════════════════════════════════════╝")
            desejo = input()

            while desejo not in ['1', '2']:
                print("╔════════════════════════════════════════════╗")
                print("║ Opção inválida. Deseja cadastrar outro?   ║")
                print("║ (1) Sim                                   ║")
                print("║ (2) Não                                   ║")
                print("╚════════════════════════════════════════════╝")
                desejo = input()

            if desejo == '1':
                add_pedido()
            else:
                print("╔════════════════════════════════════════════╗")
                print("║ Pedido cadastrado com sucesso!            ║")
                print("╚════════════════════════════════════════════╝")
                input("Pressione <enter> para continuar")
    else:
        print("╔════════════════════════════════════════════╗")
        print("║ Sem estoque para esse pedido              ║")
        print("╚════════════════════════════════════════════╝")
        input("Pressione <enter> para continuar")

def add_pedido_prato(id_pagamento):
    menu.visualizar_pratos()

    print("╔════════════════════════════════════════════╗")
    id_prato_escolhido = input("║ Digite o ID do prato: ")
    print("╠════════════════════════════════════════════╣")

    if id_prato_escolhido not in menu.menu_dados.keys():
        while id_prato_escolhido not in menu.menu_dados.keys():
            id_prato_escolhido = input("║ ID inválido. Digite um ID válido: ")
            print("╠════════════════════════════════════════════╣")

    sinal = True
    while sinal:
        try:
            quantidade_pratos = int(input("║ Digite a quantidade do pedido: "))
            sinal = False
        except ValueError:
            print("║ Valor inválido. Digite um número inteiro.")
            print("╠════════════════════════════════════════════╣")

    if verificar_estoque_prato(id_prato_escolhido, quantidade_pratos) and id_pagamentos[id_pagamento][1]:
        id_pagamentos[id_pagamento].append([id_prato_escolhido, quantidade_pratos])

        print("╔════════════════════════════════════════════╗")
        print("║ Deseja cadastrar outro prato?             ║")
        print("║ (1) Sim                                   ║")
        print("║ (2) Não                                   ║")
        print("╚════════════════════════════════════════════╝")
        loop = input()

        while loop not in ['1', '2']:
            print("╔════════════════════════════════════════════╗")
            print("║ Opção inválida. Deseja cadastrar outro?   ║")
            print("║ (1) Sim                                   ║")
            print("║ (2) Não                                   ║")
            print("╚════════════════════════════════════════════╝")
            loop = input()

        if loop == '1':
            add_pedido_prato(id_pagamento)
        elif loop == '2':
            print("╔════════════════════════════════════════════╗")
            print("║ Prato cadastrado com sucesso!             ║")
            print("╚════════════════════════════════════════════╝")
            input("Pressione <enter> para continuar")

    elif verificar_estoque_prato(id_prato_escolhido, quantidade_pratos) and not id_pagamentos[id_pagamento][1]:


        id_pagamentos[id_pagamento] = [id_pagamento, True, [id_prato_escolhido, quantidade_pratos]]

        print("╔════════════════════════════════════════════╗")
        print("║ Deseja cadastrar outro prato?             ║")
        print("║ (1) Sim                                   ║")
        print("║ (2) Não                                   ║")
        print("╚════════════════════════════════════════════╝")
        loop = input()

        while loop not in ['1', '2']:
            print("╔════════════════════════════════════════════╗")
            print("║ Opção inválida. Deseja cadastrar outro?   ║")
            print("║ (1) Sim                                   ║")
            print("║ (2) Não                                   ║")
            print("╚════════════════════════════════════════════╝")
            loop = input()

        if loop == '1':
            add_pedido_prato(id_pagamento)

        print("╔════════════════════════════════════════════╗")
        print("║ Prato cadastrado com sucesso!             ║")
        print("╚════════════════════════════════════════════╝")
        input("Pressione <enter> para continuar")

    else:
        print("╔════════════════════════════════════════════╗")
        print("║ Sem estoque para esse pedido              ║")
        print("╚════════════════════════════════════════════╝")
        input("Pressione <enter> para continuar")

def verificar_estoque_prato(id_prato_escolhido, quantidade_pratos) -> bool:
    id_estoque_usado_pre = menu.menu_dados[id_prato_escolhido][3]

    id_alimento_usado_final = id_estoque_usado_pre[0]
    quantidade_usado = id_estoque_usado_pre[1]

    quantidade_estoque = estoque.estoque_alimento[id_alimento_usado_final][5] * quantidade_pratos

    if quantidade_estoque >= quantidade_usado:
        return True
    else:
        return False

def pedido_somente_id_validado(id_pagamento):
    if estoque.estoque_bebida_ativa() and estoque.estoque_alimento_ativo():
        print("╔════════════════════╗")
        print("║ (1) Bebidas        ║")
        print("║ (2) Pratos         ║")
        print("╚════════════════════╝")
        loop = input('')

        if loop == '1':
            add_pedido_bebida(id_pagamento)
        elif loop == '2':
            add_pedido_prato(id_pagamento)


    elif estoque.estoque_alimento_ativo() and not estoque.estoque_bebida_ativa() and menu.verificar_existe_prato():
        print("╔══════════════════════════════════╗")
        print("║ (#) Sem estoque de bebida!      ║")
        print("║ (2) Pratos                      ║")
        print("╚══════════════════════════════════╝")
        loop = input('')

        if loop == '2':
            add_pedido_prato(id_pagamento)

    elif estoque.estoque_bebida_ativa() and not menu.verificar_existe_prato():
        print("╔══════════════════════════════════════╗")
        print("║ (1) Bebidas                         ║")
        print("║ (#) Sem prato cadastrado!          ║")
        print("╚══════════════════════════════════════╝")

        loop = input('')

        if loop == '1':
            add_pedido_bebida(id_pagamento)

def mostrar_id_pagamento():
    print("╔══════════════════════╗")
    print("║   ID DE PAGAMENTOS   ║")
    print("╠══════════════════════╣")
    for id_pagamento in id_pagamentos:
        print(f"║ ID: {id_pagamentos[id_pagamento][0]:<16}║")
    print("╚══════════════════════╝")

def mostrar_id_disponivel():
    for id_disponivel in id_pagamentos:
        if not id_pagamentos[id_disponivel][1]:
            print(id_pagamentos[id_disponivel][0])

def add_pedido():
    if estoque.estoque_bebida_ativa() or menu.verificar_existe_prato():

        if not id_pagamentos:
            print("╭────────────────────────────────────────────────────────╮")
            print("│ ⚠ Ainda não há ID de pagamento cadastrado no sistema! │")
            print("╰────────────────────────────────────────────────────────╯")
            input("╭────────────────────────────────────────────────────────╮\n"
                  "│ Pressione <enter> para adicionar...                    │\n"
                  "╰────────────────────────────────────────────────────────╯")
            adicionar_id_pagamento_novo()

        mostrar_id_pagamento()

        id_pagamento = input(
            "╭────────────────────────────────────────────────────────╮\n"
            "│ Digite o ID de pagamento para o pedido:                │\n"
            "╰────────────────────────────────────────────────────────╯\n➤ ")

        while id_pagamento not in id_pagamentos:
            id_pagamento = input(
                "╭────────────────────────────────────────────────────────╮\n"
                "│ ID inválido. Digite um ID de pagamento válido:         │\n"
                "╰────────────────────────────────────────────────────────╯\n➤ ")

        clientes.mostrar_clientes_ativos()
        if not clientes.verificar_clientes_ativos():
            input(
                "╭────────────────────────────────────────────────────────╮\n"
                "│ Não possui clientes no sistema. <Enter> para cadastrar │\n"
                "╰────────────────────────────────────────────────────────╯\n➤ ")
            clientes.cadastrar_cliente()

        clientes.mostrar_clientes_ativos()
        cliente = input(
            "╭────────────────────────────────────────────────────────╮\n"
            "│ Selecione o cliente vinculado ao ID de pagamento:      │\n"
            "╰────────────────────────────────────────────────────────╯\n➤ ")

        while cliente not in clientes.clientes_dados.keys():
            cliente = input(
                "╭────────────────────────────────────────────────────────╮\n"
                "│ Cliente inválido. Digite um nome válido:               │\n"
                "╰────────────────────────────────────────────────────────╯\n➤ ")

        pedido_somente_id_validado(id_pagamento)

        id_pagamentos[id_pagamento].append(clientes.clientes_dados[cliente][1])

    else:
        print("╭────────────────────────────────────────────────────────╮")
        print("│ ⚠ Nenhum prato ou bebida disponível no sistema!        │")
        print("╰────────────────────────────────────────────────────────╯")
        input("╭────────────────────────────────────────────────────────╮\n"
              "│ Pressione <enter> para continuar...                    │\n"
              "╰────────────────────────────────────────────────────────╯")

def verificar_algum_id_ativo() -> bool:
    ativo = False
    for id_pagamento in id_pagamentos:
        if id_pagamentos[id_pagamento][1]:
            ativo = True
    return ativo

def mostrar_id_e_pedidos():
    if verificar_algum_id_ativo():
        print("╔════════════════════════════════════╗")
        print("║      ID DE PAGAMENTO ATIVOS        ║")
        print("╠════════════════════════════════════╣")
        for id_pagamento in id_pagamentos:
            if id_pagamentos[id_pagamento][1]:
                for u in range(len(id_pagamentos[id_pagamento])):
                    print(f" {id_pagamentos[id_pagamento][u]}")
                print("╠════════════════════════════════════╣")
        print("╚════════════════════════════════════╝")
        input('Pressione <enter> para continuar')
    else:
        print("╔════════════════════════════════════╗")
        print("║     Nenhum ID com pedido ativo!    ║")
        print("╚════════════════════════════════════╝")
        input('Pressione <enter> para continuar')