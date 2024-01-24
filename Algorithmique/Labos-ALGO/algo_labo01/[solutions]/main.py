import csv

from algorithms import first_fit, first_fit_decreasing, full_bin
from model import Family


def load_families(filename):
    result = []
    with open(filename, 'r') as file:
        stream = csv.reader(file, delimiter=';')
        next(stream)
        for line in stream:
            result.append(Family(name=line[0], size=int(line[1])))
    return result


def main():
    capacity = int(input('Quelle capacité par navette ? '))
    families = load_families('familles.csv')
    algorithms = {
        'First Fit': first_fit,
        'First Fit Decreasing': first_fit_decreasing,
        'Full Bin': full_bin
    }

    for name, function in algorithms.items():
        result = function(families, capacity)
        print(f'\n--- {name} ---')
        print(f'Navettes nécessaires ({len(result.buses)}) :')
        for index, bus in enumerate(result.buses):
            print(f'#{index+1}: {bus}')


if __name__ == '__main__':
    main()
