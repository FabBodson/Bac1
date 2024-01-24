# Labo 01, exercice 09 : Transposition de notes

**Durée estimée** : 20 minutes

Vous êtes compositeur et vous venez d'écrire une superbe mélodie. 

Vous devez la présenter à votre groupe, mais il y a un problème: le chanteur n'atteint pas toutes les notes de celle-ci, 
et vous devez donc la transposer.

Soient une liste de notes (représentées sous la forme de texte) et une intervalle, retournez une liste des notes transposées.

**Contraintes:**
- Les notes utilisées sont les suivantes: do, do#, re, re#, mi, fa, fa#, sol, sol#, la, la#, si
- L'intervalle peut prendre toutes les valeurs comprises entre -12 et 12 inclus.

**Transposition**
- Transposer la note `do` d'une intervalle positive de 1 signifie l'augmenter d'un demi-ton. `do` devient alors `do#`.
- Transposer la note `do` d'une intervalle positive de 3 signifie l'augmenter d'un ton et demi (la tierce). `do` devient alors `re#`.
- Transposer la note `do` d'une intervalle positive de 12 signifie l'augmenter de 12 demi-tons (l'octave). `do` reste alors `do`
- Transposer la note `do` d'une intervalle négative de 1 signifie la diminuer d'un demi-ton. `do` devient alors `si`.

**Fonction:** 

```python
def transpose(song, interval):
  pass
```

Exemples de résultats attendus :

- `transpose(['sol'], 5) == ['do']`
- `transpose(['do#'], -4) == ['la#']`
- `transpose(['mi', 'fa']), 1) == ['fa', 'fa#']`
 
