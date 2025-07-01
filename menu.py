import estoque



menu_dados = {

}

def verificar_existe_prato():
    verificar = False
    for prato in menu_dados:
        if menu_dados[prato][0]:
            verificar = True
    return verificar

def cadastrar_prato():
    if estoque.verificar_estoque_ativo_alimento():
        estoque.mostrar_alimentos_ativos()
        nome = input("Digite o nome do prato: ").upper()

        alimento = input("Digite o id alimento: ")
        quantidade = int(input("Digite o quantidade usada no prato: "))

        id_prato = str(len(menu_dados))
        menu_dados[id_prato] = [True, [alimento, quantidade]]

        print(f'{estoque.estoque_alimento[alimento][1]} foi adicionado ao {nome} utilizando {quantidade} gramas.')
        loop = input('Deseja adicionar mais algum alimento ao prato?')


        while loop == 'sim':
            if estoque.verificar_estoque_ativo_alimento():
                estoque.mostrar_alimentos_ativos()

                alimento = input("Digite o id alimento: ")
                quantidade = int(input("Digite o quantidade usada no prato: "))

                menu_dados[id_prato].update([alimento, quantidade])
                print(f'{estoque.estoque_alimento[alimento][2]} foi adicionado ao {nome} utilizando {quantidade} gramas.')
                loop = input('Deseja adicionar mais algum alimento ao prato?')

        print('Prato cadastrado com sucesso!')
        input('Pressione <enter> para continuar')

    else:
        print('Nenhum alimento no estoque!')
        input('Pressione <enter> para continuar')