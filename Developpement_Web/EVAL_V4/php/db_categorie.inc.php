<?php

namespace CollectOrCategorie;
require 'db_participation.inc.php';

use DB\DBLink;
use PDO;

setlocale(LC_TIME, 'fr_FR.utf8', 'fra');

/**
 * Classe Categorie : categorie sur collect'or
 */
class Categorie
{
    private $id_categorie;
    private $categorie;



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
 * Classe CategorieRepository : gestionnaire du dépôt contenant les categories de collect'or
 */
class CategorieRepository
{
    const TABLE_NAME = 'web1_categorie';


    /**
     * Enregistre le categorie en base de données
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var Categorie $categorie la categorie à ajouter
     */
    public function storeCategorie($categorie, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("INSERT INTO " . self::TABLE_NAME . " (categorie) 
            VALUES (:categorie)");

            $stmt->bindValue(':categorie', $categorie->categorie);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "Catégorie ajoutée !";
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
     * Vérifie si une categorie existe déjà en BD
     * @return boolean true si adresse existante, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $categorie catégorie à vérifier
     * @var string $colonne_table colonne de la table à vérifier
     */
    public function existsInDB($categorie, $colonne, &$message)
    {
        $result = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE $colonne = :categorie");
            $stmt->bindValue(':categorie', $categorie);

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
     * Retourne toutes les catégories existantes
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Categorie] liste des categories triées selon l'ordre alphabétique
     */
    public function getAllCategories(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " ORDER BY categorie ASC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrCategorie\Categorie");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne la categorie correspondant à un identifiant
     * @var integer $id_categorie identifiant d'une categorie
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return Categorie|null la categorie associé à l'identifiant
     */
    public function getCategorieById($id_categorie, &$message)
    {
        $result = false;
        $bdd = null;

        try {

            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT categorie FROM " . self::TABLE_NAME . " WHERE id_categorie = :id_categorie");
            $stmt->bindValue(':id_categorie', $id_categorie);

            if ($stmt->execute()) {
                $result = $stmt->fetchObject("CollectOrCategorie\Categorie");

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
     * Supprime un categorie sur base de son identifiant
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var integer $id_categorie identifiant de la categorie
     */
    public function removeCategorieById($id_categorie, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("DELETE FROM " . self::TABLE_NAME . " WHERE id_categorie = :id_categorie;");
            $stmt->bindValue(':id_categorie', $id_categorie);

            if ($stmt->execute()) {
                $message .= "Catégorie correctement supprimée.";
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
     * Supprime un ensemble de catégories sur base de leur identifiant
     * @return boolean true si suppressions effectuées sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var [integer] $list_ids Tableau des identifiants des catégories à supprimer
     */
    function deleteCategories($list_ids, &$message)
    {
        $categorie = new CategorieRepository();
        $nb_user_delete = 0;
        $noError = True;
        foreach ($list_ids as $categorie_id) {
            $noError = $categorie->removeCategorieById($categorie_id, $message);
            if ($noError) {
                $nb_user_delete++;
            }
        }
        $message .= " " . $nb_user_delete . " catégorie(s) supprimé(s).";
        return $noError;
    }


    /**
     * Mets à jour la categorie en base de données
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $id_ancienne_categorie la categorie à modifier
     * @var string $nom_nouvelle_categorie le nouveau nom de la catégorie
     */
    public function updateCategorie($id_ancienne_categorie, $nom_nouvelle_categorie, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("UPDATE " . self::TABLE_NAME .
                " SET categorie = :nom_nouvelle_categorie
                 WHERE id_categorie = :id_ancienne_categorie;");

            $stmt->bindValue(':nom_nouvelle_categorie', $nom_nouvelle_categorie);
            $stmt->bindValue(':id_ancienne_categorie', $id_ancienne_categorie);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "La categorie a correctement été modifiée.";
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