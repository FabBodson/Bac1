# Algorithmique : Recherche dichotomique 
  version 0.97 - release 20200428.FC  

Durée prévue : 4 heures


## Recherche dichotomique 

	Algorithme utilisé pour effectuer une recherche dans une liste triée. Cette algorithme renvoit la position de l'élément recherché.
	Cette algorithme compare l'élément avec la valeur de l'élément au milieu de la liste (Taille de la liste = N, 1er recherche portera sur N/2), 
	Soit la valeur comparée est correspondante, la recherche se termine.
	Soit la valeur comparée est inférieure ou supérieure, et la recherche se poursuit sur la partie de la liste pertinente ( de 1 à N/2  ou de N/2+1 à N) 
	Cette algorithme peut être itératif ou récursif. 
	
	Cet algorithme est de complexité Log 2 (N).
	

## Mise en place
- Depuis PyCharm, créez un nouveau projet nommé `algo-labo02`. Assurez-vous que celui-ci dispose de son propre environnement virtuel.
- Dans ce projet, vous créerez un module exécutable Python nommé `main.py`, ainsi que les modules `algorithms`, `file` et `model`.


## Problème
Réalisation de la plateforme : `S.A.G.O.B`    (SPECTRA-ANALYSER-GUST-OLFACTION-BUILDER).

Cette plateforme dotée d'un ensemble de machines hautement technologiques permet de composer un parfum sur base de gouts et d’odeurs appréciés par un utilisateur.

## Mise en oeuvre : 
Il vous est demandé de produire un programme en python qui permettra de piloter et de concevoir les flacons de parfum correspondants aux choix des utilisateurs.	
Au vu de l'architecture technique utilisée sur cette plateforme, ce programme devra être écrit en orienté objet.

### Fonctionnement de la plateforme

Un utilisateur qui se présente dans notre centre s’attend à recevoir un produit cosmétique en relation avec ses gouts, ce produit est un flacon de parfum qui sera composé en fonction des appréciations du gout et des senteurs connues par l’utilisateur. 
Le traitement se faisant durant la nuit, un email sera envoyé à l’utilisateur afin de le prévenir de venir rechercher son élixir dans notre centre.
L’application demande à l’utilisateur d’encoder quelques informations : nom, prénom, tél. et email. 
Ensuite, le programme demande à l’utilisateur de sélectionner ou d’encoder des gouts (nombre de 2) et des odeurs (au nombre de 1) qu’il apprécie tout particulièrement. 

Ces données (gouts et odeur(s)) sont recherchées dans un premier fichier indiquant la posologie, représenté par un nombre de gouttes de l’essence ; le fichier contenant le nom du produit sélectionné (gout/odeur), le nom de l’essence et le nombre de gouttes.
(effectivement afin de constituer un gout/odeur le nombre de goutte d'une essence sera variable)

__Structure du fichier : posologie.csv__

    Nom;Type;essence;nombre de gouttes
    chocolat;G;ESS-BE;2 
    chocolat;G;ESS-EF;1   
    chocolat;G;ESS-FF;3 
    ...
    violette;O;ESS-FZ;3
    violette;O;ESS-DS;2
    violette;O;ESS-RF;1

*Type: O(=odeur) | G (=gout)*  
*Trié selon : NOM, essence*  
*Des doublons existent pour le nom (1ère colonne) et pour l'essence (3ème colonne): une même essence peut être utilisée avec un dosage différent pour produire un autre gout ou une autre odeur !*
   
 
Ensuite, ces mêmes données sont utilisées afin de rechercher dans un second fichier contenant le nom du l’essence et les coordonnées X,Y,Z permettant l'identification de la position physique du contenant (de l'essence) dans l’armoire-OLFA  
 _(ces coordonnées permettent à un bras robotique d’aller prélever le contenant automatiquement)_.
  
__Structure du fichier : olfaxyz.csv__ 

    Essence;X;Y;Z 
    ESS-BE;5;3;2 
    ESS-EF;12;2;1 
    ESS-FF;20;5;3  
    … 
    ESS-FZ;20;7;3 

*Trié selon : Essence*  
 *Pas de doublons sur la colonne Essence* 

Le flacon final contenant la posologie est composé des essences sélectionnées reprenant : 
 +	 les valeurs des emplacements physiques et 
 +	 des valeurs correspondantes au nombre de gouttes. 

L’étiquette du flacon doit aussi comporter une référence composée par les trois premiers caractères des produits/odeurs par ordre chronologique (ex : chocolat, piment, violette -> REF sera « cho-pim-vio »).

Il faudra également veiller à obtenir comme résultat, le nom de l’utilisateur, son adresse email et le nom du flacon qui a été composé pour lui. 
Veiller aussi à ajouter une valeur pour la date du lot qui correspond à la date du jour sous le format suivant : `AAAAMMJJ-SEQ`   (SEQ sur 5 digits)
SEQ est le numéro de séquence traité depuis l’ouverture du programme, sur 5 digits autocomplétés par des ‘0’ à gauche.

**ATTENTION : ce fichier doit pour des considérations administratives être trié par ordre alphabétique sur le nom et prénom des utilisateurs.**

Ces données seront à enregistrer dans un fichier : lot_distribution.csv


__Structure du fichier : lot_distribution.csv__ 

    Nom;prénom;email;flacon;lot-date
    HERVE;Pierre;Herve.pierre012@outlook.be;cho-pim-vio;20200210-001
    HENRI;Alfonse;HENRI.Alfonse2019A@outlook.be;van-cho-bas; 20200210-001
    KIRSTCH;Roméo;Kirstch.R1212@gmail.com;cho-car-ros;20200210-001
    DUPONT;Mike;DMUPIK.LU951@yahoo.fr;pim-van-thy;20200210-001

## Consignes 

- Dans le module `model`, créez les classes `Utilisateur, Essence, Composant, Flacon`. A vous de les définir.
- Dans le module `algorithms`, créez et implémentez la fonction `recherche_dichotomique(collection, cle, valeur_recherchee) -> resultat`.
- Dans le module `file`, créez les fonctions de parcours des fichiers CSV en utilisant [csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader) et [csv.DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter).
  

## Pour aller plus loin
- Rédigez les tests unitaires pour l'algorithme implémenté.
- Voir les compléments BONUS ci-dessous.


## Exemple de déroulement du programme
``` 
Bonjour, Encodez les informations de l'utilisateur : 
 Nom ?  Artur
 Prenom ? Michel
 Tel ?  02992599
 E-Mail ? artur.michel@yahoo.com 
--- Sélection de 2 goûts et 1 odeur --- 
 Encodez le 1er gout  ou  LST pour voir les goût disponible ?  LST
 ... liste des goûts sont affichés...... 
 Encodez le 1er gout ou LST pour voir les goûts disponible ? chocolat
 Encodez le 2iem gout ou LST pour voir les goûts disponible ? vanille
 Encodez le 1er odeur ou LST pour voir les goûts disponible ? cumin 
 le 'cumin' n'est pas une odeur disponible !! 
 Encodez le 1er odeur ou LST pour voir les goûts disponible ? violette 
 - - - - Composition de votre flacon - - - - 
  .. Lister les choix de l'utilisateur 
  .. Lister les essences selectionnées ! uniquement les noms ! 
  Votre flacon port le nom de : cho-van-vio 
  Le lot de fabrication est :  20200428-00001
 --- - - - - - - - - - - - - - - ---
 A bientot. 		
``` 

##### *« Les personnages et les situations de ce récit étant purement fictifs, toute ressemblance avec des personnes ou des situations existantes ou ayant existé ne saurait être que fortuite »*

-----------------------------------

## BONUS :
+ Si des gouts ou des odeurs ne sont pas existants, il faut les ajouter dans un fichier pour un traitement ultérieur par nos laborantins.
+ Il faut veiller à vérifier que chacun des fichiers est trié lors de l’initialisation du programme au début de la journée.
+ Ajouter une demande pour un gout ou odeur en tant que note prédominante (le/la plus apprécié(e) par l’utilisateur), et en ajouté alors 75% de plus (nombre de gouttes) pour des essences sélectionnées. 75% de la somme des gouttes totales  composant les essences composant le flacon (avant la note prédominante).
+ Parfois, les laborantins ne remettent pas les flacons aux bons endroits dans l’armoire-OFLA ! 
l'idée a été de mettre sur le capuchon du flacon une étiquette QR-Code et de placer une caméra au centre de la pince du robot.
Lors de la saisie, un programme permet de vérifier la code de l’essence sélectionnée 
Vous devriez ajouter un code QR, pour cela ajouter un fichier EssenceQRCode.CSV.

__Structure du fichier : EssenceQRcode.csv__ 
 ``` 
  Essence ; Nom du Fichier QR-Code ; 
  ESS-BA ;  code aléatoire composé de lettre et de chiffre avec comme base le nom de l'essence.
 Le Fichier sera une image au format QR-CODE (une fichier binaire) 
  Indications pour l'implémentation de la valeur d’un code QR en Python ! 
  ``` 
  [Gestion des codes QR par Python](https://pypi.org/project/PyQRCode/)   
 [Enregistrer un fichier au format SVG ou PNG](https://pythonhosted.org/PyQRCode/rendering.html) 
 

