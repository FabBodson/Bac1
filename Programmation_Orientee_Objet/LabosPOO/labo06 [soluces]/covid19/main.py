from covid19 import collector
from covid19.aggregator import Aggregator
from covid19.chart_generator import generate


def main():
    collector.collect('https://github.com/CSSEGISandData/COVID-19.git', 'data')

    aggregator = Aggregator()
    aggregator.aggregate('data/csse_covid_19_data/csse_covid_19_daily_reports')

    generate()


if __name__ == '__main__':
    main()