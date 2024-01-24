# Programmation Orientée Objet : les fichiers

Durée prévue : 4 heures prévues

## Objectif visé

À la fin du laboratoire, les étudiants seront capables de manipuler 
séquentiellement des fichiers textes, tant en lecture qu'en écriture.

## Mise en place

- Depuis PyCharm, créez un nouveau projet nommé `labo05`. Assurez-vous que celui-ci dispose de son propre environnement virtuel.
- Dans son environnement virtuel, installez les packages `radon` et `coverage`.

## Buts

Le laboratoire vise à produire deux programmes indépendants :

- un programme implémentant quelques algorithmes de décryptage stéganographiques ;
- un programme de compression et de décompression.

## Éléments de Stéganographie

**Durée estimée** : 1h30 + 30 minutes de correction

NOTE
____
Les informations données dans les exercices s'inspirent largement [d'un document](http://pignon.camille.free.fr/save/techniques_stegano.pdf) rédigé par Camille Pignon.

La stéganographie désigne un ensemble de techniques visant à cacher un message
sur un support (un texte, une image, un son, etc.). Contrairement à la cryptographie,
le contenu du message n'est pas transformé. Il est caché en clair dans le support.

Le laboratoire comporte 4 exercices débouchant sur la réalisation d'un programme 
de décryptage stéganographique de textes. Du temps est laissé pour la mise en commun 
ou la présentation de certaines solutions.

- [Exercice 01](./ex01/README.md)
- [Exercice 02](./ex02/README.md)
- [Exercice 03](./ex03/README.md)
- [Exercice 04](./ex04/README.md)

Après 1h30, le responsable présente les corrections et en profite pour répondre aux questions.

## Compression et décompression LZW

**Durée estimée** : 1h40 + 20 minutes de correction

La compression de données sans perte consiste à transformer un message
pour diminuer sa taille sans perdre d'informations.

L'algorithme présenté compte 3 exercices débouchant sur la réalisation
d'un programme de compression/décompression d'un texte.

- [Exercice 05](./ex05/README.md)
- [Exercice 06](./ex06/README.md)
- [Exercice 07](./ex07/README.md)

Après 1h20, le responsable présente les corrections et en profite pour répondre aux questions.

## Pour les plus rapides

Vous pouvez construire un programme qui construit une
chaîne de traitement.

- Compression d'un texte stéganographié ;
- Décompression d'un texte compressé et décryptage du message.

