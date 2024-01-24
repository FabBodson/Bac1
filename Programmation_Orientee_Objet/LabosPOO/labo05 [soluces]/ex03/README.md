# Exercice 3 : remaniements

**Durée estimée** : 20 minutes

**Objectifs visés** : 

- Supprimer les répétitions de code grâce à l'héritage de classe.
- Exploiter les redéfinitions de méthodes héritées.

Les classes `AcrosticStrategy` et `LettersStrategy` ont du code commun et font
la même chose : ce sont des stratégies de décryptage stéganographiques. 
Nous souhaitons proposer un cadre pour que les programmeur puissent ajouter de nouveaux algorithmes
sténographiques.

Définissez une classe `steganography.SteganographicDecryptionStrategy` dont héritent
les classes `AcrosticStrategy` et `LettersStrategy`. Cette classe propose trois méthodes :

- `decrypt(self, source, destination)` qui lit les lignes du fichier et les décompose en mots. Cette
méthode reprend le code commun aux classes réalisées pendant les exercices 1 et 2. `decrypt` fera
appel aux méthodes suivantes pour signaler quelques événements.
- `start(self, destination)` signale le début du décryptage et permet aux classe filles d'initialiser des
attributs de travail et d'écrire dans le fichier de destination.
- `end(self, destination)` signale la fin du décryptage et permet aux classes filles d'écrire 
dans le fichier de destination
- `new_words(self, destination, words)` signale qu'une nouvelle ligne a été lue et décomposée en mots.
Les classes filles utilisent ces mots pour décrypter le message contenu et l'écrire dans `destination`.

Remaniez ensuite les classes `AcrosticStrategy` et `LettersStrategy` pour redéfinir les méthodes 
adéquates. Évitez autant que possible les répétitions de code.

Vérifiez que vos tests continuent de réussir.