import collector


def _main():
    collector.collect('https://github.com/CSSEGISandData/COVID-19.git', 'data')


if __name__ == '__main__':
    _main()
