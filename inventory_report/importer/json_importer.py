from inventory_report.importer.importer import Importer

import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".json"):
            with open(path) as data:
                data = json.loads(data.read())
            return data
        else:
            raise ValueError("Arquivo inválido")
