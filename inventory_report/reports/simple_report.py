from datetime import date


class SimpleReport:

    @classmethod
    def generate(self, list_products):
        company_count = self.get_max_products(list_products)
        old_date = self.get_old_date(list_products)
        oldest_fabrication_date = self.get_close_expire_date(list_products)

        max_company = max(company_count, key=company_count.get)

        return (
          f"Data de fabricação mais antiga: {old_date}\n"
          f"Data de validade mais próxima: {oldest_fabrication_date}\n"
          f"Empresa com mais produtos: {max_company}"
        )

    @classmethod
    def get_old_date(cls, products):
        return min([product["data_de_fabricacao"] for product in products])

    @classmethod
    def get_close_expire_date(cls, products):
        close_dates = []
        for product in products:
            if product["data_de_validade"] >= date.today().isoformat():
                close_dates.append(product["data_de_validade"])
        return min(close_dates)

    @classmethod
    def get_max_products(cls, products):
        name_count = dict()
        for product in products:
            if product["nome_da_empresa"] in name_count.keys():
                name_count[product["nome_da_empresa"]] += 1
            else:
                name_count[product["nome_da_empresa"]] = 1
        return name_count
