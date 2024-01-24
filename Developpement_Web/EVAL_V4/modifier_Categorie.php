<?php
$titreOnglet = "Modifier une catégorie"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Modifier une catégorie"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Modifier une catégorie";

require 'php/session.inc.php';
include('inc/header.inc.php');

use CollectOrCategorie\CategorieRepository as CategorieRepository;

$categorieRepository = new CategorieRepository();


if (isset($_POST['Valider'])) {
    // Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        modifierCategorie($_POST, $message);
        echo $message;


    }
} else {
    $listeCategories = $categorieRepository->getAllCategories($message);
    ?>

    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

        <fieldset>
            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <label for="id_categorie">Catégorie*</label>
            <select id="id_categorie" name="id_categorie">
                <?php foreach ($listeCategories as $categorie) { ?>
                    <option value="<?php echo $categorie->id_categorie; ?>"><?php echo $categorie->categorie; ?></option>
                <?php } ?>


            </select>
            <label for="nouvelleCategorie">Nouveau nom*</label><input id="nouvelleCategorie" name="nouvelleCategorie"
                                                                      type="text">

            <input class="envoi" type="submit" name="Valider" value="Envoyer">
            <input class="effacer" type="reset" name="reset1" value="Annuler">

        </fieldset>

    </form>


    <?php
}
include('inc/footer.inc.php');
?>
