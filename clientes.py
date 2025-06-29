clientes_dados = {

}

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

        clientes_dados[len(clientes_dados)] = [nome, cpf, email, telefone, nascimento, True]

    elif cliente_select == '2':
        print('========')
        print('Gerenciar cliente')
        print('========')
        print('(1) Visualizar clientes')

        cliente_select = input('')

        if cliente_select == '1':
            for cliente in clientes_dados:
                if clientes_dados[cliente][5]:
                    print(f'Nome: {cliente}')
                    print(f'CPF: {cliente}')
                    print(f'Email: {cliente}')
                    print(f'Telefone: {cliente}')
                    print(f'Nascimento: {cliente}')
                else:
                    print('Sem clientes ativos no sistema !')
                    input('<ENTER>')
