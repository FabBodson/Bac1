<?php
$titreOnglet = "Mes participations"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Mes participations"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Mes participations";

require 'php/session.inc.php';
include('inc/header.inc.php');

use CollectOrParticipation\ParticipationRepository as ParticipationRepository;
use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrMembre\MembreRepository as MembreRepository;


$message = "";
$projetRepository = new ProjetRepository();
$membreRepository = new MembreRepository();
$participationRepository = new ParticipationRepository();

//récupérer la liste de projets
$listeParticipations = $participationRepository->getAllLastParticipations($message);

include('inc/annuler_Participation.inc.php');

    ?>


    <section class="messagesParticipations">
        <p class="messagePrincipal">Vous contribuez au futur !</p>

        <p>Nombre de participations : <?php echo nombreParticipations($id_membre_session, $message); ?></p>
        <p>Montant total promis : <?php echo montantTotalPromis($id_membre_session, $message); ?> €</p>
        <p>Montant total prélevé : <?php echo montantTotalPreleve($id_membre_session, $message); ?> €</p>

    </section>

    <section>
        <h2>Mes participations</h2>


        <?php
        foreach ($listeParticipations as $participation) {
            if ($participation->id_membre == $id_membre_session) {
                $projet = $projetRepository->getProjectById($participation->id_projet, $message);
                include ('inc/apercu_Projet.inc.php');
                 }
        } ?>


    </section>
    <?php

include('inc/footer.inc.php');
?>
