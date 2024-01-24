# Programmation Orientée Objet : rappels et limites des fonctions

Durée prévue : 4 heures

Ce laboratoire rappelle les principales notions vues dans le cadre de l'Activité d'Apprentissage *Programmation de base*. Il vise à rendre capable de :

- Définir des fonctions en Python ;
- Appeler des fonctions en Python ;
- Valider des fonctions avec le module unittest ;
- Valider des fonctions avec un outil d'analyse statique simple ;
- Manipuler des listes et des tuples en Python.

15 exercices de difficultés croissantes sont prévus. Chaque énoncé est accompagné d'un ou plusieurs exemples montrant les résultats attendus. Attention, certains cas limites ne sont pas illustrés. N'hésitez pas à les ajouter. 

Une solution sera composée de la définition de la fonction et de tests réalisés comme en Programmation de Base. Une **bonne** solution doit être lisible. Nous mesurerons la lisibilité à l'aide de 3 éléments observables :

- L'utilisation de noms parlants, issus du domaine étudié ;
- le nombre de lignes de code logique (*Logical Line Of Code*, *LLOC*) par fonction qui doit être inférieur ou égal à 10 ;
- le nombre de chemins d'exécution que les appels peuvent prendre par fonction, cette mesure correspond à la complexité cyclomatique (*Cyclomatic Complexity*, *CC*) et elle doit être inférieure ou égale à 9. Nous calculons CC à l'aide de l'outil Radon (voir ci-dessous).

Enfin, une bonne solution doit être efficace en temps d'exécution et/ou d'espace mémoire. Elle doit minimiser le nombre d'itérations exécutées par un appel dans des cas "extrêmes".

## Exercices

### Série 1 : rappels sur les opérateurs et les structures de contrôle

Ces exercices se focalisent sur les opérateurs et les structures de contrôle. Bien qu'utilisables comme variables locales, les listes et les tuples ne sont pas indispensables.

- [Exercice 01 : somme des impairs structurés en triangle](Exo01/README.md)
- [Exercice 02 : le plus grand diviseur avant N](Exo02/README.md)
- [Exercice 03 : addition binaire](Exo03/README.md)
- [Exercice 04 : les nombres forts](Exo04/README.md)
- [Exercice 05 : les nombres équilibrés](Exo05/README.md)

### Série 2 : manipulation de séquences

Ces exercices travaillent sur les séquences et plus particulièrement sur les listes et les tuples. Pour les réaliser, vous devrez parcourir des séquences et accéder à un élément sur base de sa position.

- [Exercice 06 : compter les lapins](Exo06/README.md)
- [Exercice 07 : qui a été sage pour Noël ?](Exo07/README.md)
- [Exercice 08 : voyages d'affaire](Exo08/README.md)
- [Exercice 09 : transposition de notes](Exo09/README.md)
- [Exercice 10 : convertir en CamelCase](Exo10/README.md)

### Série 3 : intégration

Cette dernière série consiste à définir plusieurs fonctions qui seront intégrées dans le dernier exercice pour construire le classement d'un tournoi.

- [Exercice 11 : calculer les points](Exo11/README.md)
- [Exercice 12 : remplir un tableau de statistiques A](Exo12/README.md)
- [Exercice 13 : remplir un tableau de statistiques B](Exo13/README.md)
- [Exercice 14 : remplir un tableau de statistiques C](Exo14/README.md)
- [Exercice 15 : classement d'un tournoi](Exo15/README.md)


## Préalable : installation de l'outil radon (~10 minutes)

Nous supposons que l'interpréteur Python (3.7.0 ou supérieure) et l'outil Pip soient installés. Ouvrez un terminal est écrivez la commande `pip install radon`. Une fois l'installation effectuée, vous pouvez la valider à l'aide de la commande `radon -v`. Cette commande affiche la verion de radon installée, par exemple `4.0.0`.

### Calculer la complexité cyclomatique des fonctions

Toujours dans un terminal, changez le répertoire courant pour atteindre le répertoire racine du votre projet, par exemple `c:\TEMP\Poo\labo01`. Supponsons que l'exercice 1 soit terminé. Écrivez la commande `radon cc Exo01\exo01.py` pour que radon affiche la CC des fonctions définies dans ce fichier.

```bash
$c:\TEMP\Poo\labo01> radon cc .\Exo01\exo01.py
.\Exo01\exo01.py
    F 1:0 sum_of_terms - A
```
Le `F` signifie que l'élément évalué est une fonction. La paire 1:0 signifie que la fonction commmence à la 1ère ligne, colonne 0. Enfin, la lettre A est un rang de qualité correspondant à une CC comprise entre 1 et 5. **Vous devez essayer de garder ce rang en dessous de la lettre B**.

| CC  score |	Rank |	Risk                                   |
|-----------|--------|-----------------------------------------|
| 1 -  5    |	A    | low - simple block 
| 6 - 10    |	B    | low - well structured and stable block
|11 - 20    |   C    | moderate - slightly complex block
|21 - 30    |   D    | more than moderate - more complex block
|31 - 40    |   E    | high - complex block, alarming
|41+        |   F    | very high - error-prone, unstable block
