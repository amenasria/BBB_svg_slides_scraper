<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Titre de la page</title>
<!--    <link rel="stylesheet" href="style.css">-->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $('#run_script_form').on('submit', function(event) {
                event.preventDefault();
                $.ajax({
                    type: 'post',
                    url: 'run_script.php',
                    data: $(this).serialize(),
                    success: function (data) {
                        document.getElementById("log_python").textContent= "Téléchargement prêt";
                        var download_btn = document.getElementById("download_button");
                        download_btn.href= String(data);
                        download_btn.style.display = "inline-block";
                    }

                });
            })
        })

    </script>
</head>
<body>
    <form method="post" id="run_script_form">
        <label> Url du bbb:
            <input type="text" id="url_bbb_svg" name="url_bbb_svg">
        </label>
        <input type="submit" value="Générer le pdf">
    </form>
    <p id="log_python"></p>
    <a href="" style="display: none;" id="download_button" download>Télécharger le fichier</a>

</body>
</html>


