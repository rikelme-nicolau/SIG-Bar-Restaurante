import estoque

menu_dados = {

}


def adicionar_pratos():
    loop = 'nao'
    prato_pronto = []
    while loop != 'sim':
        estoque.mostrar_alimentos_ativos()
        id_selecionado = input('Digite o id: ')
        print(f'Digite a quantidade do id:"{id_selecionado}"\n ')
        quantidade = int(input(''))
        prato_segmento = [id_selecionado, quantidade]
        prato_pronto.append(prato_segmento)
        loop = input('Deseja finalizar o prato?: ').lower()




def menu():
    menu_select = input('')

    if menu_select == '1':
        nome = input('Qual o nome do prato?: ')

        print('=======')
        print('SELECIONE OS INGREDIENTES')
        print('=======')

        adicionar_pratos()

############def gerenciar prato
