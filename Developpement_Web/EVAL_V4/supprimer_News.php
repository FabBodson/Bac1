<?php
$titreOnglet = "Supprimer news"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = ""; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Détail projet &gt; Supprimer news";

require 'php/session.inc.php';
include('inc/header.inc.php');

if (isset($_POST['confirmer'])) {
    // Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        if (supprimerNews($_POST['id_news'], $message))
            echo $message;
    }
}
?>

    <form class="confirmerSuppression" style="text-align: center;"
          action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
        <fieldset>
            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <p>Etes-vous sûr de vouloir supprimer la news ?</p>
            <input type="hidden" name="id_news" value="<?php echo $_GET['id_news']; ?>">
            <input class="boutonModifProfil" type="submit" name="confirmer" value="Confirmer">
            <input class="boutonModifProfil" type="submit" name="annuler" value="Annuler">
        </fieldset>
    </form>


<?php
include('inc/footer.inc.php');
?>