# Exercice 5 : compression LZW

**Durée estimée** : 40 minutes

**Objectifs visés :**
- choisir le bon mode d'ouverture
- utiliser la méthode `read(n)`

LZW est un algorithme de compression simple, rapide et plutôt efficace pour compresser les données. Les formats de fichiers pdf, tiff et gif l'utilisent.

LZW construit une table de traduction où les clés sont codées sur N bits et où les valeurs sont des chaînes de caractères. Au fur et à mesure qu'il parcourt le texte à compresser, LZW ajoute des entrées à la table. Ces entrées font référence à des morceaux de texte de plus en plus longs.

Pour ce laboratoire, nous partons d'une table où les clés sont codées sur 8 bits : la table admet jusqu'à 256 entrées. Nous limiterons le problème de compression/décompression aux lettres et à quelques caractères d'espacement (l'espace, la tabulation `\t`, le saut de ligne `\n` et le retour de chariot `\r`).

## Algorithme de compression

Avant de débuter l'algorithme de compression, la table de traduction est initialisée avec les 26 lettres et les caractères d'espacement. 

|Valeur|Clé|
|---|---|
|  A|  0|
|  B|  1|
|...|...|
|  Z| 25|
|' '| 26|
| \t| 27|
| \r| 28|
| \n| 29|

Lorsqu'il lit les premiers symboles du texte, LZW ajoute de nouvelles valeurs à la table. Ces valeur sont constituées du code du plus long morceau trouvé dans la table suivi du symbole lu. En plus d'enregistrer la nouvelle entrée, LZW écrit le code correspondant au plus long morceau en sortie.

Prenons par exemple le texte "TO BE OR NOT TO BE". "T" est un morceau présent dans la table, l'algorithme ne modifie rien et lit le symbole suivant. "TO" ne fait pas partie de la table, l'algorithme l'ajoute et écrit le code du morceau existant le plus long en sortie, en l'occurrence "T".

|Valeur|Clé|
|---|---|
|  A|  0|
|  B|  1|
|...|...|
|  Z| 25|
|' '| 26|
| \t| 27|
| \r| 28|
| \n| 29|
| *TO*| *30*|

Écrit en sortie : `19`.

L'algorithme retient le dernier symbole du morceau ajouté et lui concatène le symbole suivant à lire, ce qui donne "O ". Cette valeur n'existe pas : l'algorithme l'ajoute et écrit en sortie le code de la plus longue correspondance existante, "O".

|Valeur|Clé|
|---|---|
|  A|  0|
|  B|  1|
|...|...|
|  Z| 25|
|' '| 26|
| \t| 27|
| \r| 28|
| \n| 29|
| TO| 30|
| *O_*| *31*|

Écrit en sortie : 19 `14`

LZW poursuit son analyse jusque la fin du fichier. À la fin de l'analyse, LZW a écrit en sortie :
19 14 26 1 4 26 14 17 26 13 14 19 26 *30 32* 4. Le texte compressé comporte 16 octets : nous avons gagné 2 octets par rapport au texte à compresser :). Remarquez les valeurs 30 et 32 qui correspondent à des entrées ajoutées pendant l'analyse.

NOTE
----
Les valeurs écrites en sortie sont des octets. Par exemple, `19` sera écrit `00010011`. Le fichier compressé est dès lors illisible quand vous l'ouvrez dans un éditeur de texte.

*Pseudo-code de l'algorithme de compression
```c
compresser(Entrée, Sortie) {
	string mot = "";

	while(il reste des caractères à lire dans Entrée) {
	   char c = Lire(Entrée);
	   string cle = mot + c;
	   if(tableau contient cle)
		  mot = cle;
	   else {
		  tableau[] = cle;
		  Ecrire(Sortie, tableau[mot]);
		  mot = c;
	   }
	}
	
	Ecrire(Sortie, tableau[mot]);
}
```

## Votre code

Définissez un module `compressions` à la racine de votre projet. Définissez une classe `Lzw` qui comporte une méthode `compress(self, source, destination)`. `compress` lit le fichier source  symbole par symbole et écrit les clés correspondantes dans la table de traduction dans le fichier binaire de destination. Utilisez à cette fin la méthode `read(n)`.

Testez votre méthode.
