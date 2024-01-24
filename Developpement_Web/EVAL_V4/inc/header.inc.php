<!DOCTYPE html>
<?php

require 'php/fonctions.inc.php';



if (isset($_POST['deconnexion'])) {
    $_SESSION = array();
    setcookie("PHPSESSID", "", time() - 3600, "/");
    session_destroy();
    header('location: index.php');
}

use CollectOrMembre\MembreRepository as MembreRepository;
use CollectOrCategorie\CategorieRepository as CategorieRepository;


$membre = new MembreRepository();
$categorie = new CategorieRepository();

$listeCategories = $categorie->getAllCategories($message);



?>
<html lang="fr">

<head>
    <meta charset="utf-8"/>
    <title><?php echo $titreOnglet; ?></title>
    <link rel="stylesheet" type="text/css" href="css/style_collector.css">
    <link href="https://use.fontawesome.com/releases/v5.0.7/css/all.css" rel="stylesheet">
</head>


<body>


<header>
    <h2 class="titrePage"><a href="index.php"><?php echo $titreSite; ?></a></h2>

    <h1><?php echo $titrePage; ?></h1>


    <nav class="navProfil">
        <div class="filAriane"><?php echo $filAriane; ?></div>

        <ul>
            <li class="versProfil"><a href="#"><i class="fas fa-user"></i class="fas fa-user">&ensp;<?php echo $login_session; ?>&ensp;</a>

                <ul class="listeGererProfil">
                    <li class="elementListeProfil"><a href="gerer_Profil.php">Profil</a></li>

                    <li class="elementListeProfil">
                        <form class="deconnexion" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
                            <input id="btnDeconnexion" type="submit" name="deconnexion" value="Déconnexion">
                        </form>
                    </li>

                </ul>

            </li>
        </ul>

    </nav>


    <nav class="navigation">

        <a class="mesParticipations" href="mes_Participations.php">Mes participations</a>
        <a class="mesParticipations" href="mes_Projets.php">Mes projets</a>
        <a class="mesParticipations" href="creer_Projet.php">Créer un projet</a>
        <a class="mesParticipations" href="imprimer_Projet.php">Imprimer mes participations</a>
        <?php if($statut == 'admin'){ ?>
        <a class="mesParticipations" href="valider_Projets.php">Valider des projets</a>
        <?php } ?>
        <a class="mesParticipations" href="recherche.php">Recherche</a>

    </nav>


    <nav class="navCategories">
        <!-- Catégories -->
        <ul>
            <li class="categories"><a href="#">Catégories&ensp;</a>
                <ul class="listeCategories">
                    <?php foreach ($listeCategories as $categorie_id) { ?>
                            <li>
                                <a href="categorie.php?categorie=<?php echo $categorie_id->categorie; ?>"><?php echo $categorie_id->categorie; ?></a>
                            </li>
                        <?php
                    }?>

                </ul>
            </li>
            <?php if ($statut == 'admin') { ?>
            <li class="ajouter_categorie"><a href="ajouter_Categorie.php">Ajouter une catégorie</a></li>
            <li class="ajouter_categorie"><a href="supprimer_Categories.php">Supprimer catégorie</a></li>
            <li><a href="modifier_Categorie.php">Modifier une catégorie</a></li>
            <?php } ?>
        </ul>



        <!-- Filtres -->
        <ul>
            <li class="categories"><a href="#">Filtres&ensp;</a>

                <ul class="listeFiltres">

                    <li><a href="derniers_Projets.php">Derniers projets</a></li>
                    <li><a href="index.php">Echeances</a></li>
                    <li><a href="taux_Quasi_Complet.php">Bientot finis</a></li>
                    <li><a href="projets_Finis.php">Projets financés</a></li>

                </ul>

            </li>
        </ul>

    </nav>


</header>


<main>
