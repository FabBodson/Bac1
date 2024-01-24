<?php
$titreOnglet = "Connexion au compte"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Connexion"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Connexion";

include('inc/header_Inscription_Connexion.inc.php');
require 'php/session.inc.php';


use CollectOrMembre\MembreRepository as MembreRepository;

$membreRepository = new MembreRepository();
$message = "";


if (isset($_POST['connecter'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        if ($membreRepository->checkLogin(htmlentities($_POST['login']), htmlentities($_POST['mot_passe']), $message)) {
            $_SESSION['login'] = htmlentities($_POST['login']);
            setSession(htmlentities($_POST['login']), $message);
            header("Location: index.php");
        } else {
            echo $message;
        }
    }
}

?>


<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">

    <fieldset>
        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <label for="login">Login</label><input id="login" name="login" type="text"
                                       value="<?php echo isset($_POST['login']) ? htmlentities($_POST['login']) : ""; ?>"
                                       required>
        <label for="mot_passe">Mot de passe</label><input id="mot_passe" name="mot_passe" type="password" required>

        <input class="connecter" type="submit" name="connecter" value="Se connecter">

        <p id="renvoiInscription">Vous n'avez pas de compte ? <a href="form_Inscription.php">Inscrivez-vous ici !</a>


    </fieldset>


</form>


<?php

include('inc/footer.inc.php');
?>
