estoque_bebida = {

}

estoque_alimento = {

}


def estoque_bebida_ativa() -> bool:
    sinal = False
    for estoque in estoque_bebida:
        if estoque_bebida[estoque][6]:
            sinal = True

    return sinal


def estoque_alimento_ativo() -> bool:
    sinal = False
    for estoque in estoque_alimento:
        if estoque_alimento[estoque][6]:
            sinal = True

    return sinal


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


def mostrar_bebida_e_alimento_ativos():
    print('(1) Bebidas')
    print('(2) Alimentos')

    listagem = input('Deseja visualizar qual produto?: ')

    if listagem == '1':

        if estoque_bebida_ativa():
            mostrar_bebidas_ativas()
            input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Não possui bebidas no estoque!')
            input('Pressione <enter> para retornar ao menu principal')

    elif listagem == '2':
        if estoque_alimento_ativo():
            mostrar_alimentos_ativos()
            input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Não possui alimentos no estoque!')
            input('Pressione <enter> para retornar ao menu principal')


def adicionar_bebida_nova():
    produto = input('Digite o tipo da bebida: ').upper()
    marca = input(f'Digite a marca do {produto}: ').upper()
    capacidade = input(f'Digite os ml do {produto}: ')
    embalagem = input(f'Digite o embalagem do {produto}: ').upper()

    id = str(len(estoque_bebida))

    estoque_bebida[id] = [id, produto, marca, capacidade, embalagem, 0, True]

    print('bebida cadastrada com sucesso!')
    input('Pressione <enter> para retornar ao menu principal')


def adicionar_alimento_novo():
    produto = input('Digite o tipo de alimento: ').upper()
    marca = input(f'Digite a marca do {produto}: ').upper()
    capacidade = input(f'Digite os gramas do {produto}: ')
    embalagem = input(f'Digite o embalagem do {produto}: ').upper()

    id = str(len(estoque_alimento))

    estoque_alimento[id] = [id, produto, marca, capacidade, embalagem, 0, True]

    print('alimento cadastrado com sucesso!')
    input('Pressione <enter> para retornar ao menu principal')


def subtrair_produtos_bebidas():
    if estoque_bebida_ativa():

        mostrar_bebidas_ativas()

        id_selecionado = input('Digite o id do produto: ')
        saida = int(input('Digite a quatidade de saída do produto: '))

        if saida <= estoque_bebida[id_selecionado][5]:
            estoque_bebida[id_selecionado][5] -= saida
        elif saida > estoque_bebida[id_selecionado][5]:
            while saida > estoque_bebida[id_selecionado][5]:
                print('Essa bebida não possui esse estoque para retirada!')
                print(f'Selecione um valor de saída entre 0 e {estoque_bebida[id_selecionado][5]}')
                saida = input('')
            estoque_bebida[id_selecionado][5] -= saida
    else:
        print('Não há nenhuma bebida ativa no estoque!')
        input('Pressione <enter> para retornar ao menu principal')

    print(f'Saída com sucesso!')
    print(
        f'Agora o produto id:{estoque_bebida[id_selecionado][0]} possui {estoque_bebida[id_selecionado][5]} produtos em estoque')
    input('Pressione <enter> para retornar ao menu principal')


def subtrair_produtos_alimentos():
    if estoque_alimento_ativo():

        mostrar_alimentos_ativos()

        id_selecionado = input('Digite o id do produto: ')
        saida = int(input('Digite a quatidade de saída do produto: '))

        if saida <= estoque_alimento[id_selecionado][5]:
            estoque_alimento[id_selecionado][5] -= saida

            print(f'Saída com sucesso!')
            print(
                f'Agora o produto id:"{estoque_alimento[id_selecionado][0]}" possui {estoque_bebida[id_selecionado][5]} produtos em estoque')
            input('Pressione <enter> para retornar ao menu principal')

        elif saida > estoque_alimento[id_selecionado][5]:
            while saida > estoque_alimento[id_selecionado][5]:
                print('Esse alimento não possui esse estoque para retirada!')
                print(f'Selecione um valor de saída entre 0 e {estoque_alimento[id_selecionado][5]}')
                saida = input('')

            estoque_alimento[id_selecionado][5] -= saida

            print(f'Saída com sucesso!')
            print(
                f'Agora o produto id:"{estoque_alimento[id_selecionado][0]}" possui {estoque_bebida[id_selecionado][5]} produtos em estoque')
            input('Pressione <enter> para retornar ao menu principal')

    else:
        print('Não há nenhum alimento ativo no estoque!')
        input('Pressione <enter> para retornar ao menu principal')

    print(f'Saída com sucesso!')
    print(
        f'Agora o produto id:"{estoque_alimento[id_selecionado][0]}" possui {estoque_bebida[id_selecionado][5]} produtos em estoque')
    input('Pressione <enter> para retornar ao menu principal')


def entrada_de_produtos():
    print('=======')
    print('ENTRADA DE PRODUTOS')
    print('=======')
    print('(1) Bebida')
    print('(2) Alimentos\n')

    tipo = input('')

    if tipo == '1':
        if estoque_bebida_ativa():
            mostrar_bebidas_ativas()

            id_selecionado = input('Digite o id do produto: ')
            entrada = int(input('Digite a quatidade de entrada do produto: '))
            estoque_bebida[id_selecionado][5] += entrada

            print(
                f'Adicionado com sucesso!\n Agora o produto id:"{estoque_bebida[id_selecionado][0]}" possui {estoque_bebida[id_selecionado][5]} produtos em estoque.')
            input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Não há nenhuma bebida ativa no estoque!')
            input('Pressione <enter> para retornar ao menu principal')


    elif tipo == '2':
        if estoque_alimento_ativo():
            mostrar_alimentos_ativos()

            id_selecionado = input('Digite o id do produto: ')
            entrada = int(input('Digite a quatidade de entrada do produto: '))
            estoque_alimento[id_selecionado][5] += entrada

            print(
                f'Adicionado com sucesso!\nAgora o produto id:"{estoque_alimento[id_selecionado][0]}" possui {estoque_alimento[id_selecionado][5]} produtos em estoque.')
            input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Não há nenhum alimento ativo no estoque!')
            input('Pressione <enter> para retornar ao menu principal')


def saida_de_produtos():
    print('=======')
    print('SAÍDA DE PRODUTOS')
    print('=======')
    print('(1) Bebida')
    print('(2) Alimentos')

    tipo = input('')

    if tipo == '1':
        subtrair_produtos_bebidas()

    elif tipo == '2':
        subtrair_produtos_alimentos()