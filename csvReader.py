import csv


def getLst(file_name, sep=','):
    with open(file_name, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f, delimiter=sep)
        return [line for line in reader]
