import menu
import estoque
import clientes
from clientes import mostrar_clientes_ativos

pedidos_dados =  {

}


def verifica_estoque_pedido(id_prato_escolhido):
    id_estoque_usado_pre = menu.menu_dados[id_prato_escolhido][3]

    id_alimento_usado_final = id_estoque_usado_pre[0]
    quantidade_usado = id_estoque_usado_pre[1]

    quantidade_estoque = estoque.estoque_alimento[id_alimento_usado_final][5]

    if quantidade_estoque >= quantidade_usado:
        return True
    else:
        return False


def adicionar_pedido():
    if clientes.verificar_clientes_ativos():
        clientes.mostrar_clientes_ativos()
        print('===========')
        cliente = input("Digite o id do cliente: ")
        print('===========')
        print(f'Cliente: {cliente}')
        print('Deseja cadastrar: ')
        print('(1) Bebidas')
        print('(2) Pratos')
        cadastro = input('')


        if cadastro == '1' and estoque.verificar_estoque_ativo_bebida():
            loop = 'sim'
            while loop == 'sim':
                estoque.mostrar_bebidas_ativas()
                id_bebida = input('Digite o id da bebida: ')
                quantidade_bebida = int(input('Digite a quantidade da bebida: '))
                if quantidade_bebida <= estoque.estoque_bebida[id_bebida][5]:
                    pedidos_dados[cliente] = [cliente, [id_bebida, quantidade_bebida, quantidade_bebida]]
                    print(f'Cliente {cliente}: {id_bebida} ')
                    print('Pedido cadastrado com sucesso!')
                    loop = input('Deseja adicionar alguma outra bebida? : ')
                else:
                    print('Não possui estoque para esse pedido.')
                    loop = input('Deseja adicionar alguma outra bebida? : ')

                input('Pressione <enter> para voltar ao menu!')

            print('Pedido cadastrado com sucesso!')
            input('Pressione <enter> para continuar')

        else:
            print('Nenhuma bebida ativa no sistema!')
            input('Pressione <ENTER> para ir ao menu principal')

    else:
        print('Não possui clientes ativos para pedidos.')
        input('Pressione <enter> para continuar')

