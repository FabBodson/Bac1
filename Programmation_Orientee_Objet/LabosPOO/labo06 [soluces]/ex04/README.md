# Exercice 4 : Lecture des rapports journaliers et constitution de séries temporelles (timeseries) 

**Durée estimée** : 1h

## Objectif visé: 

- Utiliser le module csv de Python afin de lire et écrire dans un fichier CSV
 
## Description:

Tout est maintenant en place pour que nous puissions passer à lecture des fichiers et à la constituation d'une série 
temporelle.

Pour rappel, le répertoire de données qui nous intéresse est le suivant: "data/csse_covid_19_data/csse_covid_19_daily_reports"

Celui-ci contient plusieurs fichiers au format CSV. Chaque fichier CSV contient les données COVID-19 collectées par pays 
à une date donnée.

**Attention**: ce répertoire contient également deux fichiers que nous allons devoir ignorer:
- .gitignore
- README.MD

## Le programme

Dans le package `covid19`, créez un module `aggregator`. Ce module définira une fonction `aggregate(directory)` qui sera appelée par le programme principal (module `main`).

Ce module a pour objectif de parcourir tous les fichiers CSV présents dans le répertoire passé en paramètre (`data/csse_covid_19_data/csse_covid_19_daily_reports`), 
et de créer un répertoire 'covid19/output' afin d'y stocker trois nouveaux fichiers respectivement nommés:
- confirmed.csv
- deaths.csv
- recovered.csv

Voici un exemple de sortie:

    Country/Region,Province/State,2020-01-22,2020-01-23,2020-01-24,[...],2020-03-14,2020-03-15,2020-03-16
    Belgium,All,0,0,0,[...],689,886,1058
    ...
    Italy,All,0,0,0,[...],21157,24747,27980
    
Pour chaque fichier, la valeur des colonnes datées représente respectivement le nombre de cas confirmés, 
le nombre de décès et le nombre de guérisons.

Vous êtes libres d'organiser le code de ce module à votre guise. Veillez cependant à utiliser les différentes classes et
fonction réalisés au cours des exercices précédents.

## Les pièges

Plusieurs pièges se cachent dans les données à exploiter:
- Les fichiers CSV contiennent une en-tête, vous devrez donc veiller à la prendre en compte dans votre programme et la
passer au besoin.
- Lorsqu'un répertoire est listé, les fichiers obtenus ne sont pas nécessairement obtenus dans l'ordre alphabétique. Veillez donc
à garantir l'ordre des dates (en les triant, par exemple).
- Le format des dates dans les noms de fichier est un format américain (Mois-Jour-Année). Dans les fichiers de sortie, 
veillez à convertir ces dates au format "Année-Mois-Jour": YYYY-MM-DD. 
- Les champs ne sont pas toujours complétés (certaines données sont manquantes)
- Le nombre de colonnes présentes dans chaque fichier évolue au cours du temps (insertion des données de latitude et longitude par exemple)


## Conseils

- Veillez à bien structurer votre code. 
- L'utilisation de fonctions est recommandée


## Documentation

- **module csv**: https://docs.python.org/3.7/library/csv.html
- **os.mkdir()**: https://docs.python.org/3/library/os.html#os.mkdir
- **date.strftime()**: https://docs.python.org/3/library/datetime.html#datetime.date.strftime
- **datetime.strptime()**: https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
 