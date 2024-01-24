from os import path, walk
from os.path import splitext


def collect_files_with_extension(directory, extensions):
    """
    Cette fonction utilisera le module `os` et sa fonction `walk` afin de collecter dans le répertoire `directory` les fichiers
    portant une des extensions passée en paramètre.

    Paramètres:
    - directory: str: contenant le chemin vers un répertoire sur votre machine
    - extensions: List[str]: liste d'extensions, par exemple: ['.csv', '.pdf']

    Retour: List[Dict[str, str]]: une liste de dictionnaires.
    Chaque dictionnaire contiendra les 3 clés suivantes:
    - 'path': le chemin complet vers le fichier (par exemple: C:/chemin/vers/fichier.csv),
    - 'name': le nom du fichier sans son extension (par exemple: 2/12/2020)
    - 'extension': l'extension (par exemple: .csv)
    """
    for root, _, files in walk(directory):
        for file in files:
            filename, extension = splitext(file)
            if extension in extensions:
                yield {
                    'path': f'{root}/{file}',
                    'name': filename,
                    'extension': extension
                }

    """fichiers = []

    for file in walk(directory):

        file_dic = {'path': file[0], 'name': file[1], 'extension': ''}
        file_detail = splitext(directory)

        if file_detail[1] == extensions:
            file_dic['extension'] = file_detail[1]
        else:
            file_dic['extension'] = '/'

        fichiers.append(file_dic)

    return fichiers"""


def _main():
    for element in collect_files_with_extension('/Users/fabricebodson/Desktop/Securité et Systèmes/Q2/POO/LabosPOO/labo06/covid19', ['.py']):
        print(element)


if __name__ == '__main__':
    _main()