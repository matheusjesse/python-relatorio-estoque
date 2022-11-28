import json
import csv
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        with open(path) as data:
            if path.endswith(".json"):
                data = json.load(data)
            if path.endswith(".csv"):
                data = list(csv.DictReader(data))
            if path.endswith(".xml"):
                data = xmltodict.parse(data.read())["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
