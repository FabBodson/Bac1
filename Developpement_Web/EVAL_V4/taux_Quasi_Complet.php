<?php
$titreOnglet = "Taux";   /* Onglet */
$titreSite = "Collect'Or";  /* h2 */
$titrePage = "Forte participation";     /* h1 */
$messagePrincipal = "";     /* Message principal */
$messageSection = "Ils sont presque finis !";   /* Message en haut de section */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Filtres &gt; Taux élevés";

require 'php/session.inc.php';

if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre')
    include('inc/header.inc.php');
else
    include('inc/header_Anonyme.inc.php');



use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrMembre\MembreRepository as MembreRepository;


$message = "";
$projetRepository = new ProjetRepository();
$membreRepository = new MembreRepository();


//récupérer la liste de projets
$listeProjets = $projetRepository->getAllAlmostFinishedProjects($message);

include('inc/annuler_Participation.inc.php');


include ('inc/main_Accueil.inc.php');


include ('inc/footer.inc.php');
?>



