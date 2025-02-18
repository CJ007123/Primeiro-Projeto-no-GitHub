from gerenciamento import adicionar_produto, atualizar_produto,remover_produto,listar_produtos,filtrar_por_quantidade,filtrar_por_preco
from vendas import registrar_venda,calcular_desconto,calcular_valor_total_estoque, calcular_valor_total_produto
from salvar_carregar import salvar_estoque, carregar_estoque

if __name__ == '__main__':
    adicionar_produto("Guitarra Fender", 3500, 10)
    adicionar_produto("Guitarra Ibanez", 2000, 100)
    adicionar_produto("Guitarra SG", 2000, 5)
    print()

    atualizar_produto("Guitarra Fender", 1500,200)
    print()
    atualizar_produto("Guitarra SG", 1500,300)
    print()

    remover_produto("Amplificador Marshall")
    print()
    listar_produtos()
    print()

    filtrar_por_quantidade(100,300)
    print()
    filtrar_por_preco(1500,2000)
    print()

    print("Aplicando desconto de 10% nos produtos acima de R$ 3000:")
    calcular_desconto(10, 3000)
    print()

    print("Registrando venda de 10 guitarras:")
    registrar_venda("Guitarra Fender", 10)
    print()

    calcular_valor_total_estoque()
    print()
    calcular_valor_total_produto("Guitarra Ibanez")

    print("Salvando estoque no arquivo:")
    salvar_estoque("estoque.json")
    print()

    print("Carregando estoque:")
    carregar_estoque("estoque.json")
    print()