<?php
$titreOnglet = "Statistiques"; /* Onglet */
$titreSite = "Collect'Or"; /* h2 */
$titrePage = "Statistiques"; /* h1 */
$filAriane = "<a href=\"index.php\">Accueil</a> &gt; Statistiques";

require 'php/session.inc.php';

if ($statut == 'admin' || $statut == 'porteurProjet' || $statut == 'membre')
    include('inc/header.inc.php');
else
    include('inc/header_Anonyme.inc.php');

use CollectOrMembre\MembreRepository as MembreRepository;
use CollectOrProjet\ProjetRepository as ProjetRepository;
use CollectOrParticipation\ParticipationRepository as ParticipationRepository;
use CollectOrCommentaire\CommentaireRepository as CommentaireRepository;

$message = "";

$membreRepository = new MembreRepository();
$projetRepository = new ProjetRepository();
$participationRepository = new ParticipationRepository();
$commentaireRepository = new CommentaireRepository();


$nb_membres = $membreRepository->countMembres($message)[0];
$nb_projets = $projetRepository->countProjects($message)[0];

$nb_projets_finances = $projetRepository->countFinancedProjects($message)[0];

$total_recolte = $projetRepository->countTotal($message)[0];
if($total_recolte == null)
    $total_recolte = 0;

$taux_moyen = $projetRepository->avgTaux($message)[0]*100;

$projets_en_cours = $projetRepository->countActualProjects($message)[0];

$nb_porteurs_projets = $projetRepository->countCreateurProjects($message)[0];

$nb_participations = $participationRepository->countParticipations($message)[0];

$nb_commentaires = $commentaireRepository->gcountCommentaires($message)[0];

?>
    <!-- Chiffres globaux -->
    <section>
        <h2 class="titreSectionStat">Quelques chiffres</h2>

        <p class="statImportantes"><?php echo $nb_membres; ?><br>membres</p>

        <p class="statImportantes"><?php echo $nb_projets_finances; ?><br>projets financés</p>

        <p class="statImportantes"><?php echo $total_recolte; ?> €<br>collectés</p>

        <p class="statImportantes"><?php echo $nb_projets; ?><br>projets présentés</p>

        <p class="statImportantes"><?php echo $taux_moyen; ?>%<br>de participations aux projets</p>

    </section>


    <!-- Graphe en tarte -->
    <section class="graph">
        <h2 class="titreSectionStat">Nos membres</h2>
        <p>Pour <?php echo $nb_membres; ?> membres, voici leur implication:</p>
        <span class="json">
        {"type":"pie"
        ,"width":400
        ,"height":400
        ,"datasets":
            [{
                "label": "membres",
                "data": [<?php echo $nb_porteurs_projets; ?>, <?php echo $nb_participations; ?>, <?php echo $nb_commentaires; ?>],
                "color":[[0,200,0,0.6],[200,0,0,0.6],[0,0,200,0.6]],
                "borderColor":[[36,43,42]],
                "hoverColor":[[0,200,0],[200,0,0],[73,92,255]]
            }
        ],
        "dataLabel": ["Porteurs de projet(s)","Contributions","Commentaires"]
        }
    </span>
        <div class="graph"></div>
    </section>

    <!-- Graphe en barres -->
    <section class="graph">
        <h2 class="titreSectionStat">Les projets c'est : </h2>
        <span class="json">
        {"type":"bar"
        ,"width":400
        ,"height":400
        ,"datasets":
            [{
                "label": "Les projets",
                "data": [<?php echo $nb_projets; ?>, <?php echo $projets_en_cours; ?>, <?php echo $nb_projets_finances; ?>],
                "color":[[0,200,0,0.2],[200,0,0,0.2],[73,92,255,0.2]],
                "borderColor":[[0,200,0],[200,0,0],[73,92,255]],
                "hoverColor":[[0,200,0],[200,0,0],[73,92,255]]
            }],
        "dataLabel": ["Projets présentés","Projets en cours","Projets financés"]
        }
    </span>
        <div class="graph"></div>
    </section>



<?php
include('inc/footer.inc.php');
?>