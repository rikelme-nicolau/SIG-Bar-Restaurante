
estoque_bebida = {

}
estoque_alimento = {

}

def produtos():
    print("==========")
    print("GERENCIAR PEDIDOS")
    print("==========")

    print('(1) Adicionar produto novo')
    print('(2) Listar produtos')
    print('(3) Entrada de produto')
    print('(4) Saída de produto')

    menu_select = input('')

    if menu_select == '1':

        print('Qual tipo de produto?')
        print('(1) Bebida')
        print('(2) Alimento\n')
        tipo = input('')

        if tipo == '1':
            produto = input('Digite o tipo do alimento: ').upper()
            marca = input(f'Digite a marca do {produto}: ').upper()
            capacidade = input(f'Digite os ml do {produto}: ')
            embalagem = input(f'Digite o embalagem do {produto}: ').upper()

            estoque_bebida[str(len(estoque_bebida))] = [produto, marca,  capacidade, embalagem, 0, True]

        elif tipo == '2':
            produto = input('Digite o tipo de alimento: ').upper()
            marca = input(f'Digite a marca do {produto}: ').upper()
            capacidade = input(f'Digite os gramas do {produto}: ')
            embalagem = input(f'Digite o embalagem do {produto}: ').upper()

            estoque_alimento[str(len(estoque_bebida))] = [produto, marca, capacidade, embalagem, 0, True]

    elif menu_select == '2':
        listagem = input('Deseja visualizar qual produto ?')

        print('(1) Bebidas')
        print('(2) Alimentos\n')

        if listagem == '1':
            for bebida in estoque_bebida:
                print(f'PRODUTO: {estoque_bebida[bebida][0]}')
                print(f'MARCA: {estoque_bebida[bebida][1]}')
                print(f'CAPACIDADE: {estoque_bebida[bebida][2]}')
                print(f'EMABALAGEM: {estoque_bebida[bebida][3]}')
                print(f'QUANTIDADE: {estoque_bebida[bebida][4]}\n')

        elif listagem == '2':
            for alimento in estoque_alimento:
                print(f'PRODUTO: {estoque_alimento[alimento][0]}')
                print(f'MARCA: {estoque_alimento[alimento][1]}')
                print(f'CAPACIDADE: {estoque_bebida[alimento][2]}')
                print(f'EMABALAGEM: {estoque_bebida[alimento][3]}')
                print(f'QUANTIDADE: {estoque_bebida[alimento][4]}\n')

