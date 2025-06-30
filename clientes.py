clientes_dados = {

}




def mostrar_clientes_ativos():
    atividade = 0
    for cliente in clientes_dados:
        if clientes_dados[cliente][5]:
            atividade += 1
    if atividade > 0:
        for cliente in clientes_dados:
            if clientes_dados[cliente][5]:
                print(f'id: {clientes_dados[cliente][0]}')
                print(f'Nome: {clientes_dados[cliente][1]}')
                print(f'CPF: {clientes_dados[cliente][2]}')
                print(f'Email: {clientes_dados[cliente][3]}')
                print(f'Telefone: {clientes_dados[cliente][4]}')
                print(f'Nascimento: {clientes_dados[cliente][5]}')
    else:
        print('Nenhum cliente ativo no sistema!')
        input('Pressione <enter> para continuar')



def clientes():

    cliente_select = input('')

    if cliente_select == '1':
        print('========')
        print('Cadastrar cliente')
        print('========')
        nome = input('Nome: ')
        cpf = input('CPF: ')
        email = input('Email: ')
        telefone = input('Telefone: ')
        nascimento = input('Data de Nascimento xx/xx/xxxx: ')

        id_cliente = str(len(clientes_dados))

        clientes_dados[id_cliente] = [id_cliente, nome, cpf, email, telefone, nascimento, True]

    elif cliente_select == '2':
        print('========')
        print('Gerenciar cliente')
        print('========')
        print('(1) Visualizar clientes ativos')
        print('(2) Excluir clientes')
        print('(3) Ativar clientes')

        cliente_select = input('')

        if cliente_select == '1':
            mostrar_clientes_ativos()

        elif cliente_select == '2':
            mostrar_clientes_ativos()
            selecionado = input('')
            clientes_dados[selecionado][6] = False
            print(f'Cliente {clientes_dados[selecionado][1]} foi desativado')
            input('<ENTER>')

        elif cliente_select == '3':
            atividade = 0
            for cliente in clientes_dados:
                if clientes_dados[cliente][5] == False:
                    atividade += 1

            if atividade > 0:
                for cliente in clientes_dados:
                    if clientes_dados[cliente][5] == False:
                        print(f'id: {clientes_dados[cliente][0]}')
                        print(f'Nome: {clientes_dados[cliente][1]}')
                        print(f'CPF: {clientes_dados[cliente][2]}')
                        print(f'Email: {clientes_dados[cliente][3]}')
                        print(f'Telefone: {clientes_dados[cliente][4]}')
                        print(f'Nascimento: {clientes_dados[cliente][5]}')
            else:
                print('Nenhum cliente desativado no sistema!')
                input('Pressione <enter> para continuar')



