import menu
import estoque
pedidos_dados =  {

}


def verifica_estoque_pedido(id_prato_escolhido):
    id_estoque_usado_pre = menu.menu_dados[id_prato_escolhido][3]

    id_alimento_usado_final = id_estoque_usado_pre[0]
    quantidade_usado = id_estoque_usado_pre[1]

    quantidade_estoque = estoque.estoque_alimento[id_alimento_usado_final][5]

    if quantidade_estoque >= quantidade_usado:
        return True
    else:
        return False


def adicionar_pedido():
    if menu.verificar_existe_prato():
        menu.visualizar_pratos()
        prato_escolhido = input('Digite o id prato: ')
        if verifica_estoque_pedido(prato_escolhido):
            id_pedido = str(len(pedidos_dados))
            pedidos_dados[id_pedido] = [id_pedido, prato_escolhido]
            print('Pedido cadastrado com sucesso!')
            input('Pressione <ENTER> para voltar ao menu')
        else:
            print('Não há estoque para esse prato!')
            input('Pressione <ENTER> para voltar ao menu')
    else:
        print('Nenhum prato ativo no sistema!')
        input('Pressione <ENTER> para ir ao menu principal')