from ins.entities import EntitySource, Entity, EntityTarget
import csv


class CsvEntitySource(EntitySource):
    def __init__(self, opened_csv_file):
        self.opened_csv_file = opened_csv_file

    def get(self):
        csv_file_content = csv.DictReader(self.opened_csv_file, delimiter=";")
        entities = []
        for dictionnary in csv_file_content:
            code = dictionnary["CodeINS"]
            name = dictionnary["Nom"]
            entity = Entity(code, name)
            for key, value in dict.items(dictionnary):
                if key in entity.datas:
                    entity.datas[key] = int(dictionnary[key])
                else:
                    continue
            entities.append(entity)
        return entities


class CsvEntityTarget(EntityTarget):
    def __init__(self, file_to_write):
        self.file_to_write = file_to_write

    def put(self, source: EntitySource):
        fieldnames = ["CodeINS", "Nom", "MontantMedian", "PremierQuartile"]
        writer = csv.DictWriter(self.file_to_write, delimiter=";", fieldnames=fieldnames)
        writer.writeheader()
        for entity in source:
            writer.writerow({"CodeINS": entity[0], "Nom": entity[1],
                             "MontantMedian": entity[2],
                             "PremierQuartile": entity[2]})
