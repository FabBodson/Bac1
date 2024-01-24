<?php
$titreOnglet = "Ajouter une catégorie"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Ajouter une catégorie"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Ajouter une catégorie";

require 'php/session.inc.php';
include('inc/header.inc.php');


if (isset($_POST['Valider'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        $resultat_champs_inexistant = isValid_categorie($_POST, $message);
        $resultat_champs_vides = verif_champs_vide($_POST, $message);

        if ($resultat_champs_inexistant && $resultat_champs_vides) {
            ajouterCategorie($_POST, $message);
        }
        echo $message;
    }
} ?>

<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

    <fieldset>
        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <label for="ajoutCategorie">Nom de la catégorie</label><input id="ajoutCategorie" name="ajoutCategorie"
                                                                      type="text" required>
        <input class="envoi" type="submit" name="Valider" value="Ajouter">

    </fieldset>

</form>


<?php

include('inc/footer.inc.php');
?>
