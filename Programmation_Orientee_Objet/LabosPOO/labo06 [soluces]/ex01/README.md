# Exercice 1 : Téléchargement programmatique des données depuis GitHub

**Durée estimée** : 15 minutes

**Objectif visé** : 

- Utiliser la bibliothèque GitPython pour télécharger et mettre à jour le contenu d'un dépôt distant.

**Description** :

[Git](https://git-scm.com) est un outil utilisé par les développeurs pour gérer différentes versions de leur code source tout en collaborant
à plusieurs. Les fichiers sources sont généralement partagés sur un serveur Git, comme Gitlab (à l'école) ou encore 
le célèbre GitHub.

Afin d'obtenir les données du COVID-19, nous aurons besoin d'accéder au dépôt GitHub de l'institut John Hopkins: https://github.com/CSSEGISandData/COVID-19,
et d'en télécharger une copie locale sur notre ordinateur. Nous devrons également nous assurer de toujours travailler
avec les dernières données en date. 

**Préalable**
Afin de pouvoir utiliser le bibliothèque GitPython, nous aurons besoin d'installer l'outil [Git](https://git-scm.com). 
Si vous êtes sous Windows, veillez à bien ajouter Git au path de Windows.

**Le programme**

Créez un package `covid19` à la racine du projet. Dans ce package, créez un module `collector`.

Insérez-y le code suivant:
```python
import git


def collect(url, name):
    try:
        repository = git.Repo(name)
        print('Mise à jour du dépôt...', end='\t')
        repository.remotes.origin.pull()
    except (git.InvalidGitRepositoryError, git.NoSuchPathError):
        print('Création du dépot...', end='\t')
        git.Git('.').clone(url, name)
    print('OK')
```

Créez ensuite un module exécutable nommé `main.py`, contenant une fonction `main()`. 
Cette fonction va appeler la fonction `collect()` du module `collector` comme suit: 
```python
collector.collect('https://github.com/CSSEGISandData/COVID-19.git', 'data')
``` 

Que constatez-vous ?

**Analyse du code**

```python
repository = git.Repo(url)
repository.remotes.origin.pull()
```
La première instruction permet d'initialiser git en lui indiquant le répertoire contenant notre version locale du dépot distant.
Si le répertoire de destination `REPOSITORY_DIR` n'existe pas, cette instruction lèvera l'exception `git.exc.NoSuchPathError`.

La seconde instruction permet d'exécuter la commande `git pull`, mettant à jour notre version locale du dépôt.
Si aucun dépôt distant n'a été préalablement téléchargé, cette instruction lèvera une exception de type `git.exc.NoSuchPathError`.

Nous gérons les deux exceptions dans le bloc `except`, en "clonant" le dépôt distant (commande `git clone`):
```python
git.Git('.').clone(url, name)
```  

A ce stade, votre projet devrait avoir la structure suivante: 

    - covid19
        - data
            + archived_data
            + csse_covid_19_data
            + who_covid_19_situation_reports
            * README.MD
        * __init__.py
        * collector.py
        * main.py
    - ex01
        ...
    - venv
        ...
    * README.md
    
**Note**:
Si pour une raison indépendante de votre volonté, la configuration de votre système ne vous permet pas d'utiliser GitPython,
télécharger directement le contenu du dépôt grâce au lien suivant: "https://github.com/CSSEGISandData/COVID-19/archive/master.zip", 
et assurez-vous de l'extraire dans le bon répertoire et de le renommer correctement afin de retrouver l'arborescence sus-mentionnée.