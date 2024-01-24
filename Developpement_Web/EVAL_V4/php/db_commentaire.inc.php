<?php

namespace CollectOrCommentaire;
require 'db_projet.inc.php';

use DB\DBLink;
use PDO;

setlocale(LC_TIME, 'fr_FR.utf8', 'fra');

/**
 * Classe Commentaire : commentaire d'un projet
 */
class Commentaire
{
    private $id_comment;
    private $commentaire;
    private $date_mise_en_ligne;
    private $id_projet;
    private $id_membre;



    public function __get($prop)
    {

        return $this->$prop;
    }

    public function __set($prop, $val)
    {
        $this->$prop = $val;
    }
}

/**
 * Classe CommentaireRepository : gestionnaire du dépôt contenant les commentaires de collect'or
 */
class CommentaireRepository
{
    const TABLE_NAME = 'web1_commentaire';


    /**
     * Enregistre le commentaire en base de données
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var Commentaire $commentaire le commentaire à ajouter
     */
    public function storeCommentaire($commentaire, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("INSERT INTO " . self::TABLE_NAME . " (commentaire, date_mise_en_ligne, id_projet, id_membre) 
            VALUES (:commentaire, :date_mise_en_ligne, :id_projet, :id_membre)");

            $stmt->bindValue(':commentaire', $commentaire->commentaire);
            $stmt->bindValue(':date_mise_en_ligne', $commentaire->date_mise_en_ligne);
            $stmt->bindValue(':id_projet', $commentaire->id_projet);
            $stmt->bindValue(':id_membre', $commentaire->id_membre);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "Commentaire posté !";
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
     * @var string $id_projet valeur à vérifier
     * @var string $id_membre valeur à vérifier
     */
    public function existsInDB($id_membre, &$message)
    {
        $result = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " 
            WHERE id_membre = :id_membre;");
            $stmt->bindValue(':id_membre', $id_membre);

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
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return [Commentaire] liste des commentaires triés selon la date de mise en ligne
     */
    public function getAllCommentaires(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " ORDER BY date_mise_en_ligne ASC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrCommentaire\Commentaire");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }




    /**
     * Retourne tous les membres inscrits
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return [Commentaire] liste des commentaires triés selon la date de mise en ligne
     */
    public function gcountCommentaires(&$message)
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
     * Retourne le commentaire correspondant à un identifiant
     * @var integer $id identifiant d'un commentaire
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return Commentaire|null le commentaire associé à l'identifiant
     */
    public function getCommentaireById($id_comment, &$message)
    {
        $result = false;
        $bdd = null;

        try {

            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE id_comment = :id_comment");
            $stmt->bindValue(':id_comment', $id_comment);

            if ($stmt->execute()) {
                $result = $stmt->fetchObject("CollectOrCommentaire\Commentaire");

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
     * Supprime un commentaire sur base de son identifiant
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var integer $id identifiant du commentaire
     */
    public function removeCommentaireById($id_comment, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("DELETE FROM " . self::TABLE_NAME . " WHERE id_comment = $id_comment;");

            if ($stmt->execute()) {
                $message .= "Commentaire correctement supprimé.";
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
     * Supprime un ensemble de commentaires sur base de leur identifiant
     * @return boolean true si suppressions effectuées sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var [integer] $list_ids Tableau des identifiants des commentaires à supprimer
     */
    function deleteCommentaires($list_ids, &$message)
    {
        $commentaire = new CommentaireRepository();
        $nb_user_delete = 0;
        $noError = True;
        foreach ($list_ids as $comment_id) {
            $noError = $commentaire->removeCommentaireById($comment_id, $message);
            if ($noError) {
                $nb_user_delete++;
            }
        }
        $message .= $nb_user_delete . "commentaire(s) supprimé(s).";
        return $noError;
    }


    /**
     * Mets à jour le commentaire en base de données
     * @param integer $id_comment identifiant du commenatire à mettre à jour
     * @param string $colonne_a_modifier attribut à modifier
     * @param string $element_a_mettre nouvelle valeur à assigner
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function updateCommentaire($id_comment, $colonne_a_modifier, $element_a_mettre, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("UPDATE " . self::TABLE_NAME .
                " SET $colonne_a_modifier = :element_a_mettre
                WHERE id_comment = $id_comment;");

            $stmt->bindValue(':element_a_mettre', $element_a_mettre);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "Le commenatire a correctement été modifié.";
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


}


?>