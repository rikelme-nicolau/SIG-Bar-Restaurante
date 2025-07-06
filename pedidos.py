import menu
import estoque

id_pagamentos = {
    '000': ['000', False],
    '001': ['001', False],
    '002': ['002', False],
    '003': ['003', False],
    '004': ['004', False],
    '005': ['005', False],
    '006': ['006', False],
    '007': ['007', False],
    '008': ['008', False],
    '009': ['000', False],
    '010': ['010', False]
}

def add_pedido_bebida(id_pagamento):
    estoque.mostrar_bebidas_ativas()

    id_bebida = input('Digite o id da bebida: ')

    if id_bebida not in estoque.estoque_bebida:
        while id_bebida not in estoque.estoque_bebida:
            id_bebida = input('Digite um id da bebida válido: ')

    quantidade = int(input('Digite a quantidade:'))

    if estoque.estoque_bebida[id_bebida][5] >= quantidade:

        id_pagamentos[id_pagamento] = [id_pagamento, True, [id_bebida, quantidade]]
        estoque.estoque_bebida[id_bebida][5] -= quantidade

        print('Deseja cadastrar outra bebida?')
        print('(1) Sim')
        print('(2) Não')

        loop = input('')

        while loop not in ['1', '2']:
            print('Deseja cadastrar outro pedido?')
            print('(1) Sim')
            print('(2) Não')
            loop = input('')

        if loop == '1':

            while loop == '1':
                estoque.mostrar_bebidas_ativas()

                id_bebida = input('Digite o id da bebida: ')

                if id_bebida not in estoque.estoque_bebida:
                    while id_bebida not in estoque.estoque_bebida:
                        id_bebida = input('Digite um id da bebida válido: ')

                quantidade = int(input('Digite a quantidade:'))

                if estoque.estoque_bebida[id_bebida][5] >= quantidade:
                    id_pagamentos[id_pagamento].append([id_bebida, quantidade])
                    estoque.estoque_bebida[id_bebida][5] -= quantidade

                    print('Deseja cadastrar outra bebida?')
                    print('(1) Sim')
                    print('(2) Não')
                    loop = input('')

                    while loop not in ['1', '2']:
                        print('Deseja cadastrar outra bebida?')
                        print('(1) Sim')
                        print('(2) Não')
                        loop = input('')

                else:
                    print('Sem estoque para esse pedido')
                    input('Pressione <enter> para continuar')

            print('Deseja cadastrar outro pedido?')
            print('(1) Sim')
            print('(2) Não')
            desejo = input('')

            while desejo not in ['1', '2']:
                print('Deseja cadastrar outro pedido?')
                print('(1) Sim')
                print('(2) Não')

                desejo = input('')

            if desejo == '1':
                add_pedido()

            else:
                print('Pedido cadastrado com sucesso!')
                input('Pressione <enter> para continuar')

        elif loop == '2':
            print('Deseja cadastrar outro pedido?')
            print('(1) Sim')
            print('(2) Não')

            desejo = input('')

            while desejo not in ['1', '2']:
                print('Deseja cadastrar outro pedido?')
                print('(1) Sim')
                print('(2) Não')

                desejo = input('')

            if desejo == '1':
                add_pedido()
            else:
                print('Pedido cadastrado com sucesso!')
                input('Pressione <enter> para continuar')
    else:
        print('Sem estoque para esse pedido')
        input('Pressione <enter> para continuar')

def add_pedido_prato(id_pagamento):
    menu.visualizar_pratos()

    id_prato_escolhido = input('Digite o id da prato: ')
    quantidade_pratos = int(input('Digite a quantidade: '))

    if verificar_estoque_prato(id_prato_escolhido, quantidade_pratos) and id_pagamentos[id_pagamento][1] == True:
        id_pagamentos[id_pagamento].append([id_prato_escolhido, quantidade_pratos])

        print('prato cadastrado com sucesso')
        input('Pressione <enter> para continuar')

    elif verificar_estoque_prato(id_prato_escolhido, quantidade_pratos) and id_pagamentos[id_pagamento][1] == False:
        id_pagamentos[id_pagamento] = [id_pagamento, True, [id_prato_escolhido, quantidade_pratos]]

        print('prato cadastrado com sucesso')
        input('Pressione <enter> para continuar')

    else:
        print('Sem estoque para esse pedido')
        input('Pressione <enter> para continuar')

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
        print('(1) Bebidas')
        print('(2) Pratos')

        loop = input('')

        if loop == '1':
            add_pedido_bebida(id_pagamento)
        elif loop == '2':
            add_pedido_prato(id_pagamento)


    elif estoque.estoque_alimento_ativo() and not estoque.estoque_bebida_ativa() and menu.verificar_existe_prato():
        print('(#) Sem estoque de bebida!')
        print('(2) Pratos')

        loop = input('')

        if loop == '2':
            add_pedido_prato(id_pagamento)

    elif estoque.estoque_bebida_ativa() and not menu.verificar_existe_prato():
        print('(1) Bebidas')
        print('(#) Sem prato cadastrado!')

        loop = input('')

        if loop == '1':
            add_pedido_bebida(id_pagamento)

def mostrar_id_disponivel():
    for id_disponivel in id_pagamentos:
        if not id_pagamentos[id_disponivel][1]:
            print(id_pagamentos[id_disponivel][0])

def add_pedido():
    if estoque.estoque_bebida_ativa() or menu.verificar_existe_prato():

        mostrar_id_disponivel()

        id_pagamento = input('Digite o id de pagamento: ')

        if id_pagamento in id_pagamentos:
            pedido_somente_id_validado(id_pagamento)
        else:
            while id_pagamento not in id_pagamentos:
                id_pagamento = input('Digite o id de pagamento válido: ')
            pedido_somente_id_validado(id_pagamento)

    else:
        print('Nenhum prato ou bebida no sistema!')
        input('Pressione <enter> para continuar')

def verificar_algum_id_ativo() -> bool:
    ativo = False
    for id_pagamento in id_pagamentos:
        if id_pagamentos[id_pagamento][1]:
            ativo = True
    return ativo

def mostrar_id_e_pedidos():
    if verificar_algum_id_ativo():
        for id_pagamento in id_pagamentos:

            if id_pagamentos[id_pagamento][1]:
                for u in range(len(id_pagamentos[id_pagamento])):
                    print(f'{id_pagamentos[id_pagamento][u]}')

        input('Pressione <enter> para continuar')
    else:

        print('Nenhum id com pedido !')
        input('Pressione <enter> para continuar')