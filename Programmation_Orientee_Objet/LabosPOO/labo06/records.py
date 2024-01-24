class Record:
    def __init__(self, country, province):
        self.location = (
            country if len(country) > 0 else 'Unknown',
            province if len(province) > 0 else 'All'
        )
        self.__metrics = {}

    def __getitem__(self, item):
        return self.metrics[item]

    def add_metrics(self, name, value):
        self.__metrics[name] = value
