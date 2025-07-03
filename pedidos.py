import menu
import estoque
import clientes
from clientes import mostrar_clientes_ativos

pedidos_dados =  {

}


def verificar_pedido_ativo():
    for pedido in pedidos_dados:
        if pedidos_dados[pedido][2]:
            return True
        else:
            return False


def verifica_estoque_prato(id_prato_escolhido):
    id_estoque_usado_pre = menu.menu_dados[id_prato_escolhido][3]

    id_alimento_usado_final = id_estoque_usado_pre[0]
    quantidade_usado = id_estoque_usado_pre[1]

    quantidade_estoque = estoque.estoque_alimento[id_alimento_usado_final][5]

    if quantidade_estoque >= quantidade_usado:
        return True
    else:
        return False

def adicionar_clientes_estoque_bebida():
    if clientes.verificar_clientes_ativos() and estoque.verificar_estoque_ativo_bebida():
        clientes.mostrar_clientes_ativos()
        print('==========')
        print('Digite o id do cliente: ')
        print('===========')
        input('')
        print('(1) Bebidas')

        input('')

        estoque.mostrar_bebidas_ativas()

        id_bebida = input('Digite o id da bebida: ')

        while True:
            if estoque.verificar_bebida_ativa_alvo(id_bebida):
                return False
            else:
                id_bebida = input('Digite o id válido da bebida: ')
                return True
        quantidade = int(input('Digite a quantidade da bebida: '))

        if quantidade <= estoque.estoque_bebida[id_bebida]:
            mesa = input('Digite o número do mesa: ')

            pedidos_dados[cliente_id][4] = [cliente_id, mesa, [id_bebida, quantidade]]

            print('Pedido cadastrado com sucesso!')
            input('Pressione <enter> para continuar')
        else:
            print('Sem estoque para essa bebida')
            input('Pressione <enter> para voltar ao menu')

    print('Não há clientes ou estoque para bebida !')
    input('Pressione <enter> para continuar')

def adicionar_clientes_estoque_alimento():
    if clientes.verificar_clientes_ativos() and estoque.verificar_estoque_ativo_alimento():
        clientes.mostrar_clientes_ativos()
        print('==========')
        print('Digite o id do cliente: ')
        print('===========')
        cliente_id = input('')
        print('(1) Pratos')

        input('')

        estoque.mostrar_alimentos_ativos()

        id_prato = input('Digite o id da prato: ')

        while True:
            if menu.verificar_atividade_prato(id_prato):
                loop = False
            else:
                loop = True
                id_prato = input('Digite o id válido do prato: ')

        quantidade = int(input('Digite a quantidade de pratos: '))


        if verifica_estoque_prato(id_prato):
            mesa = input('Digite o número do mesa: ')

            pedidos_dados[cliente_id][4] = [cliente_id, mesa, [id_bebida, quantidade]]

            print('Pedido cadastrado com sucesso!')
            input('Pressione <enter> para continuar')
        else:
            print('Sem estoque para esse prato')
            input('Pressione <enter> para voltar ao menu')


def adicionar_pedido():
    print('(1) Bebidas')
    print('(2) Pratos')
    op = input('Adicionar ao pedido: ')

    if op == '1':
        adicionar_clientes_estoque_bebida()

    elif op == '2':
        adicionar_clientes_estoque_alimento()



def visualizar_pedidos_ativos():
    if verificar_pedido_ativo():
        for pedido in pedidos_dados:
            if pedidos_dados[pedido][2]:
                print(f'Cliente: {pedidos_dados[pedido][0]}')
                print(f'Mesa: {pedidos_dados[pedido][1]}')
                print(f'Pedido {pedidos_dados[pedido][3]}')
                input('Pressione <enter> para voltar ao menu principal')

    else:
        print('Não há pedidos ativos no sistema.')
        input('Pressione <enter> para voltar ao menu principal')


def excluir_pedido():
    if visualizar_pedidos_ativos():
        id_desativado = input('Digite o id do pedido para ser desativado: ')
        pedidos_dados[id_desativado][2] = False
        print('Desativado com sucesso!')
        input('Pressione <enter> para voltar ao menu principal')


