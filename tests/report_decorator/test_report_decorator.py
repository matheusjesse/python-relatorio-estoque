from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.colored_report import ColoredReport


mock_data = [{
    "nome_da_empresa": "Caxias",
    "data_de_fabricacao": "2021-02-18",
    "data_de_validade": "2023-09-17",
}]


def test_decorar_relatorio():
    report = (ColoredReport(SimpleReport)).generate(mock_data)
    assert "32mData de fabricação mais antiga" in report
    assert "36m2023-09-17" in report
    assert "31mCaxias" in report
