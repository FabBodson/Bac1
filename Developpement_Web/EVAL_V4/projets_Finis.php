<!DOCTYPE html>
<?php
$titreOnglet = "Projets financés"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Projets financés";
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Projets financés";


require 'php/session.inc.php';

$message = "";


if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre') {
    include('inc/header.inc.php');
}else
    include('inc/header_Anonyme.inc.php');


use CollectOrProjet\ProjetRepository as ProjetRepository;


$message = "";
$projetRepository = new ProjetRepository();

//récupérer la liste de projets
$listeProjets = $projetRepository->getAllLastProjects($message);

?>



<section>

    <h2>Les projets financés</h2>

    <?php foreach ($listeProjets as $projet) {
        if ($projet->taux_participation >= 100) { ?>
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
                    <li>Échéance: <?php echo date('d-m-Y', strtotime($projet->date_echeance)); ?></li>
                    <li><?php echo ucfirst($projetRepository->getLibelleTypePartById($projet->id_projet, $message)); ?></li>
                    <li><?php echo $projet->taux_participation/100; ?> % atteint</li>
                </ul>
                <footer class="footerArticle">

                    <p>Créé le <?php echo date('d-m-Y', strtotime($projet->date_creation)); ?></p>

                </footer>
            </article>
          <?php   }
    } ?>


</section>

<?php

include('inc/footer.inc.php');
?>

