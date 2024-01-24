# Exercice 6 : décompression

**Durée estimée : ** 40 minutes

**Objectifs visés**

- choisir le bon mode d'ouverture
- utiliser la méthode `read(n)`

L'algorithme de décompression reconstruit la table de traduction à partir du fichier compressé.
Il reproduit les opérations de l'algorithme de compression de façon symétrique. 
À cette fin, la table est initialisée avec les mêmes valeurs de départ que l'algorithme de compression.

LZW commence par lire le premier code et écrit le texte correspondant en sortie. Il conserve le caractère correspondant.

Code lu : **19**

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

Écrit en sortie : T

Mémorisé : T

L'algorithme lit le code suivant. Si ce dernier est dans la table (cas le plus courant), l'algorithme écrit la valeur correspondante en sortie 
**et** ajoute à la table une entrée formée du mot mémorisé et du premier caractère du morceau correspondant. 
Si le code n'appartient pas à la table (cas peu fréquent), l'algorithme écrit en sortie la concaténation du  mot mémorisé et de son premier symbole 
et l'ajoute à la table. L'algorithme mémorise l'entrée en vue de la répétition suivante.

Code lu : **14**

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

Écrit en sortie : O

Mémorisé : O

Code après code, l'algorithme reconstruit le texte de départ.

```c
décompresser(Entrée, Sortie)
    char code = Lire(Entrée);
    Ecrire(table[code]);
    memorise = table[code];

    while(il reste des codes en entrée){
        code = Lire(Entrée);
        string valeur = if(table contient code) table[code] else memorise+memorise[0];
        Ecrire(valeur)
        table[] = memorise+valeur[0];
        memorise = valeur;
    }
}
```


## Votre code

Ajoutez à la classe `Lzw` une méthode `decompress(self, source, destination)`. `decompress` lit le fichier binaire source
symbole par symbole et écrit les valeurs correspondantes dans la table de traduction dans le fichier texte de destination. 
Utilisez à cette fin la méthode `read(n)`.

Testez votre méthode.