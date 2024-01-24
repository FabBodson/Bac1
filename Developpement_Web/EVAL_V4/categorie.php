<?php
$categorieActuelle = $_GET['categorie'];
$titreOnglet = "Catégorie " . $categorieActuelle; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = $categorieActuelle; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Catégories &gt; $categorieActuelle";


require 'php/session.inc.php';

if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre') {
    include('inc/header.inc.php');
} else {
    include('inc/header_Anonyme.inc.php');
}


use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrCategorie\CategorieRepository as CategorieRepository;
use CollectOrMembre\MembreRepository as MembreRepository;

$message = "";

$projetRepository = new ProjetRepository();
$categorieRepository = new CategorieRepository();
$membreRepository = new MembreRepository();


//récupérer la liste de projets
$listeProjets = $projetRepository->getAllProjects($message);

include('inc/annuler_Participation.inc.php');

?>


<section>
    <p class="messagePrincipal">Projets de <?php echo $categorieActuelle; ?></p>


    <h2>Quelques projets d'<?php echo $categorieActuelle; ?> en cours …</h2>

    <?php
    foreach ($listeProjets as $projet) {
        if (getIdByCategorie($projet->id_categorie) == $categorieActuelle) {
            include ('inc/apercu_Projet.inc.php');
         }

    } ?>

</section>
<?php
include('inc/footer.inc.php');
?>
