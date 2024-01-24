# Labos 01, Exercice 12 : remplir un tableau de statistiques

**Durée estimée : 20 min**

Ecrivez une fonction qui remplirait un tableau de statistiques à deux dimensions, passé en paramètre, avec le nombre de buts marqués 
et encaissés durant les matchs pour les équipes participantes.

Tel que :
	stats[n_equipe][0] ==> Nombre de buts marqués par l'équipe n
	stats[n_equipe][1] ==> Nombre de buts encaissés par l'équipe n

**Fonction:**
```python
	def update_goals_stats(team_a, team_b, stats, game):
		pass
```
**Exemple de résultats attendus :**

- `update_goals_stats(4,3,stats,[4,3,0,2]) == `
		`stats[4][0] = stats[4][0] + 0`	//Team_a goal marqué
		`stats[3][0] = stats[3][0] + 2`	//Team_b goal marqué
		`stats[4][1] = stats[4][1] + 2`	//Team_a goal encaissé
		`stats[3][1] = stats[3][1] + 0`	//Team_a goal encaissé
