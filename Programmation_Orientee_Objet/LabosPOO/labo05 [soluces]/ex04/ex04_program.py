import os

import ex03_steganography as steganography


def change_directory():
    valid = False
    while not valid:
        path = input('Dans quel répertoire souhaitez-vous travailler ? ')
        if not os.path.exists(path):
            print('> Ce répertoire n\'existe pas.')
            continue
        os.chdir(path)
        valid = True


def get_strategy(file_path):
    strategy = None
    while strategy not in ('a', 'l'):
        strategy = input('  > Stratégie [a]crostiche ou [l]ettres ? ')
    if strategy == 'a':
        return steganography.AcrosticStrategy()
    elif strategy == 'l':
        return steganography.LetterStrategy()
    else:
        print('  > Stratégie inconnue !')
        return None


def decrypt_file(file_path, destination):
    print(f'> [{file_path}]')
    strategy = get_strategy(file_path)
    if strategy is None:
        print('  > Pas de décryptage pour ce fichier !')
        return
    with open(file_path) as source:
        strategy.decrypt(source, destination)


def main():
    change_directory()
    with open('output.txt', 'w') as destination:
        for _, _, files in os.walk('.'):
            for file_path in files:
                filename, file_extension = os.path.splitext(file_path)
                if file_extension == '.txt' and filename != 'output':
                    decrypt_file(file_path, destination)


if __name__ == '__main__':
    main()
