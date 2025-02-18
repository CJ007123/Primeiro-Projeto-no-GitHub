import json
from gerenciamento import produto
def salvar_estoque(arquivo):
    """Salva os dados do estoque em um arquivo JSON."""
    with open(arquivo, 'w', encoding='utf-8') as arquivos:
        json.dump(produto, arquivos, indent=4, ensure_ascii=False)
    print(f'✅ Estoque salvo no arquivo "{arquivo}".')

def carregar_estoque(arquivo):
    """Carrega os dados do estoque de um arquivo JSON."""
    global produto
    try:
        with open(arquivo, 'r', encoding='utf-8') as arquivos:
            produto = json.load(arquivos)
        print(f'✅ Estoque carregado do arquivo "{arquivo}".')
    except FileNotFoundError:
        print(f'⚠️ Arquivo "{arquivo}" não encontrado. Iniciando um novo estoque.')
