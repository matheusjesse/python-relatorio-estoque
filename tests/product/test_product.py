from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        5,
        "Polar",
        "material",
        "2021-09-20",
        "2022-09-20",
        "A1C3",
        "local fresco e longe do sol"
    )
    assert product.id == 5
    assert product.nome_do_produto == "Polar"
    assert product.nome_da_empresa == "material"
    assert product.data_de_fabricacao == "2021-09-20"
    assert product.data_de_validade == "2022-09-20"
    assert product.numero_de_serie == "A1C3"
    assert product.instrucoes_de_armazenamento == "local fresco e longe do sol"
