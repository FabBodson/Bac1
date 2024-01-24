<?php
$titreOnglet = "Participer à un projet"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Participer à un projet"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; <a href=\"detail_Projet.php\">Détail projet</a> &gt; Participer";

require 'php/session.inc.php';

if (empty($_SESSION))
    header("location: connexion.php");

include('inc/header.inc.php');

use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrMembre\MembreRepository as MembreRepository;

$erreur = "";
$nom_fichier = "";

$message = '';
$noError = True;

$projetRepository = new ProjetRepository();
$membreRepository = new MembreRepository();


if (isset($_POST['Valider'])) {
    // Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        $valeurs_numeriques = array('sommeVersement');

        $resultat_champs_numeriques = verif_champs_numerique($_POST, $valeurs_numeriques, $message);

        $projet = $projetRepository->getProjectById(intval($_POST['id_projet']), $message);
        $porteur_projet = $projet->id_membre;
        $montant_minimum = $projet->montant_minimum;

        $membre = $membreRepository->getMembreById($porteur_projet, $message);

        $mail_porteur_projet = $membre->courriel;


        if ($resultat_champs_numeriques && $montant_minimum <= intval($_POST['sommeVersement'])) {
            if (isValid_participation($_POST, $message)) {
                participer($_POST, $message);
                envoi_mail("team.collector@gmail.com", $mail_porteur_projet, "Participation",
                    "Un utilisateur vient de participer à votre projet !", $message);
                calculerMontantActuel($projet->id_projet, $message);
                updateTauxPart($_POST['id_projet'], $message);

            }
        }

    }
} else {

    $projet = $projetRepository->getProjectById(intval($_GET['id_projet']), $message);

    $montant_minimum = $projet->montant_minimum;
    ?>

    <p class="messagePrincipal">Participez au futur !</p>


    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

        <fieldset>
            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <label for="sommeVersement">Somme du versement</label><input id="sommeVersement" type="number"
                                                                         name="sommeVersement" step="0.1"
                                                                         min="<?php echo $montant_minimum; ?>"
                                                                         required>

            <input type="hidden" name="id_projet" value="<?php echo $_GET['id_projet']; ?>">
            <input type="hidden" name="id_membre" value="<?php echo $id_membre_session; ?>">
            <input class="envoi" type="submit" name="Valider" value="Verser l'argent">


        </fieldset>


    </form>

    <?php
}
include('inc/footer.inc.php');
?>
