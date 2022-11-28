import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    _, path_file, report_type = sys.argv

    if path_file.endswith(".csv"):
        file = InventoryRefactor(CsvImporter)
    if path_file.endswith(".json"):
        file = InventoryRefactor(JsonImporter)
    if path_file.endswith(".xml"):
        file = InventoryRefactor(XmlImporter)
    print(file.import_data(path_file, report_type), end="")
