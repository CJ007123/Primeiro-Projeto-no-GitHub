from gerenciamento import produto

def calcular_desconto(desconto, preco_minimo):
    """Aplica um desconto nos produtos acima de um determinado preço."""
    produtos_com_desconto = []
    
    for nome, info in produto.items():
        if info['valor'] >= preco_minimo:
            novo_preco = round(info['valor'] - (info['valor'] * desconto / 100), 2)
            produtos_com_desconto.append((nome, novo_preco))
    
    if produtos_com_desconto:
        print('Produtos com desconto:')
        for nome, preco in produtos_com_desconto:
            print(f'{nome} - Novo preço: R$ {preco:.2f}')
    else:
        print(f' Nenhum produto com preço acima de R$ {preco_minimo:.2f} para aplicar o desconto.')


def registrar_venda(nome, quantidade):
    """Registra a venda de um produto, atualiza o estoque e calcula o total das vendas."""
    if nome in produto and produto[nome]['quantidade'] >= quantidade:
        produto[nome]['quantidade'] -= quantidade
        salvar_vendas(nome,quantidade)
        total_venda = produto[nome]['valor'] * quantidade
        print(f' Venda registrada! Produto: {nome} | Quantidade vendida: {quantidade} | Total: R$ {total_venda:.2f}')
    else:
        print(f'Estoque insuficiente ou produto "{nome}" não encontrado!')

vendas = {}
def salvar_vendas(nome,quantidade):
    if vendas:
        vendas[nome] += quantidade
    else:
        vendas[nome] = quantidade


def produto_mais_vendido():
    if not vendas:
        print('Não houve vendas registradas!')
    else:
        mais_vendido = max(vendas, key=vendas.get)
        print(f'O produto mais vendido do estoque {mais_vendido} com {vendas[mais_vendido]} unidades vendidas')


def calcular_valor_total_produto(nome):
    """Calcula o valor total de todas as unidades de um produto no estoque."""
    produto_detalhes = produto.get(nome)
    if produto_detalhes:
        total = produto_detalhes['valor'] * produto_detalhes['quantidade']
        print(f'Produto: {nome} | Valor total: R$ {total:.2f}')
    else:
        print(f'Produto "{nome}" não encontrado no estoque!')

def calcular_valor_total_estoque():
    """Calcula o valor total de todos os produtos no estoque."""
    if not produto:
        print("O estoque está vazio!")
        return 0
    total_valor = sum(item['valor'] * item['quantidade'] for item in produto.values())
    total_quantidade = sum(item['quantidade'] for item in produto.values())
    
    print(f'Valor total do estoque: R$ {total_valor:.2f}')
    print(f'Quantidade total de produtos: {total_quantidade}')
