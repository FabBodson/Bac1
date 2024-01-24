# Algorithmique : Bin-packing

Durée prévue : 4 heures


## Mise en place
- Depuis PyCharm, créez un nouveau projet nommé `algo-labo01`. Assurez-vous que celui-ci dispose de son propre environnement virtuel.
- Dans ce projet, vous créerez un module exécutable Python nommé `main.py`, ainsi que les modules `algorithms` et `model`.


## Problème
Notre agence de voyage dispose de plusieurs navettes. Lorsque nos vacanciers partent en excursion, nous devons mettre à 
leur disposition un nombre suffisant de navettes. Evidemment, les familles ne peuvent pas être séparées dans des 
navettes différentes. Nous souhaiterions une application nous permettant de connaitre le nombre minimal de navettes à 
affrêter pour une liste de familles donnée.  

L'agence met à votre disposition un exemple de fichier CSV comprenant un listing des familles à embarquer:

```
NOM;NOMBRE
Mathy;3
Beaupere;1
Lorquet;2
Carbonara;4
Hendrikx;6
Lauwers;5
```

## Mise en oeuvre
Afin de répondre au problème posé par l'agence de voyage, vous allez écrire un programme qui: 
- Demande à l'utilisateur la capacité d'une navette (toutes les navettes ont la même capacité)
- Charge le listing des familles depuis le fichier CSV fourni
- Effectue le calcul en utilisant les 3 algorithmes étudiés au cours théorique ("First-fit", "First-fit Decreasing" et "Full-bin")
- Affiche le résultat de chaque algorithme sous la forme suivante: 

```
--- Full Bin ---
Navettes nécessaires (3):
#1: Hendrikx, Beaupere - emplacements vides = 0 
#2: Lauwers, Lorquet - emplacements vides = 0
#3: Carbonara, Mathy - emplacements vides = 0
```

**Consignes:**
- Dans le module `model`, créez les classes `Family` et `Bus`. A vous de les définir.
- Dans le module `algorithms`, créez la classe `Result` (que vous devrez définir) ainsi que l'implémentation de chaque 
algorithme dans sa propre fonction. Ces fonctions retourneront un objet de type `Result`.


## Pour aller plus loin
- Gérez les cas d'erreur (e.g.: le nombre de navettes est insuffisant, ...)
- Rédigez les tests unitaires pour chaque algorithme implémenté.


## Exemple de déroulement du programme

```
Quelle capacité par navette ? 7

--- First Fit ---
Navettes nécessaires (4) :
#1: Mathy, Beaupere, Lorquet - emplacements vides = 1
#2: Carbonara - emplacements vides = 3
#3: Hendrikx - emplacements vides = 1
#4: Lauwers - emplacements vides = 2

--- First Fit Decreasing ---
Navettes nécessaires (3) :
#1: Hendrikx, Beaupere - emplacements vides = 0
#2: Lauwers, Lorquet - emplacements vides = 0
#3: Carbonara, Mathy - emplacements vides = 0

--- Full Bin ---
Navettes nécessaires (3) :
#1: Hendrikx, Beaupere - emplacements vides = 0
#2: Lauwers, Lorquet - emplacements vides = 0
#3: Carbonara, Mathy - emplacements vides = 0

```