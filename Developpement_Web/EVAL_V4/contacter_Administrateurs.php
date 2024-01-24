<?php

$titreOnglet = "Contact";   /* Onglet */
$titreSite = "Collect'Or";  /* h2 */
$titrePage = "Contact";     /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Contact";

require 'php/session.inc.php';

if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre')
    include('inc/header.inc.php');
else
    include('inc/header_Anonyme.inc.php');

// Protection SPAM \\
if (!empty($_POST['spam'])) {
    $message .= "Requête refusée : origine incorrecte !<br>";
    $valid = false;
} else {
    $_POST['spam'] = " ";
    if (isset($_POST['Valider'])) {
        if (valid_email($_POST['courriel'])) {
            $message .= "Nous vous remercions pour votre message." . "<br>" . "Il sera traité dans les plus brefs délais." .
                "<br>" . "Team Collect'Or.";
            envoi_mail($_POST['courriel'], "team.collector@gmail.com", $_POST['sujet'], $_POST['contenu'], $message);
            $message = "";
            envoi_mail($_POST['courriel'], $_POST['courriel'], $_POST['sujet'], $_POST['contenu'], $message);
        }
    }
}


###### MAIN ######
?>

    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

        <fieldset>
            <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
            <label for="courriel">Courriel</label><input id="courriel" name="courriel" type="email"
                                                         value="<?php echo isset($_POST['courriel']) ? htmlentities($_POST['courriel']) : "" ?>"
                                                         required>
            <label for="sujet">Sujet du message</label><input id="sujet" name="sujet" type="text"
                                                              value="<?php echo isset($_POST['sujet']) ? htmlentities($_POST['sujet']) : "" ?>"
                                                              required>
            <textarea name="contenu" placeholder="Votre message" required></textarea>

            <input class="envoi" type="submit" name="Valider" value="Envoyer">

        </fieldset>

    </form>


<?php

include('inc/footer.inc.php');
?>