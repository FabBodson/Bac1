

class Record:
    def __init__(self, country, province):
        self.location = (
            country if len(country) > 0 else 'Unknown',
            province if len(province) > 0 else 'All'
        )
        self.__metrics = {}

    def __getitem__(self, item):
        return self.__metrics[item]

    def add_metric(self, name, value):
        self.__metrics[name] = value


class RecordSet:
    def __init__(self):
        self.__records_by_timestamp = {}
        self.__records_by_location = {}

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            return None
        try:
            records = self.__records_by_timestamp[item[1]]
            for record in records:
                if record.location == item[0]:
                    return record
            return None
        except KeyError:
            return None

    def add_record(self, timestamp, record):
        try:
            records = self.__records_by_timestamp[timestamp]
            records.append(record)
        except KeyError:
            self.__records_by_timestamp[timestamp] = [record]

        try:
            records = self.__records_by_location[record.location]
            records.append(record)
        except KeyError:
            self.__records_by_location[record.location] = [record]

    @property
    def locations(self):
        return sorted(self.__records_by_location.keys())

    @property
    def timestamps(self):
        return sorted(self.__records_by_timestamp.keys())
