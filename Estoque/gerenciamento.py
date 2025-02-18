produto = {}

def adicionar_produto(nome, valor, quantidade):
    """Adiciona um produto ao estoque."""
    if nome in produto:
        print(f'O produto "{nome}" já existe no estoque!')
    else:
        produto[nome] = {'nome_produto': nome, 'valor': valor, 'quantidade': quantidade}
        print(f'Produto "{nome}" adicionado com sucesso!')

def listar_produtos():
    """Lista todos os produtos cadastrados no estoque."""
    if not produto:
        print('Estoque vazio! Nenhum produto cadastrado.')
    else:
        print(' Produtos cadastrados:')
        for nome, info in produto.items():
            print(f'Nome: {info["nome_produto"]} | Valor: R$ {info["valor"]:.2f} | Quantidade: {info["quantidade"]}')

def remover_produto(nome):
    """Remove um produto do estoque."""
    if nome in produto:
        del produto[nome]
        print(f'Produto "{nome}" removido do estoque!')
    else:
        print(f'O produto "{nome}" não foi encontrado no estoque!')

def buscar_produto(nome):
    """Busca informações sobre um produto específico."""
    produto_info = produto.get(nome)
    if produto_info:
        print('Produto encontrado:')
        print(f'Nome: {produto_info["nome_produto"]}')
        print(f'Valor: R$ {produto_info["valor"]:.2f}')
        print(f'Quantidade: {produto_info["quantidade"]}')
    else:
        print(f'O produto "{nome}" não foi encontrado no estoque!')

def atualizar_produto(nome, novo_valor=None, nova_quantidade=None):
    """Atualiza o valor ou a quantidade de um produto."""
    if nome in produto:
        if novo_valor is not None:
            produto[nome]['valor'] = novo_valor
            print(f'O valor do produto "{nome}" foi atualizado para R$ {novo_valor:.2f}')
        if nova_quantidade is not None:
            produto[nome]['quantidade'] = nova_quantidade
            print(f'A quantidade do produto "{nome}" foi atualizada para {nova_quantidade}')
    else:
        print(f'O produto "{nome}" não foi encontrado no estoque!')


def filtrar_por_quantidade(quantidade_minima, quantidade_maxima):
    """Lista os produtos que possuem quantidade maior ou igual ao informado."""
    produtos_filtrados = [(nome, info['quantidade']) for nome, info in produto.items() if quantidade_minima <= info['quantidade'] <= quantidade_maxima]
    
    if produtos_filtrados:
        print(f'Produtos com quantidade maior ou igual a {quantidade_minima}:')
        for nome, quantidade in produtos_filtrados:
            print(f'{nome} - unidades {quantidade}')
    else:
        print(f'Nenhum produto com quantidade maior ou igual a {quantidade_minima}.')

def filtrar_por_preco(valor_minimo, valor_maximo):
    """Lista os produtos que possuem preço maior ou igual ao informado."""
    produtos_filtrados = [(nome, info['valor']) for nome, info in produto.items() if valor_minimo <= info['valor'] <= valor_maximo]
    
    if produtos_filtrados:
        print(f'Produtos com preço maior ou igual a {valor_minimo}:')
        for nome, valor in produtos_filtrados:
            print(f'{nome} - R$ {valor}')
    else:
        print(f'Nenhum produto com preço maior ou igual a {valor_minimo}.')