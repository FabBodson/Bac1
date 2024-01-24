<section>
    <p class="messagePrincipal"><?php echo $messagePrincipal; ?></p>


    <h2><?php echo $messageSection; ?></h2>


    <?php
    foreach ($listeProjets as $projet) {
        include ('inc/apercu_Projet.inc.php');
         } ?>


</section>