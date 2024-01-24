<?php
$titreOnglet = "Supprimer projet"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = ""; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Supprimer projet";

require 'php/session.inc.php';
include('inc/header.inc.php');

use CollectOrProjet\ProjetRepository as ProjetRepository;

$message = "";

$projetRepository = new ProjetRepository();
$projet = $projetRepository->getProjectById($_GET['id_projet'], $message);


if (isset($_POST['confirmer'])) {
    if($projet->id_membre == $id_membre_session) {
        // Protection SPAM \\
        if (!empty($_POST['spam'])) {
            $message .= "Requête refusée : origine incorrecte !<br>";
            $valid = false;
        } else {
            $_POST['spam'] = " ";
            if (supprimerProjet($_POST['id_projet'], $message))
                echo $message;
        }
    }else{
        echo "Vous ne pouvez pas supprimer ce projet !";
    }
}
?>

    <form class="confirmerSuppression" style="text-align: center;"
          action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
        <fieldset>
            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <p>Etes-vous sûr de vouloir supprimer le projet ?</p>
            <input type="hidden" name="id_projet" value="<?php echo $_GET['id_projet']; ?>">
            <input class="boutonModifProfil" type="submit" name="confirmer" value="Confirmer">
            <input class="boutonModifProfil" type="submit" name="annuler" value="Annuler">
        </fieldset>
    </form>


<?php
include('inc/footer.inc.php');
?>