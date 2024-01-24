# Labos 01, Exercice 11 : connaitre les points gagnés par des équipes lors d'un match

**Durée estimée : 15 min**

Ecrivez une fonction qui renverrait, sous forme de tuple, les points gagnés lors d'un match par chacune des équipes :

Une victoire rapporte 2 points, un match nul rapporte 1 point et une défaite ne rapport aucun point. 


Soit un tableau d'entiers nommé `game`, qui contient le résultat d'une rencontre en 2 équipes tel que:

game = [0, 5, 3, 1]   // Team 0 => 3 buts marqués - Team 5 => 1 but marqué

**Fonction:**
```python
	def points_for(game):
		pass
```
**Exemples de résultats attendus :**

	- `points_for([0,5,3,1]) == (2,0)`
	- `points_for([4,2,0,1]) == (0,2)`
	- `points_for([2,3,0,0]) == (1,1)`
