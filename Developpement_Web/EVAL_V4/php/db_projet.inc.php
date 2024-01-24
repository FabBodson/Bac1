<?php

namespace CollectOrProjet;
require 'db_membre.inc.php';

use DB\DBLink;
use PDO;

setlocale(LC_TIME, 'fr_FR.utf8', 'fra');

/**
 * Classe Projet : projet créé sur collect'or
 */
class Projet
{
    private $id_projet;
    private $intitule;
    private $date_echeance;
    private $date_creation;
    private $description;
    private $montant;
    private $montant_actuel;
    private $montant_minimum;
    private $illustration_apercu;

    private $carte_VISA;
    private $nom_VISA;

    private $est_prolonge;
    private $est_valide;

    private $taux_participation;
    private $id_membre;
    private $id_type_part;
    private $id_categorie;


    public function __get($prop)
    {
        switch ($prop) {
            case "taux_participation":
                $this->$prop *= 100;
                break;

            default:
                $this->$prop;
        }
        return $this->$prop;

    }

    public function __set($prop, $val)
    {
        switch ($prop) {
            case "nom_VISA":
                $this->$prop = strtolower($val);
                break;

            case "intitule":
                $this->$prop = strtoupper($val);
                break;

            default:
                $this->$prop = $val;
        }
    }
}

/**
 * Classe ProjetRepository : gestionnaire du dépôt contenant les projets de collect'or
 */
class ProjetRepository
{
    const TABLE_NAME = 'web1_projet';


    /**
     * Enregistre le projet en base de données, l'intitule et la carte visa ne doivent pas exister en base de données
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var Projet $projet le projet à ajouter
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function storeProject($projet, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("INSERT INTO " . self::TABLE_NAME .
                " (intitule, date_echeance, date_creation, description, montant, montant_actuel, montant_minimum, illustration_apercu, carte_visa, nom_visa, 
                est_prolonge, est_valide, taux_participation, id_membre, id_type_part, id_categorie) 
                VALUES (:intitule, :date_echeance, :date_creation, :description, :montant, :montant_actuel, :montant_minimum, :illustration_apercu, :carte_visa, 
                :nom_visa, :est_prolonge, :est_valide, :taux_participation, :id_membre, :id_type_part, :id_categorie)");

            $stmt->bindValue(':intitule', $projet->intitule);
            $stmt->bindValue(':date_echeance', $projet->date_echeance);
            $stmt->bindValue(':date_creation', $projet->date_creation);
            $stmt->bindValue(':description', $projet->description);
            $stmt->bindValue(':montant', $projet->montant);
            $stmt->bindValue(':montant_actuel', $projet->montant_actuel);
            $stmt->bindValue(':montant_minimum', $projet->montant_minimum);
            $stmt->bindValue(':illustration_apercu', $projet->illustration_apercu);
            $stmt->bindValue(':carte_visa', $projet->carte_VISA);
            $stmt->bindValue(':nom_visa', $projet->nom_VISA);

            $stmt->bindValue(':est_prolonge', $projet->est_prolonge);
            $stmt->bindValue(':est_valide', $projet->est_valide);
            $stmt->bindValue(':taux_participation', $projet->taux_participation);
            $stmt->bindValue(':id_membre', $projet->id_membre);
            $stmt->bindValue(':id_type_part', $projet->id_type_part);
            $stmt->bindValue(':id_categorie', $projet->id_categorie);

            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "Le projet a correctement été créé.";
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
     * Vérifie si un projet existe dans la BD en vérifiant si l'intitule et la carte visa sont deja utilises
     * @var string $valeur valeur fournie du formulaire qui servira à tester l'existence du projet
     * @var string $colonne_table colonne du projet qui servira à tester l'existence du projet
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si adresse existante, false sinon
     */
    public function existsInDB($valeur, $colonne_table, &$message)
    {
        $result = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE $colonne_table = :valeur;");

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
     * Retourne le résultat d'une recherche
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets
     */
    public function getResearch($recherche, &$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " p 
            JOIN web1_membre m ON p.id_membre = m.id_membre 
            WHERE p.intitule LIKE '%$recherche%' 
            OR p.description LIKE '%$recherche%' 
            OR m.login LIKE '%$recherche%' 
            OR m.nom LIKE '%$recherche%' 
            OR m.prenom LIKE '%$recherche%';",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrProjet\Projet");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne tous les projets créés
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date d'echeance
     */
    public function getAllProjects(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " ORDER BY date_echeance ASC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrProjet\Projet");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne tous les projets créés
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date d'echeance
     */
    public function countProjects(&$message)
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
     * Retourne tous les projets créés
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date d'echeance
     */
    public function countFinancedProjects(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->prepare("SELECT COUNT(*) FROM " . self::TABLE_NAME . " WHERE taux_participation >= 1;");

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
     * Retourne tous les projets créés
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date d'echeance
     */
    public function countActualProjects(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->prepare("SELECT COUNT(*) FROM " . self::TABLE_NAME . " WHERE montant_actuel < montant;");

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
     * Retourne tous les projets créés
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date d'echeance
     */
    public function countTotal(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->prepare("SELECT SUM(montant_actuel) FROM " . self::TABLE_NAME . " WHERE taux_participation = 1;");

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
     * Retourne tous les projets créés
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date d'echeance
     */
    public function avgTaux(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->prepare("SELECT AVG(taux_participation) FROM " . self::TABLE_NAME . ";");

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
     * Retourne tous les projets créés
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date d'echeance
     */
    public function countCreateurProjects(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->prepare("SELECT COUNT(DISTINCT id_membre) FROM " . self::TABLE_NAME . ";");

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
     * Retourne tous les projets créés selon leur date de création
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date de création
     */
    public function getAllLastProjects(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " ORDER BY date_creation DESC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrProjet\Projet");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne tous les projets créés selon leur date de création
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date de création
     */
    public function getAllAlmostFinishedProjects(&$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " WHERE taux_participation BETWEEN 0.9 AND 0.99
             ORDER BY taux_participation DESC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrProjet\Projet");

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne tous les projets créés selon une date donnée
     *
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return array|false|\PDOStatement [Projets] liste des projets triés selon la date donnée
     */
    public function getAllProjectsFromYear($annee, &$message)
    {
        $result = array();
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            //version "objet", l'appel au constructeur de la classe peut être forcé avant d'affecter les propriétés
            // en spécifiant les styles PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE.
            $result = $bdd->query("SELECT * FROM " . self::TABLE_NAME . " WHERE date_echeance = :annee ORDER BY date_creation DESC;",
                PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, "CollectOrProjet\Projet");

            $result->bindValue(':annee', $annee);

        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result;
    }


    /**
     * Retourne le projet correspondant à un identifiant
     * @var integer $id_projet identifiant d'un projet
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return Projet|null le projet associé à l'identifiant
     */
    public function getProjectById($id_projet, &$message)
    {
        $result = false;
        $bdd = null;

        try {

            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("SELECT * FROM " . self::TABLE_NAME . " WHERE id_projet = :id_projet");
            $stmt->bindValue(':id_projet', $id_projet);

            if ($stmt->execute()) {
                $result = $stmt->fetchObject("CollectOrProjet\Projet");

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
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $id_projet identifiant correspondant à un type de participation
     * @return array|false|\PDOStatement liste du libelle et de sa description d'un type de participation
     */
    public function getLibelleTypePartById($id_projet, &$message)
    {
        $result_string = array();
        $libelle = null;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $libelle = $bdd->prepare("SELECT tp.libelle FROM " . self::TABLE_NAME . " p
             JOIN web1_type_participation tp on p.id_type_part = tp.id_type_part
             WHERE p.id_projet = :id_projet;");
            $libelle->bindValue(':id_projet', $id_projet);

            if ($libelle->execute()) {
                $result_string = $libelle->fetch();
            }


        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result_string['libelle'];
    }


    /**
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $id_projet identifiant correspondant à un type de participation
     * @return array|false|\PDOStatement liste de la description d'un type de participation
     */
    public function getDescriptionTypePartById($id_projet, &$message)
    {
        $result_string = array();
        $description = null;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $description = $bdd->prepare("SELECT tp.description FROM " . self::TABLE_NAME . " p
             JOIN web1_type_participation tp on p.id_type_part = tp.id_type_part
             WHERE p.id_projet = :id_projet;");
            $description->bindValue(':id_projet', $id_projet);

            if ($description->execute()) {
                $result_string = $description->fetch();
            }


        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result_string['description'];
    }


    /**
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $id_membre identifiant correspondant au porteur de projet
     * @return array|false|\PDOStatement liste du login du porteur de projet
     */
    public function getCreateurProjet($id_membre, &$message)
    {
        $result_string = array();
        $login = null;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $login = $bdd->prepare("SELECT m.login FROM " . self::TABLE_NAME . " p
             JOIN web1_membre m on p.id_membre = m.id_membre
             WHERE p.id_membre = :id_membre;");
            $login->bindValue(':id_membre', $id_membre);

            if ($login->execute()) {
                $result_string = $login->fetch();
            }


        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result_string['login'];
    }


    /**
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var string $id_categorie identifiant correspondant a une categorie
     * @return array|false|\PDOStatement liste du login du porteur de projet
     */
    public function getCategorieProjet($id_categorie, &$message)
    {
        $result_string = array();
        $categorie = null;
        $bdd = null;
        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $categorie = $bdd->prepare("SELECT c.categorie FROM " . self::TABLE_NAME . " p
             JOIN web1_categorie c on p.id_categorie = c.id_categorie
             WHERE p.id_categorie = :id_categorie;");
            $categorie->bindValue(':id_categorie', $id_categorie);

            if ($categorie->execute()) {
                $result_string = $categorie->fetch();
            }


        } catch (Exception $e) {
            $message .= $e->getMessage() . '<br>';
        }
        DBLink::disconnect($bdd);
        return $result_string['categorie'];
    }


    /**
     * Supprime un projet sur base de son identifiant
     * @return boolean true si opération réalisée sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var integer $id_projet identifiant du projet
     */
    public function removeProjectById($id_projet, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);
            $stmt = $bdd->prepare("DELETE FROM " . self::TABLE_NAME . " WHERE id_projet = :id_projet;");
            $stmt->bindValue(':id_projet', $id_projet);

            if ($stmt->execute()) {
                $message .= "Projet correctement supprimé.";
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
     * Supprime un ensemble de projets sur base de leur identifiant
     * @return boolean true si suppressions effectuées sans erreur, false sinon
     * @var string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @var [integer] $list_ids Tableau des identifiants des projets à supprimer
     */
    function deleteProjets($list_ids, &$message)
    {
        $projetRepository = new ProjetRepository();
        $nb_user_delete = 0;
        $noError = True;
        foreach ($list_ids as $projet_id) {
            $noError = $projetRepository->removeProjectById($projet_id, $message);
            if ($noError) {
                $nb_user_delete++;
            }
        }
        $message .= $nb_user_delete . "membre(s) supprimé(s).";
        return $noError;
    }


    /**
     * Mets à jour le projet en base de données
     * @param string $id_projet identifiant du commenatire à mettre à jour
     * @param string $colonne_a_modifier attribut à modifier
     * @param string $element_a_mettre nouvelle valeur à assigner
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function updateProjet($id_projet, $colonne_a_modifier, $element_a_mettre, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("UPDATE " . self::TABLE_NAME .
                " SET $colonne_a_modifier = $element_a_mettre 
                 WHERE id_projet = $id_projet;");


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "Le projet a correctement été modifié.";
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
     * Mets à jour le projet en base de données
     * @param string $id_projet identifiant du commenatire à mettre à jour
     * @param string $nouvelle_description nouvelle description à assigner
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function updateDescriptionProjet($id_projet, $nouvelle_description, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("UPDATE " . self::TABLE_NAME . " SET description = '$nouvelle_description' WHERE id_projet = $id_projet;");

            if ($stmt->execute()) {
                $message .= "La description du projet a correctement été modifiée.";
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
     * Mets à jour le projet en base de données
     * @param string $id_projet identifiant du commenatire à mettre à jour
     * @param string $nouvelle_photo nouvelle photo à assigner
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function updatePhotoProjet($id_projet, $nouvelle_photo, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("UPDATE " . self::TABLE_NAME . " SET illustration_apercu = '$nouvelle_photo' 
            WHERE id_projet = $id_projet;");

            if ($stmt->execute()) {
                $message .= "La photo du projet a correctement été modifiée.<br>";
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
     * Mets à jour le commentaire en base de données
     * @param string $id_projet identifiant du commenatire à mettre à jour
     * @param $nouvelle_date string nouvelle date d'échéance choisie
     * @param string $message ensemble des messages à retourner à l'utilisateur, séparés par un saut de ligne
     * @return boolean true si opération réalisée sans erreur, false sinon
     */
    public function prolongerProjet($id_projet, $nouvelle_date, &$message)
    {
        $noError = false;
        $bdd = null;

        try {
            $bdd = DBLink::connect2db(MYDB, $message);

            $stmt = $bdd->prepare("UPDATE " . self::TABLE_NAME .
                " SET date_echeance = :nouvelle_date
                WHERE id_projet = $id_projet;");

            $stmt->bindValue(':nouvelle_date', $nouvelle_date);


            if ($stmt->execute() && $stmt->rowCount() == 1) {
                $message .= "La date d'échéance a correctement été modifiée.";
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