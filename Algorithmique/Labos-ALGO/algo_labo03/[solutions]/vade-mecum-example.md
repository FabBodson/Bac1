# Vade-mecum: `propose()`

## Fonctionnement attendu du module

### Description
Analyse la proposition du joueur et renvoie un message lui indiquant s’il a trouvé le nombre mystère ou pas. La méthode met également l’état de l’objet `GuessGame` à jour.

Cette méthode fait partie de la classe `GuessGame`, dotée des attributs suivants :
    
- `mystery_number`, entier, le nombre à trouver
- `minimum`, entier, borne inférieure du nombre mystère
- `maximum`, entier, borne supérieure du nombre mystère
- `max_trials`, entier, le nombre de trials autorisées pour deviner le nombre mystère
- `trials`, entier, le nombre actuel de trials réalisées
- `proposed_numbers`, liste d'entiers, tableau des nombres déjà proposés par le joueur
- `messages`, liste de textes, tableau des messages-types à transmettre au joueur
- `end`, booléen, indique si le jeu est fini ou pas.

### Données d’entrées
- `proposal`: nombre entier proposé par le joueur (IN)
- Attributs de la classe (IN):
    - `mystery_number`
    - `minimum`
    - `maximum`
    - `max_trials`
    - `trials`

### Pré-conditions
Aucune, car tous les cas de figure doivent mener à un message spécifique en résultat.


### Données de sorties
- `message`, texte, message à transmettre au joueur (OUT)
- Attributs de la classe (IN/OUT):
    - `trials`
    - `proposed_numbers`
    - `end`

### Post-condition (ensures)

Soient les messages suivants :
- message #1 = "Bravo! ;-))"
- message #2 = "Le nombre mystère est plus grand"
- message #3 = "Le nombre mystère est plus petit"
- message #4 = "Veuillez proposer un nombre compris entre {minimum} et {maximum} inclus "
- message #5 = "Vous avez épuisé vos {max_trials} trials ;-(\n Le nombre mystère vaut {mystery_number}"

Le résultat répondra aux conditions suivantes:
- Proposition erronée : proposal < minimum OU proposal > maximum => message #4
- Fin de partie
    - Gagné : trials <= max_trials ET proposal == mystery_number => message #1, mise à jour de trials, proposed_numbers et end
    - Perdu : trials == max_trials ET proposal != mystery_number => message #5, mise à jour de trials, proposed_numbers et end
- Trop petit : trials < max_trials ET proposal < mystery_number => message #2, mise à jour de trials, proposed_numbers
- Trop grand : trials < max_trials ET proposal > mystery_number => message #3, mise à jour de trials, proposed_numbers


### Prototype

```python
def propose(proposal: int) -> str:
    """
    Analyse la proposition du joueur et renvoie un message lui indiquant s’il a trouvé le nombre mystère ou pas
    :param proposal: int, nombre proposé par le joueur
    :return: texte, message adressé au joueur
    """
```



### Plan de tests

- Echantillon des différents cas distingués par l'algorithme
    - Nombre proposé invalide (< minimum ou > maximum) => message[3] et (trials reste à 0, proposed_numbers ne contient pas le nombre invalide, le jeu n’est pas fini)
        - minimum = 0, maximum = 10, proposal = -3
        - minimum = 0, maximum = 10, proposal = 11
    - Nombre mystère trouvé => gagné : minimum = 0, maximum = 10, première tentative, max_trials = 5, mystery_number = 3, proposal = 3
    - Nombre mystère trouvé => gagné : minimum = 0, maximum = 10, seconde tentative, max_trials = 5, mystery_number = 3, proposal = 3
    - Nombre mystère trouvé => gagné : minimum = 0, maximum = 10, dernière tentative, max_trials = 5, mystery_number = 3, proposal = 3
    - Nombre mystère jamais trouvé => perdu : minimum = 0, maximum = 10, trials = 4, max_trials = 5, mystery_number = 3, proposal = 2
    - Nombre mystère plus grand : minimum = 0, maximum = 10, trials <=3 , max_trials = 5, mystery_number = 3, proposal = 1
    - Nombre mystère plus petit: minimum = 0, maximum = 10, trials <=3, max_trials = 5, mystery_number = 3, proposal = 5
- Cas d'erreurs reconnues et traitées par le programme
    - Nombre proposé invalide (< minimum ou > maximum) : déjà prévu ci-dessus
- Cas limites
    - valeur nulle/ensemble vide: minimum = 0, maximum = 0, mystery_number = 0, proposal = 0 => gagné 
    - valeur nulle/ensemble vide: minimum = 0, maximum = 0, trials = 0, max_trials = 5, mystery_number = 3, proposal = 3 => invalide
    - première valeur de l’intervalle: minimum = 0, maximum = 10, trials <=4, max_trials = 5, mystery_number = 0, proposal = 0 => gagné 
    - dernière valeur de l’intervalle: minimum = 0, maximum = 10, trials <= 4, max_trials = 5, mystery_number = 10, proposal = 10 => gagné
    - on a bien droit au nombre max de trials avant de perdre : minimum = 0, maximum = 10, trials = 4, max_trials = 5, mystery_number = 4, proposal = 5 => perdu
- Valeurs extrêmes, pour la détection des dépassements de capacité dans les calculs. trials = 4, max_trials = 5 => gagné
- Plusieurs cas « normaux » c’est-à-dire n’entrant pas dans les catégories précédentes : tous les cas possibles ont déjà été testés.
- Le plus difficile: un maximum de combinaisons de cas.  
    - Intervalle à un seul nombre : déjà testé
    - Nombre mystère jamais trouvé  et de valeur nulle => perdu : minimum = 0, maximum = 10, trials = 4, max_trials = 5, mystery_number = 0, proposal = 2
    - …


## Idée

### Description
Tester les cas de figure listés dans les post-conditions, en les organisant au mieux pour éviter les redondances de code.

### Organigramme ou pseudo-code

```
Si proposal est non valide
Alors 
    renvoyer message #4 
Incrémenter trials 
Si le joueur n’a pas épuisé ses trials
Alors 
    ajouter proposal à proposed_numbers

    # Gagné
    Si proposal == mystery_number
    Alors 
        end = true
        renvoyer message #1
    
    # Perdu
    Si trials == max_trials ET proposal != mystery_number 
    Alors
        end = true
        renvoyer message #5
    
    # Trop petit
    Si trials < max_trials ET proposal < mystery_number
    Alors
        renvoyer message #2
    
    # Trop grand
    Si trials < max_trials ET proposal > mystery_number
    Alors
        renvoyer message #3
    Sinon
        renvoyer ""
```

