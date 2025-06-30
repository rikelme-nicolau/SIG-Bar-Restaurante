estoque_bebida = {

}

estoque_alimento = {

}

def mostrar_bebidas_ativas():
    for bebida in estoque_bebida:
        if estoque_bebida[bebida][6]:
            print(f'id: {estoque_bebida[bebida][0]}')
            print(f'PRODUTO: {estoque_bebida[bebida][1]}')
            print(f'MARCA: {estoque_bebida[bebida][2]}')
            print(f'CAPACIDADE: {estoque_bebida[bebida][3]}')
            print(f'EMBALAGEM: {estoque_bebida[bebida][4]}')
            print(f'QUANTIDADE: {estoque_bebida[bebida][5]}\n')

def mostrar_alimentos_ativos():
    for alimento in estoque_alimento:
        if estoque_alimento[alimento][6]:
            print(f'ID: {estoque_alimento[alimento][0]}')
            print(f'PRODUTO: {estoque_alimento[alimento][1]}')
            print(f'MARCA: {estoque_alimento[alimento][2]}')
            print(f'CAPACIDADE: {estoque_alimento[alimento][3]}')
            print(f'EMBALAGEM: {estoque_alimento[alimento][4]}')
            print(f'QUANTIDADE: {estoque_alimento[alimento][5]}\n')

def produtos():

    print('(1) Adicionar produto novo')
    print('(2) Listar produtos')
    print('(3) Entrada de produto')
    print('(4) Saída de produto')

    menu_select = input('')

    if menu_select == '1':

        print('Qual tipo de produto?')
        print('(1) Bebida')
        print('(2) Alimento')
        tipo = input('')

        if tipo == '1':
            produto = input('Digite o tipo da bebida: ').upper()
            marca = input(f'Digite a marca do {produto}: ').upper()
            capacidade = input(f'Digite os ml do {produto}: ')
            embalagem = input(f'Digite o embalagem do {produto}: ').upper()

            id = str(len(estoque_bebida))

            estoque_bebida[id] = [id, produto, marca,  capacidade, embalagem, 0, True]

            print('bebida cadastrada com sucesso!')
            input('Pressione <enter> para retornar ao menu principal')

        elif tipo == '2':
            produto = input('Digite o tipo de alimento: ').upper()
            marca = input(f'Digite a marca do {produto}: ').upper()
            capacidade = input(f'Digite os gramas do {produto}: ')
            embalagem = input(f'Digite o embalagem do {produto}: ').upper()

            id = str(len(estoque_alimento))

            estoque_alimento[id] = [id, produto, marca, capacidade, embalagem, 0, True]

            print('alimento cadastrado com sucesso!')
            input('Pressione <enter> para retornar ao menu principal')

    elif menu_select == '2':
        print('(1) Bebidas')
        print('(2) Alimentos')

        listagem = input('Deseja visualizar qual produto ?')

        if listagem == '1':
            mostrar_bebidas_ativas()

        elif listagem == '2':
            mostrar_alimentos_ativos()

    elif menu_select == '3':
        print('=======')
        print('ENTRADA DE PRODUTOS')
        print('=======')
        print('(1) Bebida')
        print('(2) Alimentos\n')

        tipo = input('')

        if tipo == '1':
            mostrar_bebidas_ativas()

            id_selecionado = input('Digite o id do produto: ')
            entrada = int(input('Digite a quatidade de entrada do produto: '))
            estoque_bebida[id_selecionado][5] += entrada

            print(f'Adicionado com sucesso!\n Agora o produto id:"{estoque_bebida[id_selecionado][0]}" possui {estoque_bebida[id_selecionado][5]} produtos em estoque.')
            input('Pressione <enter> para retornar ao menu principal')

        elif tipo == '2':
            mostrar_alimentos_ativos()

            id_selecionado = input('Digite o id do produto: ')
            entrada = int(input('Digite a quatidade de entrada do produto: '))
            estoque_alimento[id_selecionado][5] += entrada

            print(f'Adicionado com sucesso!\n Agora o produto id:"{estoque_alimento[id_selecionado][0]}" possui {estoque_alimento[id_selecionado][5]} produtos em estoque.')
            input('Pressione <enter> para retornar ao menu principal')
