# Labos 01, Exercice 14 : remplir un tableau de statistiques

**Durée estimée : 20 min**

Ecrivez une fonction qui remplirait un tableau de statistiques à deux dimensions, passé en paramètre, 
avec le nombre de points accumulés lors de chaque match.        

Tel que:
	stats[n_equipe][3] ==> Nombre de points accumulés par l'équipe n

**Fonction:**
```python
	def update_points_stats(team_a, team_b, stats, game):
		pass
```
**Exemples de résultats attendus :**

- `update_points_stats(4,2,stats,game=[4,2,0,1]) == `
		`stats[4][3] = stats[4][3] + 0`	
        //Team_a points obtenus lors de la rencontre 
		`stats[2][3] = stats[2][3] + 2`	
        //Team_b points obtenus lors de la rencontre 
