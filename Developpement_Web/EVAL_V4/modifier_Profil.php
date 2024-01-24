<?php
$titreOnglet = "Modifier profil"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Modifier mon profil"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; <a href=\"gerer_Profil.php\">Mon profil</a> &gt; Modifier Profil";

require 'php/session.inc.php';
include('inc/header.inc.php');

use CollectOrMembre\MembreRepository as MembreRepository;

$erreur = "";
$nom_fichier = "";

$message = '';
$noError = True;
$membreRepository = new MembreRepository();

if (isset($_POST['Valider'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";

        $valeurs_numeriques = array();

        if (!empty($_POST['numero']) && is_numeric($_POST['numero'])) {
            $valeurs_numeriques[] = 'numero';
        }
        if (!empty($_POST['codeP']) && is_numeric($_POST['codeP'])) {
            $valeurs_numeriques[] = 'codeP';
        }

        $resultat_form_modif = isValid_form_modifierProfil($_POST, $message);

        if (!empty($valeurs_numeriques))
            $resultat_champs_numeriques = verif_champs_numerique($_POST, $valeurs_numeriques, $message);
        else
            $resultat_champs_numeriques = True;


        if ($resultat_form_modif && $resultat_champs_numeriques) {
            modifierProfil($_POST, $nom_fichier, $message);
        }
        echo $message;
    }
}

$membre = $membreRepository->getMembreById($id_membre_session, $message);
?>


<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST" enctype="multipart/form-data">

    <fieldset>
        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <input type="hidden" name="MAX_FILE_SIZE" value="3072000">
        <label for="photo">Photo de profil</label><input id="photo" type="file" name="avatar"
                                                         accept="image/*, .jpg, .png">


        <label for="courriel">Courriel</label><input id="courriel" name="courriel" type="email"
                                                     value="<?php echo isset($_POST['courriel']) ? htmlentities($_POST['courriel']) : ""; ?>">

        <label for="telephone">Telephone</label><input id="telephone" name="telephone" type="text"
                                                       value="<?php echo isset($_POST['telephone']) ? htmlentities($_POST['telephone']) : ""; ?>">

        <label for="motPasse">Mot de passe</label><input id="motPasse" name="motPasse" type="password"
                                                         value="<?php echo isset($_POST['motPasse']) ? htmlentities($_POST['motPasse']) : ""; ?>">

        <label for="motPasseV">Verification mot de passe</label><input id="motPasseV" name="motPasseV"
                                                                       type="password"
                                                                       value="<?php echo isset($_POST['motPasseV']) ? htmlentities($_POST['motPasseV']) : ""; ?>">


        <label for="visa">Carte VISA</label><input id="visa" name="visa" type="text"
                                                   placeholder="ex: xxxx-xxxx-xxxx-xxxx"
                                                   value="<?php echo isset($_POST['visa']) ? htmlentities($_POST['visa']) : ""; ?>">


        <label for="adresse">Adresse</label><input id="adresse" name="adresse" type="text"
                                                   value="<?php echo isset($_POST['adresse']) ? htmlentities($_POST['adresse']) : ""; ?>">

        <label for="numero">Numéro</label><input id="numero" name="numero" type="number" min="1"
                                                 value="<?php echo isset($_POST['numero']) ? intval($_POST['numero']) : null; ?>">

        <label for="codeP">Code Postal</label><input id="codeP" name="codeP" type="number" min="1"
                                                     value="<?php echo isset($_POST['codeP']) ? intval($_POST['codeP']) : null; ?>">

        <label for="localite">Localité</label><input id="localite" name="localite" type="text"
                                                     value="<?php echo isset($_POST['localite']) ? htmlentities($_POST['localite']) : ""; ?>">

        <label for="province">Province</label>
        <select id="province" name="province">
            <option value="">---</option>
            <option value="Anvers">Anvers</option>
            <option value="Brabant Flamand">Brabant Flamand</option>
            <option value="Brabant Wallon">Brabant Wallon</option>
            <option value="Buxelles">Buxelles</option>
            <option value="Flandre Occidentale">Flandre Occidentale</option>
            <option value="Flandre Orientale">Flandre Orientale</option>
            <option value="Hainaut">Hainaut</option>
            <option value="Liège">Liège</option>
            <option value="Limbourg">Limbourg</option>
            <option value="Luxembourg">Luxembourg</option>
            <option value="Namur">Namur</option>

        </select>

        <label for="pays">Pays</label><input id="pays" name="pays" type="text"
                                             value="<?php echo isset($_POST['pays']) ? htmlentities($_POST['pays']) : ""; ?>">

        <input type="hidden" name="id_membre" value="<?php echo $id_membre_session; ?>">
        <input class="envoi" type="submit" name="Valider" value="Modifier">
        <input class="effacer" type="reset" name="reset1" value="Annuler">


    </fieldset>

</form>


<?php

include('inc/footer.inc.php');
?>
