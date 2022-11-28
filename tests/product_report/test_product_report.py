from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        2,
        'Maça',
        'Caxias',
        '07/03/2021',
        '07/09/2021',
        '3CA0',
        'em ambiente arejado'
    )
    message = (
        f'O produto {product.nome_do_produto}'
        f' fabricado em {product.data_de_fabricacao}'
        f' por {product.nome_da_empresa}'
        f' com validade até {product.data_de_validade}'
        f' precisa ser armazenado {product.instrucoes_de_armazenamento}.'
    )
    assert product.__repr__() == message
