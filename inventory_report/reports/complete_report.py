from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def quantity_products(products):
        string = "Produtos estocados por empresa:\n"

        name_company = [name["nome_da_empresa"] for name in products]
        counter = Counter(name_company)

        for element in counter:
            string += f"- {element}: {counter.get(element)}\n"

        return string

    def generate(products):
        return (
            f"{SimpleReport.generate(products)}\n"
            f"{CompleteReport.quantity_products(products)}"
        )
