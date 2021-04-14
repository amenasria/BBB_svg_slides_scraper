<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Scrapy</title>
    <link rel="icon" href="logo.png">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css">
    <script
            src="https://code.jquery.com/jquery-3.1.1.min.js"
            integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
            crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js"></script>
    <script>
        $(document).ready(function() {
            $('.ui.accordion').accordion();


            $('#run_script_form').on('submit', function(event) {
                event.preventDefault();
                document.getElementById("generation_button").classList.add("loading");
                $.ajax({
                    type: 'post',
                    url: 'run_script.php',
                    data: $(this).serialize(),
                    success: function (data) {
                        // document.getElementById("log_python").textContent= "Téléchargement prêt";
                        var download_btn = document.getElementById("download_button");
                        download_btn.href= String(data);
                        download_btn.style.display = "inline-block";
                        document.getElementById("generation_button").classList.remove("loading");
                    }

                });
            })
        })

    </script>
</head>
<body>
<!--    <form method="post" id="run_script_form">-->
<!--        <label> Url du bbb:-->
<!--            <input type="text" id="url_bbb_svg" name="url_bbb_svg">-->
<!--        </label>-->
<!--        <input type="submit" value="Générer le pdf">-->
<!--    </form>-->
<!--    <p id="log_python"></p>-->
<!--    <a href="" style="display: none;" id="download_button" download>Télécharger le fichier</a>-->

    <div class="ui container" style="margin-top: 3em;">
        <h1 style="font-size: 3em; text-align: center; font-weight: normal;">BBBScrapy</h1>
        <div class="ui hidden divider" style="margin: 4em 0em 4em"></div>
        <form method="post" id="run_script_form">
            <div class="ui fluid action input">
                <input type="text" id="url_bbb_svg" name="url_bbb_svg" placeholder="https://bbb1.centrale-marseille.fr/bigbluebutton/presentation/plein_de_chiffres_chelous/svg/">
                <button class="ui teal right labeled icon button" id="generation_button">
                    <i class="bolt icon"></i>
                    Générer le pdf
                </button>
            </div>
        </form>
        <div class="ui hidden divider"></div>
        <div class="ui container" style="display: flex; align-items: center; justify-content: center; min-height: 8em;">
            <a href="" style="display: none;" id="download_button" download class="ui secondary button big">
                <i class="bug icon"></i>
                Télécharger le pdf
            </a>
        </div>
        <h2 class="ui dividing header">FAQ</h2>
        <h4>Quelle url dois-je saisir ?</h4>
        <p>Vous devez saisir l'url qui fait référence à un svg lors d'une présentation BBB.</p>
        <h4>Où puis-je la trouver ?</h4>
        <p>Lorsque vous êtes spectateur d'une présentation BBB, clic droit > Inspecter l'élement > Selectionner l'icone <i class="mouse pointer icon"></i> en haut à gauche de la console qui vient de s'ouvrir.<br/> Cliquez sur l'image qui est en train d'être partagée, puis dans la console double-cliquez sur le lien correspondant pour le copier. Enfin collez là et effacez le numéro de la slide à la fin de l'url pour que l'url finisse en <b>.../svg/</b> .</p>
        <h4>Que puis-je faire avec le pdf que je télécharge ensuite ?</h4>
        <p>
            <b><u>Le garder pour vous</u></b>. En tant qu'élève de Centrale qui suivez les cours, vous avez accès aux documents que partagent les professeurs. Habituellement vous les enregistrez sous la forme de captures d'écran ce qui n'est franchement pas pratique.
            <br/><br/>Cet outil permet <b>si vous y avez accès</b> de télécharger ces svg en pdf plutôt que de faire des captures d'écran, il est bien entendu interdit de diffuser ces documents car cela irait à l'encontre des droits d'auteur.
            <br><br>Vous êtes le seul responsable de ce que vous faites de ces documents et les mêmes rêgles s'appliquent que pour lorsque vous partagez les captures d'écrans à vos camarades.
        </p>
        <h4>Est-ce que tu conserves des données sur les gens qui utilisent l'outil ?</h4>
        <p>Non, il n'y a aucune mise en mémoire autre que celle du fichier pdf qui est supprimé quelques secondes après que vous l'ayez téléchargé.</p>
        <h4>Quelle techno derrière cet outil ?</h4>
        <p>Python pour scraper les svg puis les combiner en un pdf. PHP en back avec un front en SemanticUI pour cette interface minimaliste.</p>
        <h4>Comment te remercier ? Comment faire pareil ?</h4>
        <p>Rejoignez le GInfo (mdrrr c'est la best asso no joke ahaha 😛)</p>
        <div class="ui hidden divider" style="margin: 8em 0em 8em"></div>
    </div>
</body>
</html>


