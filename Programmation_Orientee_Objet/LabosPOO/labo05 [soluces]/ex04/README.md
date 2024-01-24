# Exercice 4 : un programme de décryptage stéganographique

**Durée estimée** : 30 minutes

**Objectifs visés** :

- Changer le répertoire de travail courant (_CWD_)
- Choisir le bon mode d'ouverture
- Gérer les exceptions

Créez un programme qui :

1. demande à l'utilisateur d'encoder le chemin du CWD ;
2. tente de changer de le CWD. En cas d'erreur, le programme affiche un message d'erreur adéquat et termine son exécution.
3. crée un fichier `output.txt` qui contiendra les contenus decrypter ;
4. liste les fichiers du CWD et pour chaque fichier d'extension 'txt' autre que `output.txt` :
    1. Demande la stratégie à appliquer ([a]crostiche ou [l]ettres)
    2. Décrypte le contenu du fichier et l'ajoute au fichier `output.txt`
    
Pour lister les fichiers du CWD, utilisez la fonction `listdir` du module `os`.