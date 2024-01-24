<article>
    <a class="details"
       href="detail_Projet.php?id_projet=<?php echo $projet->id_projet; ?>">
        <img src="upload/<?php echo $projet->illustration_apercu; ?>" alt="Erreur chargement image">

    <header>
        <h3><?php echo $projet->intitule; ?></h3>
    </header>
    </a>
    <p class="descriptionApercu"><?php echo $projet->description; ?></p>

    <ul>
        <li><?php echo ucfirst($projetRepository->getCategorieProjet($projet->id_categorie, $message)); ?></li>
        <li>Montant demandé: <?php echo $projet->montant; ?> €</li>
        <li>Échéance: <?php echo date('d-m-Y', strtotime($projet->date_echeance)); ?></li>
        <li><?php echo ucfirst($projetRepository->getLibelleTypePartById($projet->id_projet, $message)); ?></li>
        <li><?php echo $projet->taux_participation; ?> % atteint</li>
    </ul>
    <footer class="footerArticle">

        <p>Créé le <?php echo date('d-m-Y', strtotime($projet->date_creation)); ?></p>
        <?php
        if ($id_membre_session == $projet->id_membre && $projet->est_valide == 0) { ?>
            <a class="details" href="modifier_Projet.php?id_projet=<?php echo $projet->id_projet; ?>">Modifier</a>
            <?php if (strtotime($projet->date_echeance) <= strtotime(date('Y-m-d'))
                && $projet->montant_actuel < $projet->montant) {
                ?>
                <a class="details" href="prolonger_Projet.php?id_projet=<?php echo $projet->id_projet; ?>">Prolonger</a>

            <?php }
            if ($projet->montant_actuel < $projet->montant) { ?>
                <a class="details" href="supprimer_Projet.php?id_projet=<?php echo $projet->id_projet; ?>">Supprimer</a>

            <?php }
        }
        if (($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre')
            && aParticipe($id_membre_session, $projet->id_projet, $message)
            && strtotime(date('Y-m-d')) < strtotime($projet->date_echeance)
            && $projet->montant_actuel < $projet->montant) { ?>

            <form class="formAnnulerPart" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
                <input type="hidden" name="id_projet" value="<?php echo $projet->id_projet; ?>">
                <input type="hidden" name="id_membre" value="<?php echo $id_membre_session; ?>">
                <input class="supprimerNews" type="submit" name="annulerPart" value="Annuler participation">
            </form>

        <?php }
        ?>

    </footer>
</article>