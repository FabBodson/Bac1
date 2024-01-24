# Labo 01, exercice 07 : Qui a été sage pour Noël ?

**Durée estimée** : 15 minutes

Aidez le Père Noël a déterminer qui mérite un cadeau le jour J. Parcourez la liste des enfants (`children`), et retournez une 
liste contenant chaque nom apparaissant sur la liste du Père Noël (`santas_list`).

**Notes:** 
- Un nom ne peut pas être ajouté plus d'une fois à la liste.
- La liste retournée doit être triée par ordre alphabétique.

Fonction: 

```python
def find_children(santas_list, children):
  pass
```

Exemples de résultats attendus :

- `find_children(santas_list=['Nicolas', 'Dorian', 'Cyril'], children=['Nicolas', 'Cyril']) == ['Cyril', 'Nicolas']`
- `find_children(santas_list=['Nicolas', 'Cyril'], children=['Cyril', 'Dorian', 'Nicolas']) == ['Cyril', 'Nicolas']`
- `find_children(santas_list=['Nicolas', 'Cyril'], children=['Cyril', 'Nicolas', 'Nicolas']) == ['Cyril', 'Nicolas']`