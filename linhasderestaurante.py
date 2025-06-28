produtos = {}

def cadastrar_produto():
    codigo = input('Código do produto: ')
    nome = input('Nome do produto: ')
    categoria = input('Categoria: ')
    preco = float(input('Preço unitário: '))
    estoque = int(input('Quantidade inicial em estoque: '))
    produtos[codigo] = {
        'nome': nome,
        'categoria': categoria,
        'preco': preco,
        'estoque': estoque,
        'historico': []
    }
    print('Produto cadastrado!')

def registrar_entrada():
    codigo = input('Código do produto para entrada: ')
    if codigo not in produtos:
        print('Produto não cadastrado.')
        return
    quantidade = int(input('Quantidade recebida: '))
    produtos[codigo]['estoque'] += quantidade
    produtos[codigo]['historico'].append(f'Entrada: +{quantidade}')
    print('Entrada registrada.')

def registrar_saida():
    codigo = input('Código do produto para saída: ')
    if codigo not in produtos:
        print('Produto não cadastrado.')
        return
    quantidade = int(input('Quantidade retirada/vendida: '))
    if quantidade > produtos[codigo]['estoque']:
        print('Estoque insuficiente.')
        return
    produtos[codigo]['estoque'] -= quantidade
    produtos[codigo]['historico'].append(f'Saída: -{quantidade}')
    print('Saída registrada.')

def consultar_estoque():
    print('Estoque atual:')
    for codigo, info in produtos.items():
        print(f"{codigo} - {info['nome']} - Categoria: {info['categoria']} - Estoque: {info['estoque']} - Preço: R${info['preco']:.2f}")

def listar_por_categoria():
    categoria_busca = input('Digite a categoria para listar: ')
    print(f'Produtos na categoria "{categoria_busca}":')
    for codigo, info in produtos.items():
        if info['categoria'].lower() == categoria_busca.lower():
            print(f"{codigo} - {info['nome']} - Estoque: {info['estoque']} - Preço: R${info['preco']:.2f}")

def menu():
    while True:
        print('\n1 - Cadastrar produto')
        print('2 - Registrar entrada')
        print('3 - Registrar saída')
        print('4 - Consultar estoque')
        print('5 - Listar produtos por categoria')
        print('6 - Sair')
        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            registrar_entrada()
        elif escolha == '3':
            registrar_saida()
        elif escolha == '4':
            consultar_estoque()
        elif escolha == '5':
            listar_por_categoria()
        elif escolha == '6':
            print('Saindo...')
            break
        else:
            print('Opção inválida.')

menu()
