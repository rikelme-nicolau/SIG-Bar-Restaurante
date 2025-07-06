clientes_dados = {}
atributos = {
            1: 'nome',
            2: 'CPF',
            3: 'email',
            4: 'telefone',
            5: 'nascimento'
}
def verificar_clientes_ativos():
    atividade = False
    for cliente in clientes_dados:
        if clientes_dados[cliente][6]:
            atividade = True
    return atividade

def verificar_clientes_desativados():
    atividade = False
    for cliente in clientes_dados:
        if not clientes_dados[cliente][6]:
            atividade = True
    return atividade

def mostrar_clientes_ativos():
        for cliente in clientes_dados:
            if clientes_dados[cliente][6]:
                print(f'id: {clientes_dados[cliente][0]}')
                print(f'Nome: {clientes_dados[cliente][1]}')
                print(f'CPF: {clientes_dados[cliente][2]}')
                print(f'Email: {clientes_dados[cliente][3]}')
                print(f'Telefone: {clientes_dados[cliente][4]}')
                print(f'Nascimento: {clientes_dados[cliente][5]}')

def mostrar_clientes_desativados():
            for cliente in clientes_dados:
                if not clientes_dados[cliente][6]:
                    print(f'id: {clientes_dados[cliente][0]}')
                    print(f'Nome: {clientes_dados[cliente][1]}')
                    print(f'CPF: {clientes_dados[cliente][2]}')
                    print(f'Email: {clientes_dados[cliente][3]}')
                    print(f'Telefone: {clientes_dados[cliente][4]}')
                    print(f'Nascimento: {clientes_dados[cliente][5]}')

def cadastrar_cliente():
    print('========')
    print('Cadastrar cliente')
    print('========')

    nome = input('Nome: ')
    cpf = input('CPF: ')
    email = input('Email: ')
    telefone = input('Telefone: ')
    nascimento = input('Data de Nascimento: ')

    id_cliente = str(len(clientes_dados))

    clientes_dados[id_cliente] = [id_cliente, nome, cpf, email, telefone, nascimento, True]

    print('Cliente cadastrado com sucesso!')
    input('Pressione <enter> para retornar ao menu principal')

def gerenciar_cliente():
    print('========')
    print('Gerenciar cliente')
    print('========')
    print('(1) Visualizar clientes ativos')
    print('(2) Excluir clientes')
    print('(3) Ativar clientes')
    print('(4) Alterar informação clientes')

    cliente_select = input('')

    if cliente_select == '1':
        if verificar_clientes_ativos():
            mostrar_clientes_ativos()
            input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Sem clientes ativos no momento...')
            input('Pressione <enter> para retornar ao menu principal')


    elif cliente_select == '2':
        if verificar_clientes_ativos():
            mostrar_clientes_ativos()
            selecionado = input('')
            clientes_dados[selecionado][6] = False
            print(f'Cliente {clientes_dados[selecionado][1]} foi desativado')
            input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Sem clientes ativos no momento...')
            input('Pressione <enter> para retornar ao menu principal')

    elif cliente_select == '3':
        if verificar_clientes_desativados():
            mostrar_clientes_desativados()
            id_ativar = input('Qual id do cliente que deseja ativa?: ')
            clientes_dados[id_ativar][6] = True
            print(f'Cliente ativado com sucesso!')
            input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Sem clientes ativos no momento...')
            input('Pressione <enter> para retornar ao menu principal')

    elif cliente_select == '4':
        if verificar_clientes_ativos():

            mostrar_clientes_ativos()
            selecionado = input('Digite o id do cliente: ')

            print(f'Cliente {selecionado} selecionado com sucesso!')

            print('Onde deseja fazer a alteração?')
            print('(1) Nome')
            print('(2) CPF')
            print('(3) Email')
            print('(4) Telefone')
            print('(5) Nascimento')

            alterar = int(input(''))

            print(f'Ok, digite o novo {atributos[alterar]}')
            novo = input('')
            clientes_dados[selecionado][alterar] = novo

            print('Mudança feita com sucesso!')
            input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Sem clientes ativos no momento...')
            input('Pressione <enter> para retornar ao menu principal')