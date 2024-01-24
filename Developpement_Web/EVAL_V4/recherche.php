<?php
$titreReferencement = "";
$titreOnglet = "Collect'Or"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "";
$filAriane = "";
$messagePrincipal = "";
$messageSection = "Le fruit de nos recherches …";

require 'php/session.inc.php';

$message = "";

if (isset($_POST['rechercher'])) {
    setcookie('rechercher', htmlentities($_POST['rechercher']), time()+(3600*24*30), '/~190230/');
    $recherche = htmlentities($_POST['rechercher']);
} else {
    if (!isset($_COOKIE['rechercher'])) {
        setcookie('rechercher', 'timestamp', time()+(3600*24*30), '/~~90230/');
        $recherche = 'timestamp';
    } else {
        $recherche = $_COOKIE['rechercher'];
    }
}


if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre') {
    include('inc/header.inc.php');
} else
    include('inc/header_Anonyme.inc.php');



use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrMembre\MembreRepository as MembreRepository;

$projetRepository = new ProjetRepository();
$membreRepository = new MembreRepository();

?>
<section>
    <form class="formRecherche" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <input class="barreRecherche" type="text" name="recherche" placeholder="Recherche">
        <input class="boutonRecherche" type="submit" name="rechercher" value="Rechercher">
    </form>
</section>

<?php

if (isset($_POST['rechercher'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";

        $listeProjets = $projetRepository->getResearch($_POST['recherche'], $message);

        include('inc/annuler_Participation.inc.php');

        include('inc/main_Accueil.inc.php');

    }
}
include('inc/footer.inc.php');
?>
