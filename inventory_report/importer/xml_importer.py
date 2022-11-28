from inventory_report.importer.importer import Importer

import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith(".xml"):
            with open(path, "r") as file:
                read = file.read()
                data_dict = xmltodict.parse(read)
            return list(data_dict["dataset"]["record"])
        else:
            raise ValueError("Arquivo inválido")
