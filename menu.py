import estoque

menu_dados = {


}

def verificar_atividade_prato(alvo):
    if menu_dados[alvo][0]:
        return True
    else:
        return False




def verificar_pratos_ativos():
    verificar = False
    for prato in menu_dados:
        if menu_dados[prato][0]:
            verificar = True
    return verificar

def visualizar_pratos_ativos():
     for prato in menu_dados:
         if menu_dados[prato][0]:
             print(menu_dados[prato][1])
             print(menu_dados[prato][2])

def cadastrar_prato():
    if estoque.verificar_estoque_ativo_alimento():
        estoque.mostrar_alimentos_ativos()
        nome = input("Digite o nome do prato: ").upper()

        alimento = input("Digite o id alimento: ")
        quantidade = int(input("Digite o quantidade usada no prato: "))

        id_prato = str(len(menu_dados))
        menu_dados[id_prato] = [True, id_prato, nome, [alimento, quantidade]]

        print(f'{estoque.estoque_alimento[alimento][1]} foi adicionado ao {nome} utilizando {quantidade} gramas.')
        loop = input('Deseja adicionar mais algum alimento ao prato?')


        while loop == 'sim':
            if estoque.verificar_estoque_ativo_alimento():
                estoque.mostrar_alimentos_ativos()

                alimento = input("Digite o id alimento: ")
                quantidade = int(input("Digite o quantidade usada no prato: "))

                menu_dados[id_prato].append([alimento, quantidade])
                print(f'{estoque.estoque_alimento[alimento][2]} foi adicionado ao {nome} utilizando {quantidade} gramas.')
                loop = input('Deseja adicionar mais algum alimento ao prato?')

        print(menu_dados)
        print('Prato cadastrado com sucesso!')
        input('Pressione <enter> para continuar')

    else:
        print('Nenhum alimento no estoque!')
        input('Pressione <enter> para continuar')