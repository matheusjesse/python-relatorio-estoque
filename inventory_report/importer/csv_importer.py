from inventory_report.importer.importer import Importer

import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith(".csv"):
            with open(path) as data:
                data_dict = csv.DictReader(data)
                data_list = list(data_dict)
            return data_list
        else:
            raise ValueError("Arquivo inválido")
