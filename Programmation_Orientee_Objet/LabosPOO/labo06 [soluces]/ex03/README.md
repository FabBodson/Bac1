# Exercice 3 : Définition du module records

**Durée estimée** : 1h

## Objectif visé: 

- Définir des classes permettant de manipuler une collection d'enregistrements
- Utiliser les exceptions afin de gérer les cas d'erreur
 
## Description:

Dans les données téléchargées, nous allons nous intéresser au répertoire "data/csse_covid_19_data/csse_covid_19_daily_reports"

Celui-ci contient plusieurs fichiers au format CSV. Chaque fichier CSV contient les données COVID-19 collectées par pays 
à une date donnée.


## Qu'est-ce qu'un fichier CSV ?
CSV signifie "Comma Separated Values", autrement dit un fichier dont les champs sont 
généralement séparés par des virgules (il s'agit également parfois de tabulation ou de ';').

Exemple:

    nom,prénom,identifiant
    Lorquet,Cyril,LORCY
    Hendrikx,Nicolas,HENNI
    ...
    Lauwers,Dorian,LAUDO

Que l'on peut traduire par:

    En-tête:    nom,prénom,identifiant
    Ligne 1:    Lorquet,Cyril,LORCY
    Ligne 2:    Hendrikx,Nicolas,HENNI
    ...         ...
    Ligne N:    Lauwers,Dorian,LAUDO

Dans notre cas, nos fichiers contiennent les données structurées comme suit:

    Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered
    Hubei,Mainland China,2020-02-15T23:13:05,56249,1596,5623
    ,Belgium,2020-02-04T15:43:02,1,0,0
    ,Japan,1/22/2020 17:00,2,,
    
Remarquez que certains champs peuvent être vides et devront donc avoir des valeurs par défaut. 
C'est le cas aux lignes 3 et 4 pour le champ "Province/State" et à la ligne 5 pour le nombre de décès (Deaths) et 
le nombre de patients guéris (Recovered).

## La gestion des enregistrements

Les données contenues dans ces fichiers CSV peuvent être vues comme des "enregistrements" (comme les tuples d'une table 
dans une base de données relationnelle).

Nous allons créer un module chargé de représenter ces enregistrements, d'en rassembler une collection, et de pouvoir les
récupérer en fonction de certains critères, à la manière d'une table dans une base de données relationnelle.

## Mise en place

Dans le package `covid19`, définissez un module `records`. 
Ce module définira deux classes:
- Record
- RecordSet 

### La classe Record

Cette classe a pour objectif d'associer plusieurs métriques à une localisation. Dans nos fichiers CSV, une localisation
est représentée par la combinaison "Country/Region, Province/State" que nous allons simplifier en (Country, Province).

Un enregistrement (Record) aura donc pour objectif d'associer à cette paire un ensemble variable de métriques. A cette 
fin, elle définira les méthodes suivantes:

```python
def __init__(self, country, province):
    pass

def __getitem__(self, metric):
    """
    Cette méthode magique permet de retrouver une métrique particulière en fonction de son nom. 
    Elle pourra être utilisée comme suit: record['deaths']
        
    Paramètres:
    - metric: str: le nom de la métrique en question (par exemple: 'death', 'confirmed', ou encore 'recovered') 
    """
    pass

def add_metric(self, name, value):
    """
    Cette méthode permettra d'ajouter une nouvelle métrique avec sa valeur ou d'écraser la valeur d'une métrique 
    existante. Par exemple: record.add_metric('deaths', 1)
    """
    pass
```


### La classe RecordSet

Cette classe a pour objectif de contenir une collection d'enregistrements et de pouvoir retrouver des enregistrements
spécifiques en fonction de leurs clés:
- Location: Tuple[str, str]: (Country, Province) 
- Timestamp: datetime

Elle devra donc maintenir deux "index" différents.

Pour ce faire, elle définira les méthodes suivantes:

```python
def __init__(self):
    pass

def __getitem__(self, key):
    """
    Cette méthode magique permet de retrouver un seul et unique enregistrement dans la collection en fonction des clés
    suiantes: (Country, Province) et timestamp.
    Paramètres:
    - key: Tuple[Tuple[str, str], datetime]: un tuple contenant les clés de recherche. Par exemple: (('Belgique', 'Liège'), datetime(year=2020, month=2, day=1))
    Retour:
    - Record ou None: retourne l'enregistrement spécifique. Si l'ensemble de clés ne permet pas de retrouver un résultat, la valeur de retour sera None.
    """
    pass

def add_record(self, timestamp, record):
    """
    Cette méthode permet d'ajouter un nouvel enregistrement à la collection existante. Elle veillera à mettre à jour les différents "index".
    Paramètres:
    - timestamp: datetime: timestamp de l'enregistrement
    - record: Record: l'enregistrement à ajouter
    Retour: aucun
    """

@property
def locations(self):
    """
    Cette propriété permettra de récupérer toutes les localisations déjà enregistrées.
    Retour: List[Tuple[str, str]]: liste des différentes localisations (tuple associant Country/Province) 
    """
    pass
    
@property
def timestamps(self):
    """
    Cette propriété permettra de récupérer tous les timestamps déjà enregistrés.
    Retour: List[datetime]: liste des différents timestamps 
    """
    pass
```

## Tests

Comme d'habitude, testez vos méthodes !

- **date.strftime()**: https://docs.python.org/3/library/datetime.html#datetime.date.strftime
- **datetime.strptime()**: https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime

 
 