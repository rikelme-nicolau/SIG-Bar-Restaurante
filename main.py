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

    print("==========\n")

    loop_menu = input()

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

        estoque.produtos()

    elif loop_menu == '3':
        print("==========")
        print(" CLIENTES ")
        print("==========")

        print('(1) Cadastrar cliente')
        print('(2) Gerenciar cliente\n')

        clientes.clientes()

    elif loop_menu == '4':
        print("==========")
        print(" RH ")
        print("==========")

        print('(1) Cadastrar funcionário')
        print('(2) Gerenciar funcionário')

        rh.rh_modulo()

    elif loop_menu == '5':
        print("==========")
        print(" MENU ")
        print("==========")

        print('(1) Cadastrar prato')
        print('(2) Gerenciar prato\n')

        menu.menu()
