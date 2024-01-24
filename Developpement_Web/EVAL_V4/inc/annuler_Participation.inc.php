<?php
// Annuler Participation \\
if (isset($_POST['annulerPart'])) {
    annulerParticipation($_POST, $message);

    calculerMontantActuel($_POST['id_projet'], $message);
    updateTauxPart($_POST['id_projet'], $message);

    $projet = $projetRepository->getProjectById(intval($_POST['id_projet']), $message);

    $porteur_projet = $projet->id_membre;
    $membre = $membreRepository->getMembreById($porteur_projet, $message);
    $mail_porteur_projet = $membre->courriel;


    envoi_mail("team.collector@gmail.com", $mail_porteur_projet, "Participation",
        "Un utilisateur a annulé sa participation à votre projet.", $message);

    echo $message;

}
?>