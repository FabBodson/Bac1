# Vade-mecum: `apply_merge_sort()`

## Fonctionnement attendu du module

### Description
Trie une collection d'élements selon l'algorithme du tri fusion sans modifier la liste originale et renvoie le résultat sous la forme d'une nouvelle collection.

### Données d’entrées
- `collection`: liste d'éléments triables par l'opérateur booléenne "plus petit ou égal". (IN)

### Pré-conditions
- `collection` doit être itérable
- `collection` doit être numériquement indexable (accessible via index numérique)

### Données de sorties
- `(return)`, liste, nouvelle liste d'éléments triés dans un ordre croissant (OUT)

### Post-condition (ensures)
- `collection` n'est pas modifiée durant le processus
- `(return)` contient uniquement les éléments de `collection`
- `(return)` contient tous les éléments de `collection`, y compris les doublons
- `(return)` est une liste triée dans un ordre croissant

### Prototype

```python
def apply_merge_sort(collection):
    """
    This function applies the merge sort algorithm to the collection (list) in argument. The original list will not be modified.
    :param collection: list, a collection of any sortable items.
    :return: list, the sorted collection.
    """
```

### Plan de tests

- collection d'un nombre pair d'éléments
- collection d'un nombre impair d'éléments
- collection vide
- collection contenant 1 seul élément
- collection contenant des doublons 
- collection contenant 1000 éléments 

## Idée

### Description
Implémentation de l'algorithm de tri fusion.

### Organigramme ou pseudo-code

```
    Si taille collection = 0 alors retourner liste vide
    Si taille collection = 1 alors retourner une nouvelle liste contenant le premier élément

    Calculer l'indice du milieu et stocker le résultat dans "indice milieu" 

    Appliquer le tri fusion à la partie gauche d'"indice milieu" et stocker le résultat dans "gauche"
    Appliquer le tri fusion à la partie droite d'"indice milieu" et stocker le résultat dans "droite"

    Fusionner "gauche" et "droite" et stocker le résultat dans "résultat"
    retourner "résultat"
```

### Variable de travail

- `middle_index`: index de l'élément se trouvant au milieu
- `left`: sous collection se trouvant à gauche de l'indice du milieu
- `right`: sous collection se trouvant à droite de l'indice du milieu
