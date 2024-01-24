<?php
$titreOnglet = "Imprimer mes donations"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = ""; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Imprimer mes participations";

require 'php/session.inc.php';
include('inc/header.inc.php');

use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrMembre\MembreRepository as MembreRepository;


$message = "";
$projetRepository = new ProjetRepository();
$membreRepository = new MembreRepository();

$listeProjets = $projetRepository->getAllProjects($message);
include('inc/annuler_Participation.inc.php');

?>


<section>
    <h2>Imprimer mes donations</h2>



    <?php foreach ($listeProjets as $projet) {
        if ($projet->est_valide == 1 && $projet->id_type_part == 1) {
            include ('inc/apercu_Projet.inc.php');
             }
    } ?>
</section>


<?php
include('inc/footer.inc.php');
?>
