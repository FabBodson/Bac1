<?php

namespace CollectOrParticipation;
require 'db_news.inc.php';

use DB\DBLink;
use PDO;

setlocale(LC_TIME, 'fr_FR.utf8', 'fra');

/**
 * Classe Participation : participation à un projet
 */
class Participation
{
    private $id_participation;
    private $date_participation;
    private $montant;
    private $id_membre;
    private $id_projet;


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
 * Classe ParticipationRepository : gestionnaire du dépôt contenant les participations à un projet
 */
class ParticipationRepository
{
    const TABLE_NAME = 'web1_participation';


    /**
     * Enregistre le participation en base de données
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var Participation $participation la participation à ajouter
     */
    public function storeParticipation($participation, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("INSERT INTO " . self::TABLE_NAME . " 
            (date_participation, montant, id_membre, id_projet) 
            VALUES (:date_participation, :montant, :id_membre, :id_projet)");

            $stmt->bindValue(':date_participation', $participation->date_participation);
            $stmt->bindValue(':montant', $participation->montant);
            $stmt->bindValue(':id_membre', $participation->id_membre);
            $stmt->bindValue(':id_projet', $participation->id_projet);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "Participation enregistrée !";
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
    public function existsInDB($id_projet, $id_membre, &$message)
    {
        $result = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " 
            WHERE id_projet = :id_projet AND id_membre = :id_membre;");
            $stmt->bindValue(':id_projet', $id_projet);
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
     * Retourne toutes les participations existantes
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return [Participation] liste des participations triées selon leurs date de participation
     */
    public function getAllParticipations(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " ORDER BY date_participation ASC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrParticipation\Participation");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }



    /**
     * Retourne toutes les participations existantes
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return [Participation] liste des participations triées selon leurs date de participation
     */
    public function countParticipations(&$message)
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
     * Retourne toutes les participations existantes
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return [Participation] liste des participations triées selon leurs date de participation du plsu recent au plus ancien
     */
    public function getAllLastParticipations(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " ORDER BY date_participation DESC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrParticipation\Participation");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }







    /**
     * Retourne la participation correspondante à un identifiant
     * @var integer $id identifiant d'une participation
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return Participation|null la participation associée à l'identifiant
     */
    public function getParticipationById($id_participation, &$message)
    {
        $result = false;
        $bdd = null;

        try {

            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE id_participation = :id_participation");
            $stmt->bindValue(':id_participation', $id_participation);

            if ($stmt->execute()) {
                $result = $stmt->fetchObject("CollectOrParticipation\Participation");

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
     * Retourne toutes les participations existantes
     *
     * @param $id_projet
     * @param $id_membre
     * @param $message
     * @return bool|mixed [Participation] liste des participations triées selon leurs date de participation
     */
    public function getParticipationByIdProjetIdMembre($id_projet, $id_membre, &$message)
    {
        $result = false;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $stmt = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " 
            WHERE id_projet = $id_projet AND id_membre = $id_membre ;",
            PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrParticipation\Participation");


            if ($stmt->execute()) {
                $result = $stmt->fetchObject("CollectOrParticipation\Participation");

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
     * Supprime une participation sur base de son identifiant
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var integer $id_particpation identifiant de la participation
     */
    public function removeParticipationById($id_participation, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("DELETE FROM " . self::TABLE_NAME . " WHERE id_participation = $id_participation;");

            if ($stmt->execute()) {
                $message .= "Participation correctement supprimée.";
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
     * Supprime un ensemble de participations sur base de leur identifiant
     * @return boolean true si suppressions effectuées sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var [integer] $list_ids Tableau des identifiants des participations à supprimer
     */
    function deleteParticipations($list_ids, &$message)
    {
        $participation = new ParticipationRepository();
        $nb_user_delete = 0;
        $noError = True;
        foreach ($list_ids as $participation_id) {
            $noError = $participation->removeParticipationById($participation_id, $message);
            if ($noError) {
                $nb_user_delete++;
            }
        }
        $message .= $nb_user_delete . "participation(s) supprimée(s).";
        return $noError;
    }


    /**
     * Mets à jour le montant actuel pour un projet
     * @param string $id_projet identifiant du projet
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function updateMontantActuel($id_projet, &$message)
    {
        $montant = null;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $montant = $bdd->prepare("SELECT SUM(montant) FROM " . self::TABLE_NAME . " 
             GROUP BY id_projet 
             HAVING id_projet = :id_projet;");

            $montant->bindValue(':id_projet', $id_projet);

            if ($montant->execute()) {
                $montant = $montant->fetch();
            }


        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $montant;
    }


    /**
     * Compte le nombre de participations d'un membre
     * @param string $id_membre identifiant d'un membre
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function countNombrePart($id_membre, &$message)
    {
        $nb_part = null;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $nb_part = $bdd->prepare("SELECT count(*) FROM " . self::TABLE_NAME . " 
             GROUP BY id_membre 
             HAVING id_membre = :id_membre;");

            $nb_part->bindValue(':id_membre', $id_membre);

            if ($nb_part->execute()) {
                $nb_part = $nb_part->fetch();
            }


        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $nb_part;
    }


    /**
     * Compte le montant total promis par un membre
     * @param string $id_membre identifiant d'un membre
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return integer somme totale promise par un membre
     */
    public function countMontantPromis($id_membre, &$message)
    {
        $nb_part = null;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $nb_part = $bdd->prepare("SELECT SUM(montant) FROM " . self::TABLE_NAME . " 
             GROUP BY id_membre 
             HAVING id_membre = :id_membre;");

            $nb_part->bindValue(':id_membre', $id_membre);

            if ($nb_part->execute()) {
                $nb_part = $nb_part->fetch();
            }


        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $nb_part;
    }


    /**
     * Compte le montant total promis par un membre
     * @param string $id_membre identifiant d'un membre
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return integer somme du montant total preleve à un membre
     */
    public function countMontantPreleve($id_membre, &$message)
    {
        $preleve = null;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $preleve = $bdd->prepare("SELECT SUM(pa.montant) FROM " . self::TABLE_NAME . " pa 
            JOIN web1_projet p ON pa.id_projet = p.id_projet 
            WHERE p.est_valide = 1 
             GROUP BY pa.id_membre 
             HAVING pa.id_membre = :id_membre;");

            $preleve->bindValue(':id_membre', $id_membre);

            if ($preleve->execute()) {
                $preleve = $preleve->fetch();
            }


        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $preleve;
    }


}


?>