<?php

require 'db_categorie.inc.php';

require '../PHPMailer/src/PHPMailer.php';
require '../PHPMailer/src/Exception.php';


use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;


use CollectOrMembre\MembreRepository as MembreRepository;
use CollectOrMembre\Membre as Membre;

use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrProjet\Projet as Projet;

use CollectOrCommentaire\CommentaireRepository as CommentaireRepository;
use CollectOrCommentaire\Commentaire as Commentaire;

use CollectOrNews\NewsRepository as NewsRepository;
use CollectOrNews\News as News;

use CollectOrParticipation\ParticipationRepository as ParticipationRepository;
use CollectOrParticipation\Participation as Participation;

use CollectOrCategorie\CategorieRepository as CategorieRepository;
use CollectOrCategorie\Categorie as Categorie;


// Fonctions formulaires


function envoi_mail($envoyeur, $receveur, $sujet, $contenu, &$message)
{

    $mail = new PHPMailer(true);

    try {

        $mail->CharSet = 'UTF-8';

        $mail->setFrom($envoyeur);

        $mail->addAddress($receveur);  //placez VOTRE adresse courriel

        $mail->addReplyTo('no-reply@helmo.be');

        $mail->isHTML(false);

        $mail->Subject = $sujet;

        $mail->Body = $contenu;

        $mail->send();

        echo $message;

    } catch (Exception $e) {

        return 'Erreur survenue lors de l\'envoi de l\'email<br>' . $mail->ErrorInfo;

    }

}


function verif_champs_vide($post, &$message)
{
    foreach ($post as $cle => $valeur) {
        if (empty($valeur)) {
            $message .= "Le champs " . $cle . " ne peut pas être vide.";
        }
    }
    return (empty($message)) ? True : False;
}


function verif_champs_numerique($post, $tab_champs, &$message)
{
    foreach ($tab_champs as $valeur) {
        if (!is_numeric($post[$valeur])) {
            $message .= "Le champs " . $valeur . " doit etre numérique.";
        }
    }
    return (empty($message)) ? True : False;
}


function uploadFichier($fichier, &$nom_fichier, &$message)
{

    if ($fichier['error'] > 0) {

        switch ($fichier['error']) {
            case UPLOAD_ERR_NO_FILE:
                $message .= 'Pas de fichier spcécifié';
                break;

            case UPLOAD_ERR_INI_SIZE:
                $message .= 'Taille fichier dépassant la limite autorisée par PHP';
                break;

            case UPLOAD_ERR_FORM_SIZE:
                $message .= 'Taille fichier dépassant la limite autorisée par le formulaire';
                break;

            case UPLOAD_ERR_PARTIAL:
                $message .= 'Fichier transféré partiellement';
                break;
        }

        return (empty($message)) ? True : False;
    }
    $nom_fichier = uniqid();

    $extension = pathinfo($fichier['name']);
    $nom_fichier = $nom_fichier . '.' . $extension['extension'];


    if (!move_uploaded_file($fichier['tmp_name'], REPERTOIRE_UPLOAD . $nom_fichier)) {
        $message .= 'Une erreur est survenue lors de la copie sur le serveur. Veuillez réessayer plus tard';
    }
    return (empty($message)) ? True : False;
}


function checkVISA($numVISA)
{
    $visaValide = True;
    $change = str_replace(array("-", " ", ".", "/"), "", $numVISA);
    $change_inverse = strrev($change);

    $somme = 0;
    for ($i = 0; $i < strlen($change_inverse); $i++) {
        $nb_temp = $change_inverse[$i];
        switch ($nb_temp) {
            case ($nb_temp % 2) == 0:
                $somme += $nb_temp;
                break;

            case ($nb_temp % 2) !== 0:
                $nb_temp *= 2;
                if ($nb_temp > 9):
                    $nb_temp -= 9;
                endif;
                $somme += $nb_temp;
                break;

            default:
                break;
        }
    }
    if ($somme % 10 == 0) {
        return $visaValide;
    } else
        $visaValide = False;
    return $visaValide;
}


/// FONCTIONS CREATION PROFIL \\\


function checkProvince($p)
{
    return in_array($p, array('Anvers', 'Brabant Flamand', 'Brabant Wallon', 'Bruxelles', 'Flandre Occidentale', 'Flandre Orientale',
        'Hainaut', 'Liège', 'Limbourg', 'Luxembourg', 'Namur'), true);
}

function valid_email($email)
{
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}


function isValid_form_inscription($tab_post, &$message)
{

    if (!checkVISA($tab_post['visa'])) {
        $message .= " VISA invalide";
    }

    if (!checkProvince($tab_post['province'])) {
        $message .= " Province invalide";
    }

    if (trim($tab_post['motPasse']) != trim($tab_post['motPasseV'])) {
        $message .= " Mots de passes differents";
    }

    if (!valid_email($tab_post['courriel'])) {
        $message .= " Email invalide";
    }

    $membreRepository = new MembreRepository();
    if ($membreRepository->existsInDB($tab_post['courriel'], 'courriel', $message)) {
        $message .= " Email deja existant";
    }

    if ($membreRepository->existsInDB($tab_post['user'], "login", $message)) {
        $message .= " Login deja existant";
    }

    return (empty($message)) ? True : False;
}


function inscription($post, $nom_fichier, &$message)
{
    $membre = new Membre();

    $membre->login = trim($post['user']);
    $membre->avatar = trim($nom_fichier);
    $membre->prenom = trim($post['prenom']);
    $membre->nom = trim($post['nom']);
    $membre->courriel = trim($post['courriel']);
    $membre->mot_passe = trim($post['motPasse']);
    $membre->tel = trim($post['telephone']);
    $membre->adresse_rue = trim($post['adresse']);
    $membre->adresse_numero = intval($post['numero']);
    $membre->adresse_code = intval($post['codeP']);
    $membre->adresse_ville = trim($post['localite']);
    $membre->adresse_province = trim($post['province']);
    $membre->adresse_pays = trim($post['pays']);
    $membre->carte_VISA = trim(str_replace(array("-", " ", ".", "/"), "", $post['visa']));

    $membreRepository = new MembreRepository();

    $membreRepository->storeMembre($membre, $message);

}


function MembreCanBeSuppressed($id_membre, &$message)
{
    $projetRepository = new ProjetRepository();
    $participationRepository = new ParticipationRepository();
    $commentaireRepository = new CommentaireRepository();

    $exist_in_projet = $projetRepository->existsInDB($id_membre, 'id_membre', $message);
    $exist_in_participation = $participationRepository->existsInDB($id_membre, 'id_membre', $message);
    $exist_in_commentaire = $commentaireRepository->existsInDB($id_membre, $message);

    if ($exist_in_projet) {
        $message .= " Ce profil ne peut pas etre supprimé car il possède à un ou plusieurs projet(s)";
    }

    if ($exist_in_participation) {
        $message .= " Ce profil ne peut pas etre supprimé car il participe à un ou plusieurs projet(s)";
    }

    if ($exist_in_commentaire) {
        $message .= " Ce profil ne peut pas etre supprimé car il a posté un ou plusieurs commentaire(s)";
    }

    return (empty($message)) ? True : False;
}


function supprimerMembre($id_membre, &$message)
{
    $membreRepository = new MembreRepository();

    $membreRepository->removeMembreById($id_membre, $message);
}


function desactiverMembre($id_membre, &$message)
{
    $membreRepository = new MembreRepository();

    $membreRepository->updateMembre($id_membre, "est_desactive", 1, $message);

}


function reactiverProfil($id_membre, &$message)
{
    $membreRepository = new MembreRepository();

    $membreRepository->updateMembre($id_membre, "est_desactive", 0, $message);

}


function isValid_form_modifierProfil($tab_post, &$message)
{
    if (!empty($tab_post['visa'])) {
        if (!checkVISA($tab_post['visa'])) {
            $message .= " VISA invalide";
        }
    }

    if (!empty($tab_post['province'])) {
        if (!checkProvince($tab_post['province'])) {
            $message .= " Province invalide";
        }
    }

    if (!empty($tab_post['motPasse'])) {
        if (trim($tab_post['motPasse']) != trim($tab_post['motPasseV'])) {
            $message .= " Mots de passes differents";
        }
    }

    if (!empty($tab_post['courriel'])) {
        if (!valid_email($tab_post['courriel'])) {
            $message .= " Email invalide";
        }
    }

    return (empty($message)) ? True : False;
}


function modifierProfil($post, &$nom_fichier, &$message)
{
    $membreRepository = new MembreRepository();

    if (uploadFichier($_FILES['avatar'], $nom_fichier, $message)) {
        $membreRepository->updateMembre($post['id_membre'], "avatar", $nom_fichier, $message);
    } else {
        $message = "";
    }

    if (!empty($post['courriel'])) {
        if (!valid_email($post['courriel'])) {
            $message .= "Email invalide";

        } else {
            if ($membreRepository->existsInDB($post['courriel'], 'courriel', $message)) {
                $message .= "Email deja existant";
            } else {
                $membreRepository->updateMembre($post['id_membre'], "courriel", $post['courriel'], $message);
            }
        }
    }

    if (!empty($post['motPasse'])) {
        if (trim($post['motPasse']) != trim($post['motPasseV'])) {
            $message .= "Mots de passes differents";
        } else {
            $membreRepository->updateMembre($post['id_membre'], "mot_passe", $post['motPasse'], $message);
        }
    }

    if (!empty($post['visa'])) {
        if (!checkVISA($post['visa'])) {
            $message .= "VISA invalide";
        } else {
            $membreRepository->updateMembre($post['id_membre'], "carte_VISA", $post['visa'], $message);
        }
    }

    if (!empty($post['adresse'])) {
        $membreRepository->updateMembre($post['id_membre'], "adresse_rue", $post['adresse'], $message);
    }

    if (!empty($post['numero'])) {
        if (!is_numeric($post['numero'])) {
            $message .= "Le champs 'Numéro' doit etre numérique.";
        } else {
            $membreRepository->updateMembre($post['id_membre'], "adresse_numero", $post['numero'], $message);
        }
    }

    if (!empty($post['codeP'])) {
        if (!is_numeric($post['codeP'])) {
            $message .= "Le champs 'code postal' doit etre numérique.";
        } else {
            $membreRepository->updateMembre($post['id_membre'], "adresse_code", $post['codeP'], $message);
        }
    }

    if (!empty($post['localite'])) {
        $membreRepository->updateMembre($post['id_membre'], "adresse_ville", $post['localite'], $message);
    }

    if (!empty($post['province'])) {
        if (!checkProvince($post['province'])) {
            $message .= "Province invalide";
        } else {
            $membreRepository->updateMembre($post['id_membre'], "adresse_province", $post['province'], $message);
        }
    }

    if (!empty($post['pays'])) {
        $membreRepository->updateMembre($post['id_membre'], "adresse_pays", $post['pays'], $message);
    }

}

/*
 * 1 ADMIN
 * 2 PORTEUR PROJET
 * 3 MEMBRE
 * 4 ANONYME
 */

function setSession($login, &$message)
{
    $membreRepository = new MembreRepository();
    $projetRepository = new ProjetRepository();

    $membre = $membreRepository->getMembreByLogin($login, $message); // retourne objet Membre

    $id_membre = $membre->id_membre;

    $est_admin = $membre->est_admin;


    $porteur_projet = $projetRepository->getCreateurProjet($id_membre, $message); // retourne login correspondant à l'id_membre

    if ($est_admin == 1) {
        $_SESSION['statut'] = 'admin';
        $_SESSION['id_membre'] = $id_membre;
    } else {
        if ($login == $porteur_projet) {
            $_SESSION['statut'] = 'porteurProjet';
            $_SESSION['id_membre'] = $id_membre;
        } else {
            $_SESSION['statut'] = 'membre';
            $_SESSION['id_membre'] = $id_membre;
        }
    }
}


/// FONCTIONS CREATION PROJET \\\


function checkCategorie($g, &$message)
{
    $categorieRepository = new CategorieRepository();
    $listeCategories = $categorieRepository->getAllCategories($message);

    foreach ($listeCategories as $categorie) {
        if ($g == $categorie->id_categorie) {
            return True;
        }
    }
    return False;
}


function checkContrePartie($cp)
{
    return in_array($cp, array('1', '2', '3', '4'), true);
}


function isValid_form_projet($tab_post, &$message)
{

    if (!checkVISA($tab_post['visa'])) {
        $message .= "VISA invalide";
    }

    if ($tab_post['montantProjet'] <= 0 or $tab_post['montantMinimum'] <= 0) {
        $message .= "Montant(s) invalide(s)";
    }

    if ($tab_post['dateEcheance'] <= date('Y-m-d')) {
        $message .= "Date d'échéance invalide";
    }

    if (!checkCategorie($tab_post['id_categorie'], $message)) {
        $message .= "Catégorie non valide";
    }

    if (!checkContrePartie($tab_post['typeParticipation'])) {
        $message .= "Type de participation non valide";
    }


    $projetRepository = new ProjetRepository();
    $existe_visa = $projetRepository->existsInDB($tab_post['visa'], "carte_VISA", $message);
    $existe_intitule = $projetRepository->existsInDB($tab_post['nomProjet'], 'intitule', $message);

    if ($existe_intitule && $existe_visa) {
        $message .= "Pas possible d'avoir le meme nom et la meme carte VISA qu'un autre projet";
    }

    return (empty($message)) ? True : False;
}


function supprimerProjet($id_projet, &$message)
{
    $projetRepository = new ProjetRepository();
    $projet = $projetRepository->getProjectById($id_projet, $message);

    if ($projet->montant_actuel < $projet->montant) {
        return $projetRepository->removeProjectById($id_projet, $message);
    }
    return False;
}


function prolongerProjet($post, &$message)
{
    $projetRepository = new ProjetRepository();
    $projet = $projetRepository->getProjectById($post['id_projet'], $message);

    if ($projet->montant_actuel < $projet->montant) {
        $projetRepository->updateProjet($post['id_projet'], "est_prolonge", 1, $message);
        $projetRepository->prolongerProjet($post['id_projet'], $post['nvDateEcheance'], $message);
    }
}


function validerProjet($id_projet, &$message)
{
    $projetRepository = new ProjetRepository();
    $projetRepository->updateProjet($id_projet, "est_valide", 1, $message);
}


function creerProjet($post, $nom_fichier, &$message)
{
    $projet = new Projet();

    $projet->intitule = trim($post['nomProjet']);
    $projet->date_echeance = trim($post['dateEcheance']);
    $projet->date_creation = date('Y-m-d');
    $projet->description = ucfirst(trim($post['description']));
    $projet->montant = trim($post['montantProjet']);
    $projet->montant_actuel = 0;

    $projet->montant_minimum = trim($post['montantMinimum']);
    $projet->illustration_apercu = trim($nom_fichier);
    $projet->carte_VISA = trim($post['visa']);
    $projet->nom_VISA = trim($post['nomTitulaire']);

    $projet->est_prolonge = 0;
    $projet->est_valide = 0;
    $projet->taux_participation = $projet->montant_actuel / $projet->montant;

    $projet->id_membre = $post['id_membre'];
    $projet->id_type_part = trim($post['typeParticipation']);
    $projet->id_categorie = trim($post['id_categorie']);


    $projetRepository = new ProjetRepository();

    $projetRepository->storeProject($projet, $message);
}


function modifierProjet($post, &$nom_fichier, &$message)
{
    $projetRepository = new ProjetRepository();
    if (uploadFichier($_FILES['avatar'], $nom_fichier, $message)) {
        $projetRepository->updatePhotoProjet($post['id_projet'], $nom_fichier, $message);

    }
    if (!empty($post['description'])) {
        $projetRepository->updateDescriptionProjet($post['id_projet'], $post['description'], $message);
    }


}


function calculerMontantActuel($id_projet, &$message)
{
    $participationRepository = new ParticipationRepository();
    $projetRepository = new ProjetRepository();
    $montant_actuel = $participationRepository->updateMontantActuel($id_projet, $message)[0];

    if ($montant_actuel == null) {
        $montant_actuel = 0;
    }
    if ($projetRepository->updateProjet($id_projet, 'montant_actuel',
        $montant_actuel, $message)) {
        $message = "";
        return True;
    } else {
        return False;
    }
}

function updateTauxPart($id_projet, &$message)
{
    $projetRepository = new ProjetRepository();
    $projet = $projetRepository->getProjectById($id_projet, $message);

    $nouveau_taux = round($projet->montant_actuel / $projet->montant, 2);

    if ($nouveau_taux != null) {
        $projetRepository->updateProjet($id_projet, 'taux_participation',
            $nouveau_taux, $message);
    } else
        $nouveau_taux = 0;
    $projetRepository->updateProjet($id_projet, 'taux_participation',
        $nouveau_taux, $message);
}


// Fonctions commentaires

function supprimerCommentaire($id_comment, &$message)
{
    $commentaireRepository = new CommentaireRepository();
    return $commentaireRepository->removeCommentaireById($id_comment, $message);
}


function ajouterCommentaire($post, &$message)
{
    $commentaire = new Commentaire();

    $commentaire->commentaire = trim($post['NouveauCommentaire']);
    $commentaire->date_mise_en_ligne = date('Y-m-d');
    $commentaire->id_projet = $post['id_projet'];
    $commentaire->id_membre = $post['id_membre'];

    $commentaireRepository = new CommentaireRepository();

    $commentaireRepository->storeCommentaire($commentaire, $message);
}


function modifierCommentaire($post, &$message)
{
    $commentaireRepository = new CommentaireRepository();

    $commentaireRepository->updateCommentaire($post['id_comment'], "commentaire", $_POST['NouveauCommentaire'], $message);
    $commentaireRepository->updateCommentaire($post['id_comment'], "date_mise_en_ligne", date('Y-m-d'), $message);
}


// Fonctions news

function isValid_news($post, &$message)
{
    $newsRepository = new NewsRepository();

    if ($newsRepository->existsInDB($post['sujet'], "intitule", $message)) {
        $message .= "Intitule de news deja existant";
    }

    if ($newsRepository->existsInDB($post['message'], "description", $message)) {
        $message .= "Description deja existante";
    }

    return (empty($message)) ? True : False;
}


function supprimerNews($id_news, &$message)
{
    $newsRepository = new NewsRepository();

    return $newsRepository->removeNewsById($id_news, $message);
}


function ajouterNews($post, &$message)
{
    $news = new News();

    $news->intitule = trim($post['sujet']);
    $news->description = trim($post['message']);
    $news->date_publication = date('Y-m-d');
    $news->id_projet = $post['id_projet'];

    $newsRepository = new NewsRepository();
    $newsRepository->storeNews($news, $message);

}


function modifierNews($post, &$message)
{
    $newsRepository = new NewsRepository();

    if (isValid_news($post, $message)) {
        if (!empty($post['sujet'])) {
            $newsRepository->updateNews($post['sujet'], 'intitule', $post['id_news'], $message);
        }

        if (!empty($post['message'])) {
            $newsRepository->updateNews($post['message'], 'description', $post['id_news'], $message);
        }
    }
}


// Fontions participations

function isValid_participation($post, &$message)
{
    $participationRepository = new ParticipationRepository();

    $existe_part = $participationRepository->existsInDB($post['id_projet'], $post['id_membre'], $message);
    if ($existe_part) {
        $message .= "Vous avez deja participé à ce projet";
    }

    return (empty($message)) ? True : False;

}


function participer($post, &$message)
{
    $participation = new Participation();

    $participation->date_participation = date('Y-m-d');
    $participation->montant = $post['sommeVersement'];
    $participation->id_membre = $post['id_membre'];
    $participation->id_projet = $post['id_projet'];

    $participationRepository = new ParticipationRepository();

    $participationRepository->storeParticipation($participation, $message);
}


function annulerParticipation($post, &$message)
{
    $participationRepository = new ParticipationRepository();
    if ($participationRepository->existsInDB($post['id_projet'], $post['id_membre'], $message)) {

        $participation = $participationRepository->getParticipationByIdProjetIdMembre($post['id_projet'], $post['id_membre'], $message);
        $participationRepository->removeParticipationById($participation->id_participation, $message);
    }
}


function aParticipe($id_membre, $id_projet, &$message)
{
    $participationRepository = new ParticipationRepository();

    return $participationRepository->existsInDB($id_projet, $id_membre, $message);
}


function nombreParticipations($id_membre, &$message)
{
    $participationRepository = new ParticipationRepository();

    if($participationRepository->countNombrePart($id_membre, $message)[0] == null)
        return 0;
    else
        return $participationRepository->countNombrePart($id_membre, $message)[0];
}


function montantTotalPromis($id_membre, &$message)
{
    $participationRepository = new ParticipationRepository();

    if($participationRepository->countMontantPromis($id_membre, $message)[0] == null)
        return 0;
    else
        return $participationRepository->countMontantPromis($id_membre, $message)[0];
}


function montantTotalPreleve($id_membre, &$message)
{
    $participationRepository = new ParticipationRepository();

    if ($participationRepository->countMontantPreleve($id_membre, $message)[0] == null) {
        return 0;
    } else {
        return $participationRepository->countMontantPreleve($id_membre, $message)[0];
    }
}


// Fonctions categories

function isValid_categorie($post, &$message)
{
    $categorieRepository = new CategorieRepository();
    if ($categorieRepository->existsInDB($post['ajoutCategorie'], 'categorie', $message)) {
        $message .= "Catégorie deja existante";
    }
    return (empty($message)) ? True : False;
}

function getIdByCategorie($id)
{
    $categorieRepository = new CategorieRepository();
    return $categorieRepository->getCategorieById($id, $message)->categorie;
}


function ajouterCategorie($post, &$message)
{
    $categorie = new Categorie();

    $categorie->categorie = ucfirst(trim($post['ajoutCategorie']));

    $categorierRepository = new CategorieRepository();

    $categorierRepository->storeCategorie($categorie, $message);

}


function modifierCategorie($post, &$message)
{
    $categorieRepository = new CategorieRepository();

    if (!empty($post['id_categorie']) && !empty($post['nouvelleCategorie'])) {
        if ($categorieRepository->existsInDB($post['nouvelleCategorie'], 'categorie', $message)) {
            $message .= "Catégorie deja existante";

        } elseif (!checkCategorie($post['id_categorie'], $message)) {
            $message .= "Catégorie non valide";

        } else {
            $categorieRepository->updateCategorie($post['id_categorie'], $post['nouvelleCategorie'], $message);
        }
    }
}


function supprimerCategories($id_categorie, &$message)
{

    $categorieRepository = new CategorieRepository();

    $categorieRepository->deleteCategories($id_categorie, $message);
}


?>