import csv
from datetime import datetime
import os


from covid19.records import Record, RecordSet
from covid19.utils import collect_files_with_extension


class Aggregator:

    METRICS = ('confirmed', 'deaths', 'recovered')

    HEADERS_COUNTRY = 'country'
    HEADERS_PROVINCE = 'province'
    HEADERS_CONFIRMED = 'confirmed'
    HEADERS_DEATHS = 'deaths'
    HEADERS_RECOVERED = 'recovered'

    def __init__(self):
        self.records = RecordSet()

    def aggregate(self, directory):
        print('Agrégation... ', end='\t')
        self.collect_records(directory)
        self.create_output_directory('output')
        self.create_output_files()
        print('OK')

    def collect_records(self, directory):
        for file in collect_files_with_extension(directory, ['.csv']):
            with open(file['path'], encoding='utf-8-sig') as stream:
                reader = csv.reader(stream)
                headers_read = False
                for row in reader:
                    if not headers_read:
                        headers = self.parse_header(row)
                        headers_read = True
                    else:
                        self.records.add_record(
                            datetime.strptime(file['name'], '%m-%d-%Y'), self.create_record(headers, row)
                        )

    def parse_header(self, row):
        names = {
            'Province/State': self.HEADERS_PROVINCE,
            'Province_State': self.HEADERS_PROVINCE,
            'Country/Region': self.HEADERS_COUNTRY,
            'Country_Region': self.HEADERS_COUNTRY,
            'Confirmed': self.HEADERS_CONFIRMED,
            'Deaths': self.HEADERS_DEATHS,
            'Recovered': self.HEADERS_RECOVERED,
        }

        headers = {}
        for index, item in enumerate(row):
            if item in names:
                headers[names[item]] = index

        return headers

    def create_record(self, headers, row):
        index_country = headers[self.HEADERS_COUNTRY]
        index_province = headers[self.HEADERS_PROVINCE]
        index_confirmed = headers[self.HEADERS_CONFIRMED]
        index_deaths = headers[self.HEADERS_DEATHS]
        index_recovered = headers[self.HEADERS_RECOVERED]

        record = Record(country=row[index_country], province=row[index_province])
        record.add_metric(self.METRICS[0], int(row[index_confirmed]) if len(row[index_confirmed]) > 0 else 0)
        record.add_metric(self.METRICS[1], int(row[index_deaths]) if len(row[index_deaths]) > 0 else 0)
        record.add_metric(self.METRICS[2], int(row[index_recovered]) if len(row[index_recovered]) > 0 else 0)

        return record

    @staticmethod
    def create_output_directory(directory):
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass

    def create_output_files(self):
        header = ['Country/Region', 'Province/State']
        header.extend([timestamp.strftime('%Y-%m-%d') for timestamp in self.records.timestamps])
        for metric in self.METRICS:
            self.create_output_file(metric, header)

    def create_output_file(self, metric, header):
        with open(f'output/{metric}.csv', 'w') as stream:
            writer = csv.writer(stream)
            self.write_metrics(writer, header, metric)

    def write_metrics(self, writer, header, metric):
        locations = self.records.locations
        writer.writerow(header)
        for location in locations:
            row = self.create_row(metric, location)
            writer.writerow(row)

    def create_row(self, metric, location):
        row = [location[0], location[1]]
        for timestamp in self.records.timestamps:
            record = self.records[location, timestamp]
            row.append(record[metric] if record else '0')
        return row
