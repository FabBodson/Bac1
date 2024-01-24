<?php

namespace CollectOrMembre;
require 'db_link.inc.php';

use DB\DBLink;
use PDO;

setlocale(LC_TIME, 'fr_FR.utf8', 'fra');

/**
 * Classe Membre : membre inscrit sur collect'or
 */
class Membre
{
    private $id_membre;
    private $login;
    private $avatar;
    private $prenom;
    private $nom;
    private $courriel;
    private $mot_passe;
    private $tel;

    private $adresse_rue;
    private $adresse_numero;
    private $adresse_code;
    private $adresse_ville;
    private $adresse_province;
    private $adresse_pays;

    private $carte_VISA;

    private $est_desactive;
    private $est_admin;


    public function __get($prop)
    {
        return $this->$prop;
    }

    public function __set($prop, $val)
    {
        switch ($prop) {
            case "nom" or "prenom" or "adresse_rue" or "adresse_ville" or "adresse_pays":
                $this->$prop = ucfirst($val);
                break;

            case "courriel":
                $this->$prop = strtolower($val);
                break;
            /*
            case "mot_passe":
                $this->$prop = hash("sha512",$this->$prop);
                break;
            */
            default:
                $this->$prop = $val;
        }


    }
}

/**
 * Classe MembreRepository : gestionnaire du dépôt contenant les membres de collect'or
 */
class MembreRepository
{
    const TABLE_NAME = 'web1_membre';


    /**
     * Enregistre le membre en base de données
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var Membre $membre le membre à ajouter
     */
    public function storeMembre($membre, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("INSERT INTO " . self::TABLE_NAME . " (login, avatar, prenom, nom, courriel, mot_passe, tel, adresse_rue, adresse_numero, adresse_code, adresse_ville, adresse_province, adresse_pays, carte_VISA, est_desactive, est_admin) VALUES (:login, :avatar, :prenom, :nom, :courriel, :mot_passe, :tel, :adresse_rue, :adresse_numero, :adresse_code, :adresse_ville, :adresse_province, :adresse_pays, :carte_VISA, :est_desactive, :est_admin)");

            $stmt->bindValue(':login', $membre->login);
            $stmt->bindValue(':avatar', $membre->avatar);
            $stmt->bindValue(':prenom', $membre->prenom);
            $stmt->bindValue(':nom', $membre->nom);
            $stmt->bindValue(':courriel', $membre->courriel);
            $stmt->bindValue(':mot_passe', hash("sha512", $membre->mot_passe));
            $stmt->bindValue(':tel', $membre->tel);
            $stmt->bindValue(':adresse_rue', $membre->adresse_rue);
            $stmt->bindValue(':adresse_numero', $membre->adresse_numero);
            $stmt->bindValue(':adresse_code', $membre->adresse_code);
            $stmt->bindValue(':adresse_ville', $membre->adresse_ville);
            $stmt->bindValue(':adresse_province', $membre->adresse_province);
            $stmt->bindValue(':adresse_pays', $membre->adresse_pays);
            $stmt->bindValue(':carte_VISA', $membre->carte_VISA);
            $stmt->bindValue(':est_desactive', 0);
            $stmt->bindValue(':est_admin', 0);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "Inscription réussie !";
                $noError = true;
            } else {
                $message .= 'Une erreur système est survenue.<br> 
                    Veuillez essayer à nouveau plus tard ou contactez l\'administrateur du site. 
                    (Code erreur: ' . $stmt->errorCode() . ')<br>';
            }
            $stmt = null;
        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $noError;
    }


    /**
     * Vérifie si une valeur pour une colonne donnée existe déjà en BD
     * @return boolean true si adresse existante, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $valeur valeur à vérifier
     * @var string $colonne_table colonne de la table où aller vérifier
     */
    public function existsInDB($valeur, $colonne_table, &$message)
    {
        $result = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE $colonne_table = :valeur");
            $stmt->bindValue(':valeur', $valeur);

            if ($stmt->execute()) {
                if ($stmt->fetch() !== false) {
                    $result = true;
                }
            } else {
                $message .= 'Une erreur système est survenue.<br> 
                    Veuillez essayer à nouveau plus tard ou contactez l\'administrateur du site. 
                    (Code erreur E: ' . $stmt->errorCode() . ')<br>';
            }
            $stmt = null;
        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne tous les membres inscrits
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Member] liste des membres triés selon le nom
     */
    public function getAllMembres(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " ORDER BY nom ASC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrMembre\Membre");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne tous les membres inscrits
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Member] liste des membres triés selon le nom
     */
    public function countMembres(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->prepare("SELECT COUNT(*) FROM " . self::TABLE_NAME . ";");

            if ($result->execute()) {
                $result = $result->fetch();

            }
        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne le membre correspondant à un identifiant
     * @var integer $id_membre identifiant d'un membre
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return Membre|null le membre associé à l'identifiant
     */
    public function getMembreById($id_membre, &$message)
    {
        $result = false;
        $bdd = null;

        try {

            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE id_membre = :id_membre");
            $stmt->bindValue(':id_membre', $id_membre);

            if ($stmt->execute()) {
                $result = $stmt->fetchObject("CollectOrMembre\Membre");

            } else {
                $message .= 'Une erreur système est survenue.<br> 
                    Veuillez essayer à nouveau plus tard ou contactez l\'administrateur du site. 
                    (Code erreur E: ' . $stmt->errorCode() . ')<br>';
            }
            $stmt = null;

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne le membre correspondant à un login
     * @var integer $login login d'un membre
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return Membre|null le membre associé au login
     */
    public function getMembreByLogin($login, &$message)
    {
        $result = false;
        $bdd = null;

        try {

            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE login = :login");
            $stmt->bindValue(':login', $login);

            if ($stmt->execute()) {
                $result = $stmt->fetchObject("CollectOrMembre\Membre");

            } else {
                $message .= 'Une erreur système est survenue.<br> 
                    Veuillez essayer à nouveau plus tard ou contactez l\'administrateur du site. 
                    (Code erreur E: ' . $stmt->errorCode() . ')<br>';
            }
            $stmt = null;

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Supprime un membre sur base de son identifiant
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $id_membre identifiant du membre
     */
    public function removeMembreById($id_membre, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("DELETE FROM " . self::TABLE_NAME . " WHERE id_membre = :id_membre;");
            $stmt->bindValue(':id_membre', $id_membre);

            if ($stmt->execute()) {
                $message .= "Membre correctement supprimé.";
                $noError = true;
            } else {
                $message .= 'Une erreur système est survenue.<br> 
                    Veuillez essayer à nouveau plus tard ou contactez l\'administrateur du site. 
                    (Code erreur: ' . $stmt->errorCode() . ')<br>';
            }

            $stmt = null;
        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }

        DBLink::disconnect($bdd);
        return $noError;

    }


    /**
     * Supprime un ensemble de membres sur base de leur identifiant
     * @return boolean true si suppressions effectuées sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var [integer] $list_ids Tableau des identifiants des membres à supprimer
     */
    function deleteMembres($list_ids, &$message)
    {
        $membre = new MembreRepository();
        $nb_user_delete = 0;
        $noError = True;
        foreach ($list_ids as $membre_id) {
            $noError = $membre->removeMembreById($membre_id, $message);
            if ($noError) {
                $nb_user_delete++;
            }
        }
        $message .= $nb_user_delete . "membre(s) supprimé(s).";
        return $noError;
    }


    /**
     * Mets à jour le membre en base de données
     * @param integer $id_membre identifiant du membre à mettre à jour
     * @param string $colonne_a_modifier attribut à modifier
     * @param string $element_a_mettre nouvelle valeur à assigner
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function updateMembre($id_membre, $colonne_a_modifier, $element_a_mettre, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("UPDATE " . self::TABLE_NAME .
                " SET $colonne_a_modifier = :element_a_mettre
                WHERE id_membre = :id_membre;");

            $stmt->bindValue(':element_a_mettre', $element_a_mettre);
            $stmt->bindValue(':id_membre', $id_membre);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "Votre profil a été correctement modifié.";
                $noError = true;
            } else {
                $message .= 'Une erreur système est survenue.<br> 
                    Veuillez essayer à nouveau plus tard ou contactez l\'administrateur du site. 
                    (Code erreur: ' . $stmt->errorCode() . ')<br>';
            }
            $stmt = null;
        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $noError;
    }


    function checkLogin($login, $mot_passe, &$message)
    {
        $result = false;
        $bdd = null;
        $mot_passe = hash("sha512", $mot_passe);
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE login = :login AND mot_passe = :mot_passe");
            $stmt->bindValue(':login', $login);
            $stmt->bindValue(':mot_passe', $mot_passe);
            if ($stmt->execute()) {
                if ($stmt->fetch() != false) {
                    $result = true;
                } else {
                    $message .= 'Nom d\'utilisateur ou mot de passe incorrect<br>';
                }
            } else {
                $message .= 'Une erreur système est survenue.<br> Veuillez essayer à nouveau plus tard ou contactez l\'administrateur du site. (Code erreur: ' . $stmt->errorCode() . ')<br>';
            }
            $stmt = null;
        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        $bdd = null;
        return $result;
    }


}


?>