# Exercice 2 : variante de l'acrostiche

**Durée estimée** : 20 minutes

**Objectifs visés** : 

- Utiliser les méthodes `readline`, `write` et `readline`.
- Analyser le contenu d'un fichier.
- Choisir les modes d'ouvertures.
- Utiliser la structure `with`

De nombreuses variantes de l'acrostiche existe. Dans la variante suivante,
il faut prendre la deuxième lettre de chaque mot pour reconstituer le message.

Par exemple, le message :
    "Apparently neutral’s protest is thoroughly discounted and ignored. 
    Isman hard him. Blockade issue affects pretext for embargo on byproducts,
    ejecting suets and vegetableoils."

Donne le texte déchiffré :
    "pershingsailsfromnyjunei"
    
Avec le contexte, le texte déchiffré s'interprète comme ci-dessous :
    "Pershing sails from NY June 1".

Ajoutez une classe `LetterStrategy` au module `steganography`. Cette
classe expose une méthode `decrypt(self, input, output)` qui écrit dans
le fichier `output` le texte déchiffré depuis `input`.