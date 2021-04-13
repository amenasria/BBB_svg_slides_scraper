# BBBScrapy : Telechargez les slides d'un cours BBB à l'aide d'une url seulement ! 🤓

Fonctionnalité :

Entrez l'url de l'image que le prof diffuse sur BBB, BBBScrapy vous reconstruit le pdf sur votre ordinateur

## Installation

Tout d'abord **clonez le répo**, puis rendez-vous dans le dossier du projet et utilisez pip pour installer les dépendances :

```bash
pip install -r requirements.txt
```

## Lancement du script

**Rendez vous dans le fichier main.py et remplacez le contenu de *url_slides_bbb***:

En général en utilisant l'inspecteur d'élément vous trouvez une url du type:

```bash
https://bbb1.centrale-marseille.fr/bigbluebutton/presentation/plein_de_chiffres_chelous/svg/6
```

Dans ce cas là remplacez le contenu de *url_slides_bbb* (ligne 8) par cette url sans le numéro à la fin, i.e ici:

```bash
https://bbb1.centrale-marseille.fr/bigbluebutton/presentation/plein_de_chiffres_chelous/svg/
```

La ligne deviendra donc

```bash
url_slides_bbb = "https://bbb1.centrale-marseille.fr/bigbluebutton/presentation/plein_de_chiffres_chelous/svg/"
```

Enfin **récupérez le pdf final appelé result.pdf** que vous pourrez trouver dans le dernier dossier de la forme temp_*chiffres* créé.
