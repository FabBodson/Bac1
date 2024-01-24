import csv


class CSVReader:

    def __init__(self, filename, separator=';'):
        self.filename = filename
        self.separator = separator

    def read(self):
        with open(self.filename, newline='') as file:
            stream = csv.DictReader(file, delimiter=self.separator)
            for row in stream:
                yield {key.lower(): value for key, value in row.items()}
