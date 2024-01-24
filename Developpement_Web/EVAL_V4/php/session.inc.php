<?php
session_start();
if (isset($_SESSION['login']) && isset($_SESSION['statut']) && isset($_SESSION['id_membre'])){
    $login_session = $_SESSION['login'];
    $statut = $_SESSION['statut'];
    $id_membre_session = $_SESSION['id_membre'];

}else{
    $statut = "";
    $id_membre_session = null;
    $login_session = "";
}
?>