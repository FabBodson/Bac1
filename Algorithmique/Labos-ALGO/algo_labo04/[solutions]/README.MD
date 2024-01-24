# Algorithmique : doublons et arbres binaires  
  version 0.11 - release 20200511.FC  

Durée prévue : 4 heures


## Doublons  

	Bien souvent dans des collections se trouvent des données identiques qui sont 
	présentent plusieurs fois, elles sont alors nommées doublons.
	Les résultats d'algorithmes utilisant des collections de données, cherchent
	souvent à éviter les doublons qui peuvent alors induire des fonctionnements
	indésirables.

## Arbres binaires 	
	Un arbre binaire est une structure de données qui peut se représenter sous 
	la forme d'une hiérarchie dont chaque élément est appelé noeud, le noeud 
	initial étant appelé racine. 
	Dans un arbre binaire, chaque élément possède au plus deux éléments fils 
	au niveau inférieur, habituellement appelés gauche et droit. 
	Du point de vue de ces éléments fils, l'élément dont ils sont issus au 
	niveau supérieur est appelé père.

    Au niveau le plus élevé il y a donc un noeud racine. 
    Au niveau directement inférieur, il y a au plus deux noeuds fils. 
    Un noeud n'ayant aucun fils est appelé feuille. 
    Le nombre de niveaux total, autrement dit la distance entre la feuille la 
    plus éloignée et la racine, est appelé hauteur de l'arbre.

    Le niveau d'un noeud est appelé profondeur.
     
	(webographie : wikipedia)	
	
 [Les arbres binaires - version détaillée](https://fr.wikipedia.org/wiki/Arbre_Binaire)  
 [ABR - Arbre binaire de recherche](https://fr.wikipedia.org/wiki/arbre_binaire_de_recherche)	
	

## Mise en place
- Depuis PyCharm, créez un nouveau projet nommé `algo-labo04`. Assurez-vous que celui-ci dispose de son propre environnement virtuel.
- Dans ce projet, vous créerez un module exécutable Python nommé `main.py`, ainsi que les modules `algorithms` et `binary_tree`.


## Exercices en laboratoire
#### Les doublons :
Enoncé :     
  
    1. Renvoyer un valeur booléenne indiquant si une liste passée en paramètre contient un doublon.
       Vrai si liste contiend un doublon et faux dans le cas contraire 
       A. Ecrire le code en python. 
       B. Noter la complexité de votre algorithme O(n).
       C. Voyez s'il est possible d'optimiser votre algorithme.

Prototypes :    
    
    1.A.
     def has_duplicates(collection: List) -> bool  

Exemple de déroulement du programme
```
Bonjour, recherche un doublon dans une liste.
Entrer une liste de valeurs séparées par une virgule : camion voiture moto vélo grue hoverboard hoverboard
01.Votre liste contient-elle une doublon ?  True
02.Votre liste contient-elle une doublon ?  True
03.Votre liste contient-elle une doublon ?  True

Process finished with exit code 0
```       

#### Les arbres binaires :
Enoncé : 
      
    1. Réaliser une classe pour la gestion d'un objet node (arbre binaire). 
	2. Implémenter l'ajout d'un noeud dans cet objet. 
	3. Implémenter la suppression d'un noeud dans cet objet. 
	   Vous devrez sans doute utiliser une méthode objet intermédiaire qui 
	   effectuera une recherche dans l'arbre binaire. 
	   
	4. Amélioration de vos algorithmes : 
		. Permettre l'utilisation des opérateurs + et - sur l'objet. 
		. Gérer les cas limites (noeud vide, valeur de noeud déja existante...)

    5. Renvoyer la profondeur d'un noeud (~ son etage 0 = racine et puis on compte)  
       A. Ecrire le code en Python
       B. Noter la complexité de votre algorithme O(n).   

    6. Renvoyer la hauteur de l'arbre ( ~ distance entre la racine et la feuille la plus basse)
       A. Ecrire le code en Python
       B. Noter la complexité de votre algorithme O(n).    

    7. Renvoyer le nombre de noeuds total dans l'arbre. 
       avec un argument sélectionne les noeuds : Tous , avec 1 ou 2 enfants, uniquement les feuilles
       et un second argument qui définit le noeud (par défaut, c'est la racine)
       A. Ecrire le code en Python
       B. Noter la complexité de votre algorithme O(n).    
       
    8. Renvoyer les statistiques de la synchronicité entre deux noeuds 
       évaluer : le total des valeurs du noeud et des fils (jusqu'à la feuille) 
                 le nombre de noeud total 
                 le nombre de noeud avec 1 ou 2 enfants
                 le nombre de feuilles
                 la profondeur des noeuds évalués 
                     
    9. Inverser l'arbre au niveau de sa logique.
       A. comment définir la logique de l'arbre ?     		
       B. eccrire le code en Python 
       C. Noter la complexité de votre algorithme O(n).
       

Prototypes :    
    
    1.        
    2.
    3.
    4.
    5.
    6.
    7.
    8.
    9.B. Node_Reverse() <-- none 


Exemple de déroulement du programme
```
Bonjour, 
 - Les arbres binaires - (1)
 (2) 
 Entrer une liste de valeurs numériques séparées par un espace, correspondante à votre arbre binaire.
 Liste : 89 120 52 31 11 92 77 71 145 46 83 9 14 65 75 79 85 76 69 78 80 86

 (3) Entrez une valeur à supprimer : 77  
 (5) Profondeur d'un noeud 
     Entrez la valeur d'un noeud : 79
     La profondeur du noeud -79- est de - 4 - (Niv.0 = racine.valeur 89)
 (6) La hauteur de votre arbre est de - 5 - 
 (7) Le nombre de feuille de votre arbre est de - 10 -
     Le nombre de noeud ayant 1 fils est de - 4 - 
     Entrez une valeur : 83
     Que souhaitez-vous connaitre ? 
     (T=Tous,N=Noeud 2 fils, n=noeud 1 fils, f=feuilles) : n  
     Le nombre de noeud ayant 1 fils à partir du noeud - 83 - est de - 1 -

 (8) -- Synchronicité ---
     Evaluation de tout l'arbre 
     La somme des valeurs                 = 1533
     Le nombre total de noeud             =   12        # ne pas compter les feuilles
     Le nombre total de noeud avec 1 fils =    3
     Le nombre total de noeud avec 2 fils =    9
     Le nombre total de feuille           =   10  
     La profondeur du noeud               =    5 
     La hauteur du noeud                  =    0 

     Entrez la premier valeur du noeud à évaluer : 31
     Entrez la premier valeur du noeud à évaluer : 71
                     noeud                   - 31 -     - 71 -
     La somme des valeurs                 =    80        285  
     Le nombre total de noeud             =    1          2        
     Le nombre total de noeud avec 1 fils =    0          2
     Le nombre total de noeud avec 2 fils =    1          0
     Le nombre total de feuille           =    3          2
     La profondeur du noeud               =    2          2
     La hauteur du noeud                  =    3          4 

  (9) Liste des noeuds gauche - 89, 52, 31, 11, 9 
      Inverser la logique de l'arbre : Oui
      Liste des noeuds gauche - 89, 120, 145
      Inverser la logique de l'arbre : Oui
      Liste des noeuds gauche - 89, 52, 31, 11, 9

 A bientot. 	 
```       
Schéma de l'arbre selon l'exemple de déroulement du programme  

                                     89
                       /-------------°--------------------\
                      52                                 120
              /-------°-------------\                   /--°--\
             31                     77                 92     145
          /--°---\         /--------°---------\      
         11      46       71                 83
        /--\            /---\           /----°---\
       9   14          65   75         79        85
                         \    \       /-°-\      /
                          69   76    78   80    86

## Mise en oeuvre : 
   Rechercher l'algorithme le plus adapté et évaluer sa complexité.  
   Ecrire le code sous le paradigme de l'orienté objet. 
  
**Consignes :**
- Dans le module `binary_tree`, créez la classe B_Tree et ses méthodes objets.
- Dans le module `algorithms`, créez la fonction `has_duplicate` (voir la partie prototype).
  

## Pour aller plus loin
- Gérez les cas d'erreurs et des limites (un arbre vide, ajouter un noeud dont la valeur n'existe pas,...)
- Rédigez les tests unitaires pour chaque algorithme implémenté.
- Voir les compléments BONUS ci-dessous.

-----------------------------------
## BONUS :
+ ...libérez votre créativité... 
