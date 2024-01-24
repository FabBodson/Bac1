# Labo 01, Exercice 05 : les nombres équilibrés

**Durée estimée** : 15 minutes

Un entier N est équilibré si et seulement si la somme des chiffres à gauche des chiffres centraux équivaut à la somme des chiffres à droite des chiffres centraux.

Si l'entier N est composé par un nombre impair de chiffres, alors il n'y a qu'un chiffre central. Par exemple, le chiffre central de 12345 est 3 et le chiffre central de 323 est 2. Si l'entier N est composé par un nombre pair de chiffres, alors il y a deux chiffres centraux. Par exemple, les chiffres centraux de 123456 sont 3 et 4 et les chiffres centraux de 23 sont 2 et 3.

Écrivez une fonction `balanced_num` qui retourne le texte "balanced !!!" si le nombre est équilibré et "not balanced" sinon.

Exemples de résultats attendus :

- `balanced_num (959) == "balanced !!!"`
- `balanced_num (27102983) == "not balanced"`
- `balanced_num (7) == "balanced !!!"`
