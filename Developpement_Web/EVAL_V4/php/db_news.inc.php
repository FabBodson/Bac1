<?php

namespace CollectOrNews;
require 'db_commentaire.inc.php';

use DB\DBLink;
use PDO;

setlocale(LC_TIME, 'fr_FR.utf8', 'fra');

/**
 * Classe News : news d'un projet
 */
class News
{
    private $id_news;
    private $intitule;
    private $description;
    private $date_publication;
    private $id_projet;



    public function __get($prop)
    {
        return $this->$prop;
    }

    public function __set($prop, $val)
    {
        switch ($prop){
            case "intitule":
                $this->$prop = ucfirst($val);
                break;
            default:
                $this->$prop = $val;
        }

    }
}

/**
 * Classe NewsRepository : gestionnaire du dépôt contenant les news d'un projet'
 */
class NewsRepository
{
    const TABLE_NAME = 'web1_news';


    /**
     * Enregistre la news en base de données
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var News $news la news à ajouter
     */
    public function storeNews($news, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("INSERT INTO " . self::TABLE_NAME . " (intitule, description, date_publication, id_projet) 
            VALUES (:intitule, :description, :date_publication, :id_projet)");

            $stmt->bindValue(':intitule', $news->intitule);
            $stmt->bindValue(':description', $news->description);
            $stmt->bindValue(':date_publication', $news->date_publication);
            $stmt->bindValue(':id_projet', $news->id_projet);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "News postée !";
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
     * Vérifie si un intitule de news et une description existent déjà en BD
     * @return boolean true si l'intitule ou la description existante, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $intitule intitule à vérifier
     * @var string $description description à vérifier
     * @var string $id_projet id_projet à vérifier
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
     * Retourne toutes les news postées
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return [News] liste des news triés selon la date de mise en ligne
     */
    public function getAllNews(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " ORDER BY date_publication ASC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrCommentaire\Commentaire");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne la news correspondant à un identifiant
     * @var integer $id_news identifiant d'une news
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return News|null la news associé à l'identifiant
     */
    public function getNewsById($id_news, &$message)
    {
        $result = false;
        $bdd = null;

        try {

            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE id_news = :id_news");
            $stmt->bindValue(':id_news', $id_news);

            if ($stmt->execute()) {
                $result = $stmt->fetchObject("CollectOrNews\News");

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
     * Supprime une news sur base de son identifiant
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var integer $id_news identifiant d'une news
     */
    public function removeNewsById($id_news, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("DELETE FROM " . self::TABLE_NAME . " WHERE id_news = :id_news;");
            $stmt->bindValue(':id_news', $id_news);

            if ($stmt->execute()) {
                $message .= "News correctement supprimée.";
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
     * Supprime un ensemble de news sur base de leur identifiant
     * @return boolean true si suppressions effectuées sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var [integer] $list_ids Tableau des identifiants des news à supprimer
     */
    function deleteNews($list_ids, &$message)
    {
        $news = new NewsRepository();
        $nb_user_delete = 0;
        $noError = True;
        foreach ($list_ids as $news_id) {
            $noError = $news->removeNewsById($news_id, $message);
            if ($noError) {
                $nb_user_delete++;
            }
        }
        $message .= $nb_user_delete . "News supprimée(s).";
        return $noError;
    }


    /**
     * Mets à jour la news en base de données
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $valeur la news à modifier
     * @var string $colonne_table la colonne où modifier
     */
    public function updateNews($valeur, $colonne_table, $id_news, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("UPDATE " . self::TABLE_NAME .
                " SET $colonne_table = :valeur
                 WHERE id_news = :id_news;");

            $stmt->bindValue(':valeur', $valeur);
            $stmt->bindValue(':id_news', $id_news);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "La news a correctement été modifiée.";
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