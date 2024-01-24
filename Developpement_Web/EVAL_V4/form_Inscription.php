<?php
$titreOnglet = "Inscription"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Inscription"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Inscription";


include('inc/header_Inscription_Connexion.inc.php');


$erreur = "";
$nom_fichier = "";

$message = '';
$noError = True;


if (isset($_POST['Valider']) && !checkVISA($_POST['visa'])) {
    echo "<p style=\"color: red;\">Vous devez entrer un numéro de carte VISA valide.</p>";
}


if (isset($_POST['Valider'])) {
// Protection SPAM \\
    if (!empty($_POST['spam'])) {
        $message .= "Requête refusée : origine incorrecte !<br>";
        $valid = false;
    } else {
        $_POST['spam'] = " ";
        $valeurs_numeriques = array('numero', 'codeP');

        $resultat_form_inscription = isValid_form_inscription($_POST, $message);

        $resultat_champs_vide = verif_champs_vide($_POST, $message);

        $resultat_champs_numeriques = verif_champs_numerique($_POST, $valeurs_numeriques, $message);

        if ($resultat_form_inscription && $resultat_champs_vide && $resultat_champs_numeriques) {
            if (uploadFichier($_FILES['avatar'], $nom_fichier, $message)) {

                inscription($_POST, $nom_fichier, $message);
                $message = "Email envoyé";
                envoi_mail("team.collector@gmail.com", $_POST['courriel'], "Confirmation d'inscription",
                    "Bonjour " . $_POST['user'] . ",Votre inscription a bien été prise en compte.Team CollectOr.", $message);
                header("location: connexion.php");

            }
        }

        echo $message;

    }
} ?>

<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST" enctype="multipart/form-data">


    <fieldset>
        <label class="spam"><span></span><input type="text" name="spam" value=""/></label>
        <input type="hidden" name="MAX_FILE_SIZE" value="<?php echo TAILLE; ?>">
        <label for="photo">Photo de profil*</label><input id="photo" type="file" name="avatar"
                                                          accept="image/*, .jpg, .png">
        <label for="nom">Nom*</label><input id="nom" name="nom" type="text"
                                            value="<?php echo isset($_POST['nom']) ? htmlentities($_POST['nom']) : "" ?>"
                                            required>
        <label for="prenom">Prénom*</label><input id="prenom" name="prenom" type="text"
                                                  value="<?php echo isset($_POST['prenom']) ? htmlentities($_POST['prenom']) : "" ?>"
                                                  required>
        <label for="user">Login*</label><input id="user" name="user" type="text"
                                               value="<?php echo isset($_POST['user']) ? htmlentities($_POST['user']) : "" ?>"
                                               required>

        <label for="courriel">Courriel*</label><input id="courriel" name="courriel" type="email"
                                                      value="<?php echo isset($_POST['courriel']) ? htmlentities($_POST['courriel']) : "" ?>"
                                                      required>
        <label for="telephone">Telephone*</label><input id="telephone" name="telephone" type="text"
                                                       value="<?php echo isset($_POST['telephone']) ? htmlentities($_POST['telephone']) : "" ?>"
                                                       required>

        <label for="motPasse">Mot de passe*</label><input id="motPasse" name="motPasse" type="password"
                                                          value="<?php echo isset($_POST['motPasse']) ? htmlentities($_POST['motPasse']) : "" ?>"
                                                          required>
        <label for="motPasseV">Verification mot de passe*</label><input id="motPasseV" name="motPasseV"
                                                                        type="password"
                                                                        value="<?php echo isset($_POST['motPasseV']) ? htmlentities($_POST['motPasseV']) : "" ?>"
                                                                        required>


        <label for="visa">Carte VISA*</label><input id="visa" name="visa" type="text"
                                                    placeholder="ex: xxxx-xxxx-xxxx-xxxx"
                                                    value="<?php echo isset($_POST['visa']) ? htmlentities($_POST['visa']) : "" ?>"
                                                    required>


        <label for="adresse">Adresse*</label><input id="adresse" name="adresse" type="text"
                                                   value="<?php echo isset($_POST['adresse']) ? htmlentities($_POST['adresse']) : "" ?>"
                                                   required>
        <label for="numero">Numéro*</label><input id="numero" name="numero" type="number" min="1"
                                                 value="<?php echo isset($_POST['numero']) ? intval($_POST['numero']) : null ?>"
                                                 required>
        <label for="codeP">Code Postal*</label><input id="codeP" name="codeP" type="number" min="1"
                                                     value="<?php echo isset($_POST['codeP']) ? intval($_POST['codeP']) : null ?>"
                                                     required>
        <label for="localite">Localité*</label><input id="localite" name="localite" type="text"
                                                     value="<?php echo isset($_POST['localite']) ? htmlentities($_POST['localite']) : "" ?>"
                                                     required>

        <label for="province">Province*</label>
        <select id="province" name="province" required>

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

        <label for="pays">Pays*</label><input id="pays" name="pays" type="text"
                                             value="<?php echo isset($_POST['pays']) ? htmlentities($_POST['pays']) : "" ?>"
                                             required>


        <input class="envoi" type="submit" name="Valider" value="S'inscrire">
        <input class="effacer" type="reset" name="reset1" value="Annuler">

    </fieldset>


</form>


<?php

include('inc/footer.inc.php');
?>
