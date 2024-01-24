from algo_labo01.algorithms import first_fit, first_fit_decreasing, full_bin
from algo_labo01.model import Family
from algo_labo01.algorithms import Result
import csv


def _main():
    # capacity = int(input("Quelle capacité pour chaque navette ? "))
    capacity = 7
    families = []

    try:
        with open('familles.csv', newline='') as family_file:
            print(f"'familles.csv' successfully opened\n")
            family_list = csv.reader(family_file, delimiter=';')
            total_family_people = 0
            for line in family_list:
                if line[0] == 'NOM':
                    continue
                else:
                    new_family = Family(line[0], int(line[1]))
                    families.append(new_family)
                    total_family_people += int(line[1])

    except FileNotFoundError:
        print(f"'familles.csv' not found")

    print("--- First Fit ---")
    first_fit(families.copy(), capacity).print_bus()
    print("\n--- First Fit Decreasing ---")
    first_fit_decreasing(families.copy(), total_family_people, capacity).print_bus()
    print("\n--- Full Bin ---")
    full_bin(families.copy(), capacity).print_bus()


if __name__ == '__main__':
    _main()
