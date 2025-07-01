import rh
import menu
import estoque
import clientes

loop_menu = ''

while loop_menu != '6':
    print("==========")
    print(" SIG-Bar ")
    print("==========")
    print("(1) Acesso aos pedidos")
    print("(2) Acesso ao estoque")
    print("(3) Acesso aos clientes")
    print("(4) Acesso ao RH")
    print("(5) Acesso ao menu")
    print("(6) Sair")
    print("==========")

    loop_menu = input('')

    if loop_menu == '1':
        print("==========")
        print(" PEDIDOS ")
        print("==========")
        print('(1) Adicionar pedido')
        print('(2) Gerenciar pedido')

    elif loop_menu == '2':
        print("==========")
        print(" ESTOQUE ")
        print("==========")
        print('(1) Adicionar produto novo')
        print('(2) Listar produtos')
        print('(3) Entrada de produto')
        print('(4) Saída de produto')

        loop_menu = input('')

        if loop_menu == '1':
            estoque.adicionar_produtos_novos()
        elif loop_menu == '2':
            estoque.visualizar_produtos_ativos()
        elif loop_menu == '3':
            estoque.entrada_de_produtos()
        elif loop_menu == '4':
            estoque.saida_de_produtos()

    elif loop_menu == '3':
        print("==========")
        print(" CLIENTES ")
        print("==========")
        print('(1) Cadastrar cliente')
        print('(2) Gerenciar cliente')

        loop_menu = input('')

        if loop_menu == '1':
            clientes.cadastrar_cliente()
        elif loop_menu == '2':
            clientes.gerenciar_cliente()

    elif loop_menu == '4':
        print("==========")
        print(" RH ")
        print("==========")
        print('(1) Cadastrar funcionário')
        print('(2) Gerenciar funcionário')

        loop_menu = input('')

        if loop_menu == '1':
            rh.cadastrar_funcionario()
        elif loop_menu == '2':
            rh.gerenciar_funcionario()

    elif loop_menu == '5':
        print("==========")
        print(" MENU ")
        print("==========")
        print('(1) Cadastrar prato')
        print('(2) Gerenciar prato\n')

        menu.menu()

