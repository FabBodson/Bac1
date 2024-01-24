# Labo 01, exercice 15 : classement d'un tournoi

**Durée estimée** : 30 min plus travail à domicile

Nous organisons un tournoi de football où chaque équipe se rencontre. Dans ce tournoi, une victoire rapporte 2 points, un match nul rapporte 1 point et une défaite ne rapport aucun point. 

Vous devez calculer le classement du tournoi après certains matchs. Ce classement est calculé selon trois critères :

- d'abord les points récoltés ;
- en cas d'égalité, la différence entre les goals inscrits et ceux concédés ;
- en cas d'égalité, les goals inscrits.

Écrivez une fonction à cette fin. La fonction `compute_ranking` prend en paramètre le nombre d'équipes inscrites et une liste contenant d'autres listes. Chaque sous-liste représente un match de la façon suivante `[indice de l'equipe A, indice de l'équipe B, goals de l'équipe A, goals de l'équipe B]`. Par exemple [0, 5, 2, 2] représente le match *Équipe 0 - Équipe 5* dont le score est *2 : 2*.

Votre fonction retournera une liste où l'élément d'indice i est le rang qu'occupe l'équipe i dans le classement.

Exemple : soient 6 équipes ayant déjà joué 9 matchs.
```python
number = 6
games = [[0, 5, 2, 2],   // Team 0 - Team 5 => 2:2
         [1, 4, 0, 2],   // Team 1 - Team 4 => 0:2
         [2, 3, 1, 2],   // Team 2 - Team 3 => 1:2
         [1, 5, 2, 2],   // Team 1 - Team 5 => 2:2
         [2, 0, 1, 1],   // Team 2 - Team 0 => 1:1
         [3, 4, 1, 1],   // Team 3 - Team 4 => 1:1
         [2, 5, 0, 2],   // Team 2 - Team 5 => 0:2
         [3, 1, 1, 1],   // Team 3 - Team 1 => 1:1
         [4, 0, 2, 0]]   // Team 4 - Team 0 => 2:0
```

Utilisez les fonctions programmées lors des exercices 11, 12, 13 et 14 pour construire une matrice analogue à celle illustrée ci-dessous. Pour trier cette matrice, vous pouvez faire appel à la fonction pré-définie `sorted(iterable[, key:func][, reverse:bool])`. Lisez ce [Manuel d'utilisation](https://wiki.python.org/moin/HowTo/Sorting#Key_Functions) pour apprendre comment lui fournir des fonctions de comparaison adaptées.

| Rang |Equipe  | Insc. : Pris  | Diff. Buts |Points |
|------|--------|---------------|------------|-------|
|0 	   |      4 | 5 : 1         | +4         | 5
|1 	   |      5 | 6 : 4         | +2         | 4
|2 	   |      3 | 4 : 3         | +1         | 4
|3     |      0 | 3 : 5         | -2         | 2
|3 	   |      1 | 3 : 5         | -2         | 2
|5 	   |      2 | 2 : 5         | -3         | 1

Selon ce classement, votre fonction retournera `[ 3, 3, 5, 2, 0, 1]`. Remarquez que les équipes 0 et 1 occupent le même rang : la position 3 (si on compte à partir de 0).

