<?php
$titreOnglet = "Profil"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Mon profil"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Votre Profil";

require 'php/session.inc.php';
include('inc/header.inc.php');

if (isset($_POST['supprimerProfil'])) {
    if (MembreCanBeSuppressed($_POST['id_membre'], $message)) {
        supprimerMembre($_POST['id_membre'], $message);

        $_SESSION = array();
        setcookie("PHPSESSID", "", time() - 3600, "/");
        session_destroy();
        header('location: index.php');

    } else {
        desactiverMembre($_POST['id_membre'], $message);
    }
    echo $message;

}


use CollectOrMembre\MembreRepository as MembreRepository;

$membreRepository = new MembreRepository();

$membre = $membreRepository->getMembreById(intval($id_membre_session), $message);

if(isset($_POST['reactiverProfil'])){
    reactiverProfil($_POST['id_membre'], $message);
    echo $message;
}

 ?>

    <section id="sectionGererProfil">
        <p class="messagePrincipal">Bienvenue sur votre profil</p>


        <article class="coordonneesProfil">

            <img src="upload/<?php echo $membre->avatar; ?>" alt="Error loading image">


            <ul>
                <li>Nom: <?php echo $membre->nom; ?></li>
                <li>Prénom: <?php echo $membre->prenom; ?></li>
                <li>Login: <?php echo $membre->login; ?></li>
                <li>Courriel: <a href="mailto:" target="_blank"><?php echo $membre->courriel; ?></a>
                </li>
                <li>Téléphone: <?php echo $membre->tel; ?></li>

            </ul>

        </article>


        <article class="coordonneesProfil">

            <ul>
                <li><?php echo ucfirst($membre->adresse_rue); ?></li>
                <li>Code postal: <?php echo $membre->adresse_code; ?></li>
                <li>Ville: <?php echo $membre->adresse_ville; ?></li>
                <li>Province: <?php echo $membre->adresse_province; ?></li>
            </ul>

        </article>


    </section>


    <section class="boutonGererProfil">
        <form class="boutonsProfil" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

            <a class="lienModifProfil" href="modifier_Profil.php">Modifier</a>
            <?php if($membre->est_desactive == 1){ ?>
                <input class="boutonModifProfil" type="submit" name="reactiverProfil"
                       value="Ré-activer profil">
                <input type="hidden" name="id_membre" value="<?php echo $id_membre_session; ?>">
           <?php }else{ ?>
            <input class="boutonModifProfil" type="submit" name="supprimerProfil"
                   value="<?php echo MembreCanBeSuppressed($id_membre_session, $message) ? "Supprimer profil" : "Désactiver profil"; ?>">
            <input type="hidden" name="id_membre" value="<?php echo $id_membre_session; ?>">
            <?php } ?>
        </form>
    </section>


    <?php

include('inc/footer.inc.php');
?>
