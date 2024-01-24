# Vade-mecum: `__merge()`

## Fonctionnement attendu de la fonction

### Description

Parcours les éléments de chaque sous-liste et positionne le plus petit élément dans la `collection`.\

### Données d’entrées

- `left`: sous-liste, collection d'éléments triables, partie gauche de `collection`.
- `right`: sous-liste, collection d'éléments triables, partie droite de `collection`.
- `collection`: liste contenant les éléments à trier.

### Pré-conditions

Avoir des listes contenant des éléments triables.

### Données de sorties

Une liste triée fusionnant la partie gauche et la partie droite.

### Post-condition (ensures)

La liste en sortie est triée.

### Prototype

Exemple:
```python
def __merge(left, right):
    """
    This function merges two lists into a new (third) one. The resulting list will be sorted using the merge sort algorithm.
    :param left: list, a collection of any sortable items.
    :param right: list, a collection of any sortable items.
    :return: list, the sorted collection resulting from the merge of left and right.
    """
```


### Plan de tests

- Echantillon des différents cas distingués par l'algorithme
    
- Cas d'erreurs reconnues et traitées par le programme

- Valeurs extrêmes
 
- Plusieurs cas « normaux » c’est-à-dire n’entrant pas dans les catégories précédentes.

- Le plus difficile: un maximum de combinaisons de cas.


## Idée

### Description

Utilisation de l'algorithme de tri fusion, appliqué à la `collection`.\

### Organigramme ou pseudo-code

````
lonG vaut la longueur de la liste de gauche
lonD vaut la longueur de la liste de droite
collection est la liste qui contiendra les éléments triés et qui sera retournée
i, j= 0, 0 -> indices des boucles

TANT QUE i plus petit que lonG ET j plus petit que lonD
FAIRE
    SI l'élément de de la liste de gauche à la pos i est plus petit ou egal à l'élément de la liste de droite à la pos j
    FAIRE
    ajouter l'élément à la pos i dans collection
    mise à jour i

    SINON
    FAIRE 
    ajouter l'élément à la pos j dans collection
    mise à jour j

    FIN SI
FIN TANT QUE

TANT QUE i plus petit que lonG
FAIRE 
    ajouter l'élément à la pos i dans collection
    mise à jour i
FIN TANT QUE

TANT QUE j plus petit que lonD
FAIRE 
    ajouter l'élément à la pos j dans collection
    mise à jour j
FIN TANT QUE

````