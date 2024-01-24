# Vade-mecum: `apply_merge_sort()`

## Fonctionnement attendu de la fonction

### Description

Permet de trier un tableau.\
Argument:
- `collection`: liste, collection d'éléments triables.

### Données d’entrées

- `collection`: liste contenant des éléments à trier.

### Pré-conditions

Avoir une liste contenant des éléments triables.

### Données de sorties

Une liste triée fusionnant la partie gauche et la partie droite de la `collection`.

### Post-condition (ensures)

La liste en sortie est triée.

### Prototype

Exemple:
```python
def apply_merge_sort(collection):
    """
    This function applies the merge sort algorithm to the collection (list) in argument. The original list will not be modified.
    :param collection: list, a collection of any sortable items.
    :return: list, the sorted collection.
    """
```


### Plan de tests

- Echantillon des différents cas distingués par l'algorithme
    - Liste contenant 1 élément => Retourner la liste.
    - Liste contenant plus de 1 élément:
        - Retourner la liste triée.
    
- Cas d'erreurs reconnues et traitées par le programme
    - Liste vide => Retourner la liste vide.

- Valeurs extrêmes
    - L'algorithme de tri fusion s'arrete lorsque qu'il ne reste plus que 1 élément dans une sous-liste
 
- Plusieurs cas « normaux » c’est-à-dire n’entrant pas dans les catégories précédentes.

- Le plus difficile: un maximum de combinaisons de cas.


## Idée

### Description

Utilisant l'algorithme de tri fusion, je vais l'appliquer à la `collection`.\
Séparer la `collection` en 2 à partir de son milieu. Trier chaque sous-liste.\
Au moyen de la récursivité, ré-appliquer l'algorithme à chaque sous-liste jusqu'à obtenir une liste de 1 élément.

### Organigramme ou pseudo-code

````
n vaut la longueur de la collection
Si la collection n'a que 1 élément, 
retourner la collection

Sinon
milieu vaut la moitié de la taille de la collection
left est la partie gauche de la collectin
right est la partie droite de la collection

Appel récursif de la fonction sur la partie gauche et sur la partie droite
Fusionner les 2 parties

````