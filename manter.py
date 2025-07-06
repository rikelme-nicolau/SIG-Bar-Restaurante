import json
import os
import atexit

import clientes
import pedidos
import estoque
import menu
import rh

ARQUIVO = "dados.json"


def carregar():
    """
    Carrega todos os dados do JSON e preenche as variáveis globais dos módulos.
    """
    if not os.path.exists(ARQUIVO):
        return

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Substitui os dicionários iniciais pelos carregados (ou mantém vazios)
    clientes.clientes_dados       = dados.get("clientes", {})
    pedidos.id_pagamentos         = dados.get("pagamentos", {})
    estoque.estoque_bebida        = dados.get("estoque_bebida", {})
    estoque.estoque_alimento      = dados.get("estoque_alimento", {})
    menu.menu_dados               = dados.get("menu", {})
    rh.rh_dados                   = dados.get("rh", {})


def salvar():
    """
    Coleta os dados atuais dos módulos e salva tudo em um único JSON.
    """
    dados = {
        "clientes":     clientes.clientes_dados,
        "pagamentos":   pedidos.id_pagamentos,
        "estoque_bebida":   estoque.estoque_bebida,
        "estoque_alimento": estoque.estoque_alimento,
        "menu":         menu.menu_dados,
        "rh":           rh.rh_dados
    }

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


# Carrega dados ao importar este módulo
carregar()

# Garante salvamento ao encerrar o programa
atexit.register(salvar)