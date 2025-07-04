import menu
import estoque

mesas = {
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


def add_pedido_bebida(mesa):
    estoque.mostrar_bebidas_ativas()
    id_bebida = input('Digite o id da bebida: ')
    quantidade = int(input('Digite a quantidade:'))

    if estoque.estoque_bebida[id_bebida][5] >= quantidade:

        mesas[mesa] = [mesa, True, [id_bebida, quantidade]]
        loop = input('deseja cadastrar outra bebida ?')
        if loop == 'sim':
            while loop == 'sim':
                estoque.mostrar_bebidas_ativas()
                id_bebida = input('Digite o id da bebida: ')
                quantidade = int(input('Digite a quantidade:'))
                mesas[mesa].append([id_bebida, quantidade])
                loop = input('deseja cadastrar outra bebida ?')
        else:
            desejo = input('Deseja cadastrar outro pedido?: ').lower
            if desejo == 'sim':
                return add_pedido()

    else:
        print('Sem estoque para esse pedido')
        input('Pressione <enter> para continuar')


def verificar_estoque_prato(id_prato_escolhido) -> bool:
    id_estoque_usado_pre = menu.menu_dados[id_prato_escolhido][3]

    id_alimento_usado_final = id_estoque_usado_pre[0]
    quantidade_usado = id_estoque_usado_pre[1]

    quantidade_estoque = estoque.estoque_alimento[id_alimento_usado_final][5]

    if quantidade_estoque >= quantidade_usado:
        return True
    else:
        return False


def add_pedido():
    if estoque.estoque_bebida_ativa() or menu.verificar_existe_prato():
        print('000  001  002\n  003  004  005\n  006  007  008\n  009  010')
        mesa = input('Digite o id da mesa: ?')
        if estoque.estoque_bebida_ativa() and estoque.estoque_alimento_ativo():
            print('(1) Bebidas')
            print('(2) Pratos')

            loop = input('')

            if loop == '1':
                add_pedido_bebida(mesa)

        elif estoque.estoque_alimento_ativo() and not estoque.estoque_bebida_ativa() and menu.verificar_existe_prato():
            print('(#) Sem estoque de bebida!')
            print('(2) Pratos')

            input('Pressione <enter> para continuar')
        elif estoque.estoque_bebida_ativa() and not menu.verificar_existe_prato():
            print('(1) Bebidas')
            print('(#) Sem prato cadastrado!')

            loop = input('')
            if loop == '1':
                add_pedido_bebida(mesa)


    else:
        print('Nenhum prato ou bebida no sistema!')
        input('Pressione <enter> para continuar')


def verificar_alguma_mesa_ativa() -> bool:
    ativo = False
    for mesa in mesas:
        if mesas[mesa][1]:
            ativo = True
    return ativo


def mostrar_mesas_e_pedidos():
    if verificar_alguma_mesa_ativa():
        for mesa in mesas:
            if mesas[mesa][1]:
                print(f'id: {mesa}')
                print(f'pedido: {mesas[mesa][2]}')
                input('Pressione <enter> para continuar')

    else:
        print('Nenhuma mesa com pedido !')
        input('Pressione <enter> para continuar')