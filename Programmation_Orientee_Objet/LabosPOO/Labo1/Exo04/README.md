# Labo 01, Exercice 04 :  les nombres forts

**Durée estimée** : 15 minutes

Un entier N est fort si la somme des factorielles de ses chiffres vaut N. 

Écrivez une fonction `is_strong` déterminant si un nombre N est fort.

Exemples :

- is_strong(1) == True
- is_strong(2) == True
- is_strong(145) == 1! + 4! + 5! = 1 + 24 + 120 == 145 == True
- is_strong(40585) == True
- is_strong(7) == False
- is_strong(93) == False
- is_strong(185) == False
- is_strong(2999999) == False