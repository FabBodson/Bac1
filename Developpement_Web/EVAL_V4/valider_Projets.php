<!DOCTYPE html>
<?php
$titreOnglet = "Valider des projets"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Valider des projets";
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Valider des projets";


require 'php/session.inc.php';
include('inc/header.inc.php');


use CollectOrProjet\ProjetRepository as ProjetRepository;


$message = "";
$projetRepository = new ProjetRepository();

//récupérer la liste de projets
$listeProjets = $projetRepository->getAllLastProjects($message);

if(isset($_POST['validerProjet'])){
    validerProjet($_POST['id_projet'], $message);
    echo $message;
}
?>



    <section>

        <h2>Projets à valider</h2>

        <?php foreach ($listeProjets as $projet) {
            if ($projet->taux_participation >= 100 && $projet->est_valide == 0) {
                ?>

                <article>
                    <a class="details"
                       href="detail_Projet.php?id_projet=<?php echo $projet->id_projet; ?>">
                    <img src="upload/<?php echo $projet->illustration_apercu; ?>" alt="Erreur chargement image">
                    </a>
                    <header>
                        <h3><?php echo $projet->intitule; ?></h3>
                    </header>
                    <p class="descriptionApercu"><?php echo $projet->description; ?></p>

                    <ul>
                        <li><?php echo ucfirst($projetRepository->getCategorieProjet($projet->id_categorie, $message)); ?></li>
                        <li>Montant demandé: <?php echo $projet->montant; ?> €</li>
                        <li>Échéance: <?php echo $projet->date_echeance; ?></li>
                        <li><?php echo ucfirst($projetRepository->getLibelleTypePartById($projet->id_projet, $message)); ?></li>
                        <li><?php echo ($projet->taux_participation / 100); ?> % atteint</li>
                    </ul>
                    <footer class="footerArticle">
                        <p>Créé le <?php echo $projet->date_creation; ?></p>
                    <?php if ($projet->id_membre == $id_membre_session){ ?>
                        <a class="details"
                           href="modifier_Projet.php?id_projet=<?php echo $projet->id_projet; ?>">Modifier</a>
                        <?php } ?>

                        <form class="formSuppression" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
                            <input type="hidden" name="id_projet" value="<?php echo $projet->id_projet; ?>">
                            <input class="supprimerNews" type="submit" name="validerProjet" value="Valider projet">
                        </form>




                    </footer>
                </article>
            <?php }
        } ?>


    </section>

<?php

include('inc/footer.inc.php');
?>

