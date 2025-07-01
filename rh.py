rh_dados = {

}

cargos = {
    '1': 'Cozinheiro',
    '2': 'Garçom',
    '3': 'Barman',
    '4': 'Balconista',
    '5': 'Gerente'
            }

def verificar_funcionario_ativo():
    verificar = False
    for funcionario in rh_dados:
        if rh_dados[funcionario][5]:
            verificar = True
    return verificar

def verificar_funcionario_desativado():
    verificar = False
    for funcionario in rh_dados:
        if not rh_dados[funcionario][5]:
            verificar = True
    return verificar

def cadastrar_funcionario():

    print('==========')
    print('Cadastrar funcionario')
    print('==========')


    nome = input('Digite o nome do funcionário?: ')
    data_nascimento = input('Digite a data de nascimento no formato: ')
    cpf = input('Digite o cpf no formato: ')

    cargo = input('Qual o cargo exercido\n'
                  '(1) Cozinheiro\n'
                  '(2) Garçom\n'
                  '(3) Barman\n'
                  '(4) Balconista\n'
                  '(5) Gerente\n')

    id_funcionario = str(len(rh_dados))

    rh_dados[id_funcionario] = [id_funcionario, nome, data_nascimento, cpf, cargos[cargo], True]

    print('Funcionário cadastrado com sucesso!')
    input('Pressione <enter> para retornar ao menu principal')


def gerenciar_funcionario():
    print("==========")
    print(" RH | Gerenciar ")
    print("==========")
    print('(1) Visualizar funcionarios')
    print('(2) Desativar funcionarios')
    print('(3) Ativar funcionarios')

    rh_select = input('')

    if rh_select == '1':
        if verificar_funcionario_ativo():
            for funcionario in rh_dados:
                if rh_dados[funcionario][4]:
                    print(rh_dados[funcionario][0])
                    print(rh_dados[funcionario][1])
                    print(rh_dados[funcionario][2])
                    print(rh_dados[funcionario][3])
                    print(rh_dados[funcionario][4])
                    print(len(rh_dados))

                    print()
                    input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Ainda não há funcionários ativos!')
            input('Pressione <enter> para retornar ao menu principal')

    elif rh_select == '2':
        if verificar_funcionario_ativo():
            for funcionario in rh_dados:
                if rh_dados[funcionario][5]:
                    print(rh_dados[funcionario][0])
                    print(rh_dados[funcionario][1])

                id_desativar = input('digite o id do funcionário que deseja desativar!')
                rh_dados[id_desativar][5] = False

                print(f'funcionário {id_desativar} desativado!')
                input('Pressione <enter> para retornar ao menu principal')
        else:
            print('Ainda não há funcionários ativos!')
            input('Pressione <enter> para retornar ao menu principal')

    elif rh_select == '3':
        if verificar_funcionario_desativado():
            for funcionario in rh_dados:
                if not rh_dados[funcionario][5]:
                    print(rh_dados[funcionario][0])
                    print(rh_dados[funcionario][1])

                    id_ativar = input('digite o id do funcionário que deseja ativar!')
                    rh_dados[id_ativar][5] = True

                    print(f'funcionário {id_ativar} ativado!')
                    input('Pressione <enter> para retornar ao menu principal')

        else:
            print('Ainda não há funcionários desativados!')
            input('Pressione <enter> para retornar ao menu principal')