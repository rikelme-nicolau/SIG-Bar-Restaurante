rh_dados = {

            }

cargos = {
    '1': 'Cozinheiro',
    '2': 'Garçom',
    '3': 'Barman',
    '4': 'Balconista',
    '5': 'Gerente'
            }

def rh_modulo():

    rh_select = input('')
    
    if rh_select == '1':

        nome = input('Digite o nome do funcionário?\n')
        data_nascimento = input('Digite a data de nascimento no formato xx/xx/xxxx\n')
        cpf = input('Digite o cpf no formato xxx.xxx.xxx-xx\n')
        
        cargo = input('Qual o cargo exercido\n'
        '(1) Cozinheiro\n'
        '(2) Garçom\n'
        '(3) Barman\n'
        '(4) Balconista\n'
        '(5) Gerente\n')

        rh_dados[str(len(rh_dados))] = [nome, data_nascimento, cpf, cargos[cargo], True]

        print('Funcionário cadastrado com sucesso!')
        input('Pressione <enter> para retornar ao menu principal')

    elif rh_select == '2':

        print("==========")
        print(" RH | Gerenciar ")
        print("==========")

        print('(1) Visualizar funcionarios')
        print('(2) Excluir funcionarios\n')

        rh_select = input('')

        if rh_select == '1':

            for funcionario in rh_dados:
                if rh_dados[funcionario][4]:
                    print(rh_dados[funcionario][0])
                    print(rh_dados[funcionario][1])
                    print(rh_dados[funcionario][2])
                    print(rh_dados[funcionario][3])
                    print(rh_dados[funcionario][4])
                    print(len(rh_dados))

            input('Pressione <enter> para retornar ao menu principal')

        elif rh_select == '2':

            for funcionario in rh_dados:
                print(f'({len(rh_dados) - 1}) {rh_dados[funcionario][0]}')

            desativar = input('')
            rh_dados[desativar][4] = False

            print('Funcionário desativado!')
            input('Pressione <enter> para retornar ao menu principal')