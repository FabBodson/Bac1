<?php
$titreOnglet = "Modifier une news"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Modifier une news"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; <a href=\"mes_Projets.php\">Mes projets</a> &gt; 
                                                   <a href=\"detail_Projet.php\">Detail du projet</a> &gt; Modifier news";

require 'php/session.inc.php';
include('inc/header.inc.php');


if (isset($_POST['Valider'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        modifierNews($_POST, $message);
        echo $message;
    }
} ?>

<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

    <fieldset>
        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <label for="sujet">Intitulé de la news</label><input id="sujet" name="sujet" type="text">
        <textarea name="message" placeholder="Rédigez votre news…"></textarea>

        <input type="hidden" name="id_news" value="<?php echo $_GET['id_news']; ?>">
        <input class="envoi" type="submit" name="Valider" value="Envoyer">

    </fieldset>

</form>

<?php

include('inc/footer.inc.php');
?>
