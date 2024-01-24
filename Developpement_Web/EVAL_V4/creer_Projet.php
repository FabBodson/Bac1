<?php
$titreOnglet = "Créer un projet"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Créer un projet"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; <a href=\"gerer_Profil.php\">Profil</a> &gt; <a href=\"mes_Projets.php\">Mes projets</a> &gt; Créer mon projet";

require 'php/session.inc.php';
include('inc/header.inc.php');

use CollectOrCategorie\CategorieRepository as CategorieRepository;

$categorieRepository = new CategorieRepository();

$erreur = "";
$nom_fichier = "";

$message = '';
$noError = True;


if (isset($_POST['Valider'])) {
    // Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        $valeurs_numeriques = array('id_categorie', 'montantProjet', 'montantMinimum');

        $resultat_form_inscription = isValid_form_projet($_POST, $message);

        $resultat_champs_vide = verif_champs_vide($_POST, $message);

        $resultat_champs_numeriques = verif_champs_numerique($_POST, $valeurs_numeriques, $message);

        if ($resultat_form_inscription && $resultat_champs_vide && $resultat_champs_numeriques) {
            if (uploadFichier($_FILES['avatar'], $nom_fichier, $message)) {
                creerProjet($_POST, $nom_fichier, $message);

            }
        }
        echo $message;

    }
} else {
    $listeCategories = $categorieRepository->getAllCategories($message);

    ?>


    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST" enctype="multipart/form-data">

        <fieldset>
            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <label for="id_categorie">Catégorie*</label>
            <select id="id_categorie" name="id_categorie">
                <?php foreach ($listeCategories as $categorie) { ?>
                    <option value="<?php echo intval($categorie->id_categorie); ?>"><?php echo $categorie->categorie; ?></option>
                <?php } ?>

            </select>

            <label for="nomProjet">Nom du projet*</label><input id="nomProjet" name="nomProjet" type="text"
                                                                value="<?php echo isset($_POST['nomProjet']) ? htmlentities($_POST['nomProjet']) : "" ?>"
                                                                required>
            <input type="hidden" name="MAX_FILE_SIZE" value="3072000">
            <label for="photo">Photo de projet*</label><input id="photo" type="file" name="avatar"
                                                              accept="image/*, .jpg, .png" required>

            <label for="montantProjet">Montant nécessaire*</label><input id="montantProjet" name="montantProjet"
                                                                         type="number" min="1" step="0.1"
                                                                         value="<?php echo isset($_POST['montantProjet']) ? htmlentities($_POST['montantProjet']) : 1 ?>"
                                                                         required>

            <label for="dateEcheance">Date d'échéance*</label><input id="dateEcheance" name="dateEcheance" type="date"
                                                                     value="<?php echo isset($_POST['dateEcheance']) ? htmlentities($_POST['dateEcheance']) : date('Y-m-d') ?>"
                                                                     required>

            <label for="description">Description du projet*</label><textarea id="description" name="description"
                                                                             placeholder="Décrivez le ici"
                                                                             required></textarea>


            <label for="typeParticipation">Type de participation*</label>
            <select id="typeParticipation" name="typeParticipation" required>
                <option value="1" selected>Don</option>
                <option value="2">Récompense</option>
                <option value="3">Prêt</option>
                <option value="4">Part du capital</option>

            </select>

            <?php if (isset($_POST['typeParticipation']) && $_POST['typeParticipation'] == 1) {
                echo "<p><span>Aucune contrepartie n’est promise au donateur</span></p>";
            } ?>

            <?php if (isset($_POST['typeParticipation']) && $_POST['typeParticipation'] == 2) {
                echo "<p><span>En fonction du montant offert, des paliers de cadeaux peuvent être proposés
                à la concrétisation du projet</span></p>";
                ?>

                <!-- Paliers des récompenses
                ainsi que leur description -->

                <label for="palierRecompense1">1er palier</label><input id="palierRecompense1" class="palierRecompense"
                                                                        type="number" name="palier1"
                                                                        step="0.1"
                                                                        min="0.0">
                <label for="typeRecompense1">Récompense</label><input id="typeRecompense1" class="typeRecompense"
                                                                      name="recompense1" type="text">


                <label for="palierRecompense2">2e palier</label><input id="palierRecompense2" class="palierRecompense"
                                                                       type="number" name="palier2"
                                                                       step="0.1"
                                                                       min="0.0">
                <label for="typeRecompense2">Récompense</label><input id="typeRecompense2" class="typeRecompense"
                                                                      name="recompense2" type="text">


                <label for="palierRecompense3">3e palier</label><input id="palierRecompense3" class="palierRecompense"
                                                                       type="number" name="palier3"
                                                                       step="0.1"
                                                                       min="0.0">
                <label for="typeRecompense3">Récompense</label><input id="typeRecompense3" class="typeRecompense"
                                                                      name="recompense3" type="text">


                <label for="palierRecompense4">4e palier</label><input id="palierRecompense4" class="palierRecompense"
                                                                       type="number" name="palier4"
                                                                       step="0.1"
                                                                       min="0.0">
                <label for="typeRecompense4">Récompense</label><input id="typeRecompense4" class="typeRecompense"
                                                                      name="recompense4" type="text">


                <label for="palierRecompense5">5e palier</label><input id="palierRecompense5" class="palierRecompense"
                                                                       type="number" name="palier5"
                                                                       step="0.1"
                                                                       min="0.0">
                <label for="typeRecompense5">Récompense</label><input id="typeRecompense5" class="typeRecompense"
                                                                      name="recompense5" type="text">


                <input class="plusDePaliers" type="button" name="PlusPaliers" value="Plus de paliers">
                <!-- Fin paliers -->

            <?php } ?>

            <?php if (isset($_POST['typeParticipation']) && $_POST['typeParticipation'] == 3) {
                echo "<p><span>Après un délai annoncé écoulé depuis la concrétisation du projet, le donateur est
                remboursé avec intérêt</span></p>";
            } ?>


            <?php if (isset($_POST['typeParticipation']) && $_POST['typeParticipation'] == 4) {
                echo "<p><span>Le donateur reçoit un certain nombre de parts de la société</span></p>";
            } ?>


            <label for="montantMinimum">Participation minimum*</label><input id="montantMinimum" type="number"
                                                                             name="montantMinimum" step="0.1" min="1"
                                                                             value="<?php echo isset($_POST['montantMinimum']) ? htmlentities($_POST['montantMinimum']) : 1 ?>"
                                                                             required>

            <?php
            if (isset($_POST['Valider']) && !checkVISA($_POST['visa'])) {
                echo "<p style=\"color: red;\">Vous devez entrer un numéro de carte VISA valide.</p>";
            }
            ?>
            <label for="visa">Numéro de VISA*</label><input id="visa" name="visa" type="text"
                                                            placeholder="ex: xxxx-xxxx-xxxx-xxxx"
                                                            value="<?php echo isset($_POST['visa']) ? htmlentities($_POST['visa']) : "" ?>"
                                                            required>

            <label for="nomTitulaire">Nom du titulaire*</label><input id="nomTitulaire" name="nomTitulaire" type="text"
                                                                      value="<?php echo isset($_POST['nomTitulaire']) ? htmlentities($_POST['nomTitulaire']) : "" ?>"
                                                                      required>


            <input type="hidden" name="id_membre" value="<?php echo $id_membre_session; ?>">
            <input class="envoi" type="submit" name="Valider" value="Créer projet">
            <input class="effacer" type="reset" name="reset1" value="Annuler">

        </fieldset>


    </form>

    <?php
}
include('inc/footer.inc.php');
?>