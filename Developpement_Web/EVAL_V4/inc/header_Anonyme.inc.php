<!DOCTYPE html>
<?php
require 'php/fonctions.inc.php';

use CollectOrCategorie\CategorieRepository as CategorieRepository;

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
    <h1 id="titreReferencement"><?php echo $titreReferencement; ?></h1>

    <h2 class="titrePage"><a href="index.php"><?php echo $titreSite; ?></a></h2>

    <h1><?php echo $titrePage; ?></h1>


    <nav class="navProfil">
        <div class="filAriane"><?php echo $filAriane; ?></div>

        <ul class="versProfil">
            <li><a href="connexion.php">Connexion</a></li>
            <li><a href="form_Inscription.php">S'inscrire</a></li>
        </ul>
    </nav>


    <nav class="navigation">

        <a class="elementCache" href="#">Mes participations</a>
        <a class="mesParticipations" href="recherche.php">Recherche</a>

    </nav>


    <nav class="navCategories">
        <!-- Catégories -->
        <ul class="ulCategories">
            <li class="categories"><a href="#">Catégories&ensp;</a>

                <ul class="listeCategories">
                    <?php foreach ($listeCategories as $categorie_id){  ?>

                        <li><a href="categorie.php?categorie=<?php echo $categorie_id->categorie; ?>"><?php echo $categorie_id->categorie; ?></a></li>

                    <?php } ?>
                </ul>

            </li>
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
