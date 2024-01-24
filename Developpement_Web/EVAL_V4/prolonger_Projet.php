<?php
$titreOnglet = "Prolonger mon projet"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Prolonger mon projet"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; <a href=\"gerer_Profil.php\">Profil</a> &gt; 
<a href=\"mes_Projets.php\">Mes projets</a> &gt; Prolonger mon projet";

require 'php/session.inc.php';
include('inc/header.inc.php');

$erreur = "";
$nom_fichier = "";

$message = '';
$noError = True;

use CollectOrProjet\ProjetRepository as ProjetRepository;


if (isset($_POST['Valider']) && empty($_POST['nvDateEcheance'])) {
    echo "<p style=\"color: red;\">Vous devez sélectionner une date.</p>";
}


if (isset($_POST['Valider'])) {
    // Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        prolongerProjet($_POST, $message);
        echo $message;
    }
} else {

    $projetRepository = new ProjetRepository();

    $projet = $projetRepository->getProjectById(intval($_GET['id_projet']), $message);


    ?>


    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

        <fieldset>

            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <p>Echéance actuelle: <br>
                <?php echo date('d-m-Y', strtotime($projet->date_echeance)); ?>
            </p>
            <label for="nvDateEcheance">Nouvelle échéance*</label><input id="nvDateEcheance" name="nvDateEcheance"
                                                                         type="date"
                                                                         value="<?php echo isset($_POST['nvDateEcheance']) ? htmlentities($_POST['nvDateEcheance']) : ""; ?>"
                                                                         required>


            <input type="hidden" name="id_projet" value="<?php echo $_GET['id_projet']; ?>">
            <input class="envoi" type="submit" name="Valider" value="Prolonger projet">
            <input class="effacer" type="reset" name="reset" value="Annuler">

        </fieldset>


    </form>


    <?php
}
include('inc/footer.inc.php');
?>
