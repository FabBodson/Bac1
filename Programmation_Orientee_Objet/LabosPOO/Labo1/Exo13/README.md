# Labos 01, Exercice 13 : remplir un tableau de statistiques

**Durée estimée : 20 min**

Ecrivez une fonction qui remplirait un tableau de statistiques à deux dimensions, passé en paramètre, contenant la différence entre les nombres 
de buts marqués et encaissés durant les matchs pour les équipes participantes.

Tel que:
	stats[n_equipe][2] ==> Différence entre buts marqués et buts encaissés par l'équipe n

**Fonction:**
```python
	def update_goal_diff(stats):
		pass
```
**Exemples de résultats attendus :**

- `update_goal_diff(stats) == `
		`stats[4][2] = stats[4][0] - stats[4][1]`	//Team_a goal marqués - Team_a goal encaissés
