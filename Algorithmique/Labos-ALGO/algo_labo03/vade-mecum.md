*Adapté du document original [Vade-Mecum] issu du cours d'algorithmique de Christiane Mathy*.



# 1. Qu’est-ce qu’un Vade-Mecum ?

Définition du Centre National (français) de Ressources Textuelles et Lexicales : 

> **Recueil** contenant des renseignements sur les règles d'un art ou d'une technique à observer ou sur une conduite à suivre, et qu'on garde sur soi ou à portée de main pour le consulter. 

> **Synonymes**: aide-mémoire, mémento, répertoire, guide.

Dans le cadre du cours d’algorithmique, il s’agira d’une sorte de formulaire à compléter, reprenant les bonnes questions à vous poser lorsque vous concevez un programme, une procédure, fonction
ou méthode, et qui respectera un formalisme particulier.

Compléter ce type de document constitue une excellente manière de clarifier et vérifier votre compréhension de l’énoncé, du problème à résoudre ou de l’algorithme à trouver. Idéalement, le
vade-mecum devrait:
- être construit avant d’écrire la moindre ligne de code,
- rester indépendant du langage de programmation qui sera utilisé pour implémenter l’algorithme qu’il décrit.

Une fois complété, le vade-mecum doit toujours correspondre parfaitement au code qui en découle, et ainsi constituer la documentation technique de ce code, ce qui en facilite la lecture et la compréhension a posteriori.
Certains éléments du vade-mecum devraient se retrouver dans la documentation de votre projet (paramètres des méthodes et valeurs de retour, au minimum).



# 2. Contenu d’un Vade-Mecum

## 2.1. Fonctionnement attendu du module (= Quoi ?)

Cette section couvre le fonctionnement attendu du module, du point de vue de celui qui y fait appel, c'est son « mode d’emploi ».

### 2.1.1. Description

Contient: 
- le **nom** du module (procédure, fonction, méthode) que vous documentez - celui-ci peut également faire référence à l’algorithme mis en oeuvre pour peu qu’il soit connu.
- une **courte description** de son rôle (= ce qu’il réalise comme traitement, sans donner aucun détail sur comment il le réalise)
- la **nature du traitement** (à l’aide d’une structure de type vebre + complément d’objet direct + complément d’objet indirect)

**Exemples**
- le module `read_rectangle` se charge de la lecture au clavier d’une longueur et d’une largeur de rectangle
- le module `compute_triangle_area` (ici, le nom seul suffit à décrire le rôle de la fonction)
- le module `search_element` renvoie l’indice d’un élément dans une liste, ou -1 si cet élément n’y est pas
- le module `quick_sort_integers` trie les éléments d’une liste d’entiers, en ordre croissant, selon l’algorithme Quicksort
- le module `binary_search` renvoie l’indice d’un élément dans une liste triée, ou -1 si cet élément n’y est pas, selon l’algorithme de la recherche dichotomique


### 2.1.2. Données d’entrées

Ce sont les données que le module reçoit de son environnement d'exécution pour accomplir son "travail". 

Pour chaque donnée `IN`:
- **nom**: le nom doit être judicieusement choisi, afin d’exposer clairement le rôle de la donnée qu’il étiquette !
- **type**: le type de la donnée (nombre entier, réel, texte)

**Exemples**
- `salary` : nombre réel à 2 décimales (IN)
- `student` : objet de la classe `Student` (`last_name` : texte, `first_name` : texte, `points` : liste de nombres réels à une décimale) (IN)
- `students_count` : nombre entier (IN)


### 2.1.3. Pré-conditions (requires)

Décrivez à l’aide d’une assertion ou d’une courte phrase les règles que les données d’entrées (IN) doivent satisfaire pour garantir une exécution cohérente du module.
L’exécution est cohérente si les résultats de l’exécution du module sont prévisibles. Le crash d’un programme n’est pas considéré comme un résultat prévisible ;-)
Les données d’entrées et les pré-conditions délimitent la classe de problèmes à résoudre.

**Exemples**
- `salary` > 0
- 0 <= `student.points` <= 20
- Le nom et le prénom de l’étudiant comportent au moins un caractère.

Les préconditions peuvent être reportées dans votre code sous forme d’assertions (e.g.: `assert salary > 0, 'Le salaire doit être supérieur à 0 !'`)


### 2.1.4. Données de sorties

Ce sont:
- les données que le module renvoi à la fin de l'exécution 
- les données d'entrée (IN) que le module modifie durant son exécution

Pour chaque donnée `OUT`:
- **nom**: le nom doit être judicieusement choisi, afin d’exposer clairement le rôle de la donnée qu’il étiquette !
- **type**: le type de la donnée (nombre entier, réel, texte)

**Exemples**
- `(return)`: nombre réel à une décimale (OUT)
- `salary`: nombre réel à 2 décimales (OUT)
- `student` : objet de la classe `Student` (`last_name` : texte, `first_name` : texte, `points` : liste de nombres réels à une décimale) (IN/OUT)


### 2.1.5. Post-condition (ensures)

Décrivez à l’aide d’une assertion ou d’une courte phrase les règles que les paramètres de sortie (OUT) doivent satisfaire à la fin de l’exécution du module. 
Ces règles définissent les paramètres de sortie en fonction de toutes les données d’entrées : il s’agit de formaliser la sémantique du module, sa signification.

**Exemples**
- -5.5 <= `(return)` < 10
- `salary` < 0 en cas de données erronées, sinon salary >= 0
- `student` n'est pas None et contient les informations relatives à l’étudiant de nom recherché
- la liste de points d'un student est triée en ordre croissant


### 2.1.6. Prototype

A ce stade, vous êtes en mesure d’écrire le prototype (signature) du module en combinant le nom donné au module à ses paramètres et valeurs de retour éventuels. Vous pouvez écrire ce prototype en Pseudo-code ou en Python.

**Exemples**
- Python : `def granted_loan(seniority_in_years: int, revenu: float, criminal_record: bool, credit: bool) -> bool`
- Pseudocode : `bool granted_loan(int seniority_in_years, float revenu, bool criminal_record, bool credit)`
- Python : sort(notes: List[float]) -> None 
- Pseudocode : sort(liste d’entiers cotes)


### 2.1.7. Plan de test

La rédaction du plan de test devrait idéalement intervenir avant même d’écrire l’algorithme du module à réaliser. 
Elle peut aussi être réalisée en même temps que le pseudocode, ou, en dernier ressort, après avoir rédigé le pseudocode.

Que doit contenir le plan de test:
- Echantillon des différents cas distingués par l'algorithme. Exemple: si le calcul du salaire dépend du nombre d’enfants à charge, il faut prévoir les cas où il n’y a aucun enfant, un enfant, 2 enfants, …
- Cas d'erreurs reconnues et traitées par le programme. Exemple : si on doit faire une division et que le programme vérifie bien que le diviseur est non nul, il faut quand même tester ce cas.
- Cas limites. Exemples : 
    - valeur nulle
    - première et dernière valeur dans une liste
    - ensemble vide
- Valeurs extrêmes, pour la détection des dépassements de capacité dans les calculs. Exemple : plus grand entier représentable.
- Plusieurs cas « normaux » c’est-à-dire n’entrant pas dans les catégories précédentes.
- Le plus difficile: un maximum de combinaisons de cas. Exemples : 
    - 1 enfant à charge (= un cas distingué par l’algorithme) et salaire de base égal à 0 (= un cas limite), 
    - -1 enfant (= un cas d’erreur) et salaire de base de 10 000€ (=un cas normal)


## 2.2. Idée (= Comment ?)

Cette section aborde le « comment », c’est-à-dire l’algorithme du module, son mode de fonctionnement interne, comment il arrive à produire le résultat annoncé.

### 2.2.1. Description
Décrivez d’abord l’idée principale de la solution imaginée, qui peut être
- la méthode de résolution classique que vous appliquez (comme le tri à bulle, la recherche dichotomique, ...).
- le point de départ de votre algorithme, l’étincelle qui vous a permis de démarrer, de savoir comment résoudre le problème posé.
- la caractéristique ou le théorème sur lequel vous vous êtes appuyé
- etc.

Il ne s’agit pas de décrire complètement votre solution, mais bien de mettre en évidence son inspiration.

**Exemples**
- Formule de calcul du salaire fournie par la commission paritaire
- Théorème d’Euclide sur les nombres premiers


### 2.2.2. Organigramme ou pseudo-code
Présenter votre algorithme de résolution à l’aide d’un organigramme ou de pseudo-code. 

L’idéal est d’obtenir un algorithme indépendant du langage de programmation qui sera employé pour le mettre en oeuvre, même si à ce stade, on connait déjà certains éléments techniques (programmation orientée objets par exemple).

Pour vous aider, vous pouvez exprimer le pseudo-code sous la forme “Pour `objectif`, il faut `actions`”.

> L'idée est d'arriver à expliquer l'algorithme à un enfant de six ans - *N. Hendrikx*


### 2.2.3. Données de travail
Si vous devez manipuler des variables supplémentaires, afin de mémoriser des résultats intermédiaires ou d’améliorer la lisibilité de l’algorithme par exemple, mentionnez leur nom et leur
type. Le nom choisi doit faire clairement apparaître le rôle joué par la variable.

**Exemples**
- `brut_salary` : nombre réel à une décimale
- `new_name` : texte
- `index_middle` : int

