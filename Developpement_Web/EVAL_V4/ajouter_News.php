<?php
$titreOnglet = "Ajouter une news"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Ajouter une news"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; <a href=\"mes_Projets.php\">Mes projets</a> &gt; 
                                                   <a href=\"detail_Projet.php\">Detail du projet</a> &gt; Ajouter une news";

require 'php/session.inc.php';
include('inc/header.inc.php');


if (isset($_POST['Valider'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        $resultat_champs_inexistant = isValid_news($_POST, $message);
        $resultat_champs_vides = verif_champs_vide($_POST, $message);

        if ($resultat_champs_inexistant && $resultat_champs_vides) {
            ajouterNews($_POST, $message);
        }
        echo $message;
    }
} ?>

<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

    <fieldset>
        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <label for="sujet">Intitulé de la news</label><input id="sujet" name="sujet" type="text" required>
        <textarea name="message" placeholder="Rédigez votre news…" required></textarea>
        <input type="hidden" name="id_projet" value="<?php echo $_GET['id_projet']; ?>">
        <input class="envoi" type="submit" name="Valider" value="Envoyer">

    </fieldset>

</form>

<?php

include('inc/footer.inc.php');
?>
