import csv


def read_csv_file(file):
    products = []
    try:
        with open(file, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                products.append(row)

    except FileNotFoundError:
        print(f"'{file}' not found")

    return products


def write_csv_file(file, user, flask, result):
    try:
        with open(file, "a", newline='') as csv_file:
            fieldnames = ['Nom', 'Prenom', 'Email', 'Flacon', 'Lot-date']
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=fieldnames)

            file_empty = read_csv_file(file)
            message = ""
            if len(file_empty) == 0:
                writer.writeheader()
                message = f"Fichier '{file}' créé"
            writer.writerow({'Nom': str.upper(user.lastname),
                             'Prenom': user.firstname,
                             'Email': user.email,
                             'Flacon': flask.reference,
                             'Lot-date': result.lot_date
                             })
            if message == "":
                message = f"Ligne ajoutée"

            print(message)

    except FileNotFoundError:
        print(f"'{file}' not found")
