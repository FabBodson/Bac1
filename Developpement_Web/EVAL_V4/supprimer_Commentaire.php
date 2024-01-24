<?php
$titreOnglet = "Supprimer commentaire"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = ""; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Détail projet &gt; Supprimer commentaire";

require 'php/session.inc.php';
include('inc/header.inc.php');

if (isset($_POST['confirmer'])) {
    // Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        if (supprimerCommentaire($_POST['id_comment'], $message))
            echo $message;
    }
}

?>

    <form class="confirmerSuppression" style="text-align: center;"
          action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
        <fieldset>
            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <p>Etes-vous sûr de vouloir supprimer le commentaire ?</p>
            <input type="hidden" name="id_comment" value="<?php echo $_GET['id_comment']; ?>">
            <input class="boutonModifProfil" type="submit" name="confirmer" value="Confirmer">
            <input class="boutonModifProfil" type="submit" name="annuler" value="Annuler">
        </fieldset>
    </form>


<?php
include('inc/footer.inc.php');
?>