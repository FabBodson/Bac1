<?php
$titreOnglet = "Modifier mon projet"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Modifier mon projet"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; <a href=\"gerer_Profil.php\">Profil</a> &gt; 
<a href=\"mes_Projets.php\">Mes projets</a> &gt;
<a href=\"modifier_Projet.php\">Modifier projet</a> &gt; Modifier mon projet";

require 'php/session.inc.php';
include('inc/header.inc.php');

$erreur = "";
$nom_fichier = "";

$message = '';
$noError = True;

if (isset($_POST['Valider']) && empty($_POST['description']) && empty($_FILES['avatar']['name'])) {
    var_dump($_POST);
    echo '<br>';
    var_dump($_FILES);
    echo "<p style=\"color: red;\">Vous devez modifier au moins un champs.</p>";
}


if (isset($_POST['Valider'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        modifierProjet($_POST, $nom_fichier, $message);
        echo $message;
    }
} ?>


<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST" enctype="multipart/form-data">

    <fieldset>

        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <input type="hidden" name="MAX_FILE_SIZE" value="3072000">
        <label for="photo">Photo de projet</label><input id="photo" type="file" name="avatar"
                                                         accept="image/*, .jpg, .png">

        <label for="description">Description du projet</label><textarea id="description" name="description"
                                                                        placeholder="Décrivez le ici"></textarea>

        <input type="hidden" name="id_projet" value="<?php echo $_GET['id_projet']; ?>">
        <input class="envoi" type="submit" name="Valider" value="Modifier projet">
        <input class="effacer" type="reset" name="reset1" value="Annuler">

    </fieldset>


</form>


<?php

include('inc/footer.inc.php');
?>
