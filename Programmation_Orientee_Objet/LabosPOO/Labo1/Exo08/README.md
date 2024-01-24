# Labo 01, exercice 08 : Voyages d'affaire

**Durée estimée** : 20 minutes

Combien de journées avons-nous prestés à l'étranger ?

La fonction `days_represented` reçoit une liste de voyages (`trip`). 

Chaque voyage est un tuple de deux nombres entiers (représentant le numéro du jour dans l'année): 
- le jour de départ
- le jour de retour

Ainsi, un voyage du 30 janvier au 2 février inclus sera exprimé comme suit: (30, 33)

**Notes:** 
- Une journée ne peut pas être comptée plus d'une fois. Ainsi, si deux voyages se sont déroulés pendant les mêmes journées, ces journées ne seront comptabilisées qu'une seule fois. 

**Fonction:** 

```python
def days_represented(trips):
  pass
```

Exemples de résultats attendus :

- `days_represented([(3, 3)]) == 1`
- `days_represented([(3, 10), (40, 42), (350, 360)]) == 8 + 3 + 11 == 22`
- `days_represented([(1, 2), (2, 3), (3, 4)]) == 4`
