# Exercice 1 : les acrostiches

**Durée estimée** : 20 minutes

**Objectifs visés** : 

- Utiliser les méthodes `readline`, `write` et `readline`.
- Analyser le contenu d'un fichier.
- Choisir les modes d'ouvertures.
- Utiliser la structure `with`

La forme la plus simple d'algorithme stéganographique consiste à placer
les mots du message à cacher comme premier mot d'une ligne : c'est l'acrostiche.

L'exemple classique est cette lettre envoyée par Alfred de Musset à Georges Sand 
(la véridicité des faits reste à prouver, car personne n'a retrouvé ces textes dans leur correspondance).

    "**Quand** je mets à vos pieds un éternel hommage
     **Voulez**-vous qu'un instant je change de visage?
     **Vous** avez capturé les sentiments d'un cour
     **Que** pour vous adorer forma le Créateur.
     **Je** vous chéris, amour, et ma plume en délire
     **Couche** sur le papier ce que je n'ose dire.
     **Avec** soin, de mes vers lisez les premiers mots
     **Vous** saurez quel remède apporter à mes maux"
    
Voici la réponse de Georges Sand :

    "**Cette** insigne faveur que votre cour réclame
     **Nuit** à ma renommée et répugne mon âme."

Créez un module `steganography` à la racine du projet. Définissez une classe `steganography.AcrosticStrategy`. 
Définissez-y une méthode `decrypt(self, source, dest)` où `source` désigne un fichier source ouvert en lecture 
et `dest` un fichier où le texte décrypté sera écrit. Partez du principe que le fichier à lire peut être volumineux : 
lire son contenu d'une traite n'est pas une bonne idée.

Validez votre code dans une classe `ex01.test_acrostic_strategy.AcrosticStrategyTests`, vous pouvez définir plusieurs fichiers 
dans le paquetage `ex01`. N'oubliez pas que tout fichier ouvert doit être fermé.

**Point d'attention**

Une bonne suite de tests unitaires doit être rejouable sans avoir à manipuler l'environnement de test. 
Quel mode d'ouverture garantit que le contenu du fichier de destionation est effacé ?

## Pour les plus rapides

Dans son module `io`, Python propose une classe `StringIO` pour simuler des fichiers textes en mémoire.
Elle offre l'avantage d'éviter de remettre le contenu du paquetage dans un état initial
pour que les exécutions de test suivantes continuent de réussir.

Réécrivez les tests avec cette classe.

