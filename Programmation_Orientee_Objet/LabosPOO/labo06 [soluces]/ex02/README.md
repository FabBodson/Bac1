# Exercice 2 : Agrégation des données: collecter les fichiers d'un certain type dans un répertoire 

**Durée estimée** : 20 minutes

## Objectif visé: 

- Utiliser le module os et sa fonction `walk()` afin de récupérer les fichiers portant une extension particulière dans un répertoire donné. 
 
## Description:

Dans le package `covid19`, créez un module `utils`. 
Dans ce module, vous allez définir la fonction suivante: 

```python
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
    pass
```

## Documentation

- `os.walk()`: https://docs.python.org/3/library/os.html#os.walk
- `os.path.splitext()`: https://docs.python.org/3/library/os.path.html#os.path.splitext
 
