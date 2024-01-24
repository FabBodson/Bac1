<?php
$titreReferencement = "Accueil anonyme Collect'Or";
$titreOnglet = "Accueil Collect'Or"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "";
$filAriane = "";
$messagePrincipal = "Bienvenue sur Collect'Or, la plateforme de crowdfunding où vous pouvez participer à ou créer des projets !";
$messageSection = "Quelques projets en cours …";

require 'php/session.inc.php';

$message = "";


if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre') {
    include('inc/header.inc.php');
}else
    include('inc/header_Anonyme.inc.php');


use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrMembre\MembreRepository as MembreRepository;

$projetRepository = new ProjetRepository();
$membreRepository = new MembreRepository();

//récupérer la liste de projets
$listeProjets = $projetRepository->getAllProjects($message);


include('inc/annuler_Participation.inc.php');

include('inc/main_Accueil.inc.php');

include('inc/footer.inc.php');
?>
