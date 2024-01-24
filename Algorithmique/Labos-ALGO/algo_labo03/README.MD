# Algorithmique : Tri fusion (Merge Sort)

Durée prévue : 3 heures


## Mise en place
- Depuis PyCharm, créez un nouveau projet nommé `algo-labo03`. Assurez-vous que celui-ci dispose de son propre environnement virtuel.
- Dans ce projet, vous créerez un module exécutable Python nommé `main.py`, ainsi que les modules `algorithm` et `test_algorithm`.


## Objectif
L'objectif de ce laboratoire est de **comprendre**, **documenter**, **implémenter** et **tester** un algorithme de tri: le tri fusion (ou merge sort).

Pour cet algorithme, nous aurons besoin des deux fonctions suivantes:

```python
def apply_merge_sort(collection):
    """
    This function applies the merge sort algorithm to the collection (list) in argument. The original list will not be modified.
    :param collection: list, a collection of any sortable items.
    :return: list, the sorted collection.
    """
    pass
    
def __merge(left, right):
    """
    This function merges two lists into a new (third) one. The resulting list will be sorted using the merge sort algorithm.
    :param left: list, a collection of any sortable items.
    :param right: list, a collection of any sortable items.
    :return: list, the sorted collection resulting from the merge of left and right.
    """
    pass
```


## Mise en oeuvre

### Comprendre
Consultez la [vidéo descriptive](https://www.youtube.com/watch?v=TzeBrDU-JaY) de l'algorithme `Merge Sort`. Regardez-là attentivement en prenant des notes.

### Documenter
Afin de préparer votre implémentation, réalisez un Vade-Mecum complet **pour chacune des fonctions**. 

Veuillez vous référer à:
- la [fiche descriptive du Vade-Mecum](vade-mecum.md).
- l'[exemple de vade-mecum fourni](./vade-mecum-exemple.md).

### Implémenter
Dans le module `algorithm`, réalisez l'implémentation de chaque fonction en respectant les pseudo-codes produits dans vos vade-mecum.

### Tester
Dans le module `test_algorithm`, écrivez les tests unitaires de chaque fonction en respectant les plans de tests établis dans vos vade-mecum.

