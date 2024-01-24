<?php
$titreOnglet = "Visualier un projet"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = ""; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Détail d'un projet";


require 'php/session.inc.php';

if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre')
    include('inc/header.inc.php');
else
    include('inc/header_Anonyme.inc.php');

use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrCommentaire\CommentaireRepository as CommentaireRepository;
use CollectOrNews\NewsRepository as NewsRepository;
use CollectOrMembre\MembreRepository as MembreRepository;


// Poster Commentaire \\
if (isset($_POST['EnvoyerCommentaire'])) {
    $resultat_champs_vide = verif_champs_vide($_POST, $message);

    if ($resultat_champs_vide) {
        ajouterCommentaire($_POST, $message);
        echo $message;
    }
} else {

// Supprimer Commentaire \\
    if (isset($_POST['supprimerCommentaire'])) {
        include ('supprimer_Commentaire.php');
    }

// Supprimer News \\
    if (isset($_POST['supprimerNews'])) {
        include ('supprimer_News.php');
    }


    $erreur = "";
    $nom_fichier = "";

    $message = '';
    $noError = True;


    $projetRepository = new ProjetRepository();
    $commentaire = new CommentaireRepository();
    $news = new NewsRepository();


    $listeCommentaires = $commentaire->getAllCommentaires($message);
    $listeNews = $news->getAllNews($message);
    $libelleTypePart = $projetRepository->getLibelleTypePartById($_GET['id_projet'], $message);
    $descriptionTypePart = $projetRepository->getDescriptionTypePartById($_GET['id_projet'], $message);

    if (isset($_GET['id_projet']) && is_numeric($_GET['id_projet'])) {
        $projet = $projetRepository->getProjectById(intval($_GET['id_projet']), $message);
    }


    ?>


    <h1 class="nomProjet"><?php echo $projet->intitule; ?></h1>


    <!-- INFOS PROJET -->

    <section class="section1DetailProjet">


        <section class="infoProjetA">

            <img class="imageProjetDetail" src="upload/<?php echo $projet->illustration_apercu; ?>"
                 alt="Erreur chargement image">


            <h2 class="presentationProjet">Description du projet</h2>

            <p><?php echo $projet->description; ?></p>


            <h2 class="presentationProjet"><?php echo ucfirst($libelleTypePart); ?></h2>

            <p><?php echo ucfirst($descriptionTypePart); ?></p>


        </section>

        <!-- INFOS PRATIQUES -->

        <section class="infoProjetB">

            <p class="descriptionProjet"><?php echo $projet->montant_actuel; ?> €
                récoltés<br>sur <?php echo $projet->montant; ?> €</p>

            <p class="descriptionProjet">Echéance:<br><?php echo date('d-m-Y', strtotime($projet->date_echeance)); ?>
            </p>


            <p class="descriptionProjet"><?php echo $projet->taux_participation; ?>% atteint</p>

        <?php if ($projet->montant_actuel < $projet->montant && (strtotime(date('Y-m-d')) < strtotime($projet->date_echeance))) {
                if (!aParticipe($id_membre_session, $projet->id_projet, $message)) {
                    ?>
                    <a class="lienParticiperProjet"
                       href="participation_Projet.php?id_projet=<?php echo $projet->id_projet; ?>">Je veux participer !</a>

                    <?php
                }
            } ?>

            <p>Créé par:<br><?php echo $projetRepository->getCreateurProjet($projet->id_membre, $message); ?></p>

        </section>


    </section>

    <!-- NEWS -->

    <section class="section2DetailProjet">
        <h2>News</h2>
        <?php foreach ($listeNews as $news_id) {
            if ($news_id->id_projet == intval($_GET['id_projet'])) {
                ?>
                <article class="newsDetailProjet">
                    <header>
                        <h3><?php echo $news_id->intitule; ?></h3>
                    </header>

                    <p>
                        <?php echo $news_id->description; ?>
                    </p>

                    <footer class="footerNews">
                        <p><?php echo date('d-m-Y', strtotime($news_id->date_publication)); ?></p>
                        <?php if (($statut == 'admin' || $statut == 'porteurProjet') && $id_membre_session == $projet->id_membre) { ?>
                            <a class="modiferNews"
                               href="modifier_News.php?id_news=<?php echo $news_id->id_news; ?>">Modifier</a>
                            <a class="modiferNews"
                               href="supprimer_News.php?id_news=<?php echo $news_id->id_news; ?>">Supprimer</a>

                        <?php } ?>
                    </footer>


                </article>

            <?php }

        } ?>


        <?php if (($statut == 'admin' || $statut == 'porteurProjet') && $id_membre_session == $projet->id_membre) { ?>
            <a class="ajoutNews"
               href="ajouter_News.php?id_projet=<?php echo $_GET['id_projet']; ?>">Ajouter une news</a>
        <?php } ?>

    </section>

    <!-- COMMENTAIRES -->

    <section class="section3DetailProjet">
        <h2>Commentaires</h2>

        <?php foreach ($listeCommentaires as $commentaire_id) {

            if ($commentaire_id->id_projet == intval($_GET['id_projet'])) {
                $membreRepository = new MembreRepository();
                $membre = $membreRepository->getMembreById($commentaire_id->id_membre, $message);
                ?>

                <article class="commentaireDetailProjet">
                    <header>
                        <h3><?php echo $membre->login; ?></h3>
                    </header>


                    <p><?php echo $commentaire_id->commentaire; ?></p>

                    <footer class="footerCommentaire">

                        <p> <?php echo date('d-m-Y', strtotime($commentaire_id->date_mise_en_ligne)); ?> </p>

                        <?php if ($id_membre_session == $commentaire_id->id_membre) {
                            ?>
                            <a class="modiferComm"
                               href="supprimer_Commentaire.php?id_comment=<?php echo $commentaire_id->id_comment; ?>">Supprimer</a>

                            <a class="modiferComm"
                               href="modifier_Commentaire.php?id_projet=<?php echo $commentaire_id->id_projet; ?>&&id_comment=<?php echo $commentaire_id->id_comment; ?>">Modifier</a>

                        <?php } ?>
                    </footer>

                </article>

            <?php } ?>
        <?php } ?>


        <?php if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre') { ?>

            <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

                <fieldset>

                    <textarea name="NouveauCommentaire" placeholder="Rédigez votre commentaire…" required></textarea>
                    <input type="hidden" name="id_membre" value="<?php echo $id_membre_session; ?>">
                    <input type="hidden" name="id_projet" value="<?php echo $_GET['id_projet']; ?>">
                    <input class="envoi" type="submit" name="EnvoyerCommentaire" value="Poster">

                </fieldset>
            </form>
        <?php } ?>


    </section>


    <?php

}
include('inc/footer.inc.php');
?>
