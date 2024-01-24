<?php
$titreOnglet = "Mes projets"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Mes projets"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Mes projets";

require 'php/session.inc.php';
include('inc/header.inc.php');


use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrMembre\MembreRepository as MembreRepository;


$message = "";
$projetRepository = new ProjetRepository();
$membreRepository = new MembreRepository();

//récupérer la liste de projets
$listeProjets = $projetRepository->getAllLastProjects($message);


include('inc/annuler_Participation.inc.php');


    ?>
    <section>

        <h2>Mes projets</h2>

        <?php foreach ($listeProjets as $projet) {
            if ($projet->id_membre == $id_membre_session) {

                include('inc/apercu_Projet.inc.php');
                 }
        } ?>


    </section>

<?php

include('inc/footer.inc.php');
?>
