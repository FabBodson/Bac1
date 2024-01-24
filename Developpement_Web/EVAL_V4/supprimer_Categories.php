<?php
$titreOnglet = "Supprimer catégorie"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Supprimer catégorie"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Supprimer catégorie";

require 'php/session.inc.php';
include('inc/header.inc.php');

use CollectOrCategorie\CategorieRepository as CategorieRepository;
use CollectOrProjet\ProjetRepository as ProjetRepository;

$categorieRepository = new CategorieRepository();
$projetRepository = new ProjetRepository();


// Suppression catégorie
if (!empty($_POST['id_categorie']) && isset($_POST['supprimerCategorie'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        supprimerCategories($_POST['id_categorie'], $message);
        echo $message;
    }
}

$listeCategories = $categorieRepository->getAllCategories($message);
?>

<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

    <fieldset>
        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <label for="id_categorie">Catégorie(s) à supprimer</label>
        <?php foreach ($listeCategories as $categorie_id) {
            $correspondance = False;
            $listeProjets = $projetRepository->getAllProjects($message);
            foreach ($listeProjets as $projet) {
                if ($projet->id_categorie == $categorie_id->id_categorie) {
                    $correspondance = True;
                    break;
                }
            }
            if ($correspondance == False) {

                ?>
                <label class="checkbox" for="check1"><input type="checkbox" name="id_categorie[]"
                                                            value="<?php echo $categorie_id->id_categorie; ?>"><?php echo $categorie_id->categorie; ?>
                </label>
                <br><br>
                <?php
            }
        } ?>
        <input class="envoi" type="submit" name="supprimerCategorie" value="Supprimer">
        <input class="effacer" type="reset" name="reset1" value="Annuler">

    </fieldset>

</form>


<?php

include('inc/footer.inc.php');
?>
