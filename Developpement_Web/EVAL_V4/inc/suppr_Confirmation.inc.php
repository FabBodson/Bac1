<form class="confirmerSuppression" style="text-align: center;" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
    <fieldset>
        <p>Etes-vous sûr de vouloir le supprimer ?</p>
        <input class="boutonModifProfil" type="submit" name="confirmer" value="Confirmer">
        <input class="boutonModifProfil" type="submit" name="annuler" value="Annuler">
    </fieldset>
</form>