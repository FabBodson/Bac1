<?php
$titreOnglet = "Modifier commentaire"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Modifier commentaire"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Détail projet &gt; Modifier commentaire";

require 'php/session.inc.php';
include('inc/header.inc.php');


if (isset($_POST['EnvoyerCommentaire'])) {
    // Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        $resultat_champs_vides = verif_champs_vide($_POST, $message);

        if ($resultat_champs_vides) {
            modifierCommentaire($_POST, $message);
        }
        echo $message;
    }
} ?>

    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

        <fieldset>
            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <textarea name="NouveauCommentaire" placeholder="Rédigez votre commentaire…" required></textarea>
            <input type="hidden" name="id_comment" value="<?php echo $_GET['id_comment']; ?>">
            <input type="hidden" name="id_projet" value="<?php echo $_GET['id_projet']; ?>">
            <input class="envoi" type="submit" name="EnvoyerCommentaire" value="Modifier">

        </fieldset>
    </form>

<?php
include('inc/footer.inc.php');
?>