import menu

pedidos_dados =  {

}
def adicionar_pedido():
    if menu.verificar_existe_prato():
        ##verificar qual prato
        ##verificar se há estoque
        ##adicionar informação de cliente e mesa
    else:
        print('Nenhum prato ativo no sistema!')
        input('Pressione <ENTER> para ir ao menu principal')
