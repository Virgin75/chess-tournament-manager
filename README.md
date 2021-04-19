# Description

Chess tournament manager est un script Python permettant de créer et un gérer un tournoi d'échecs. Ajoutez vos joueurs, les matches sont générés automatiquement. Vous n'avez plus qu'à rentrer les résultats et suivre le classement.

# Installation

1. Téléchargez l'ensemble du code pour l'avoir dans votre environnement local.
2. Depuis un terminal, allez dans le répertoire téléchargé puis lancez un nouvel environnement virtuel:

```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

# Utilisation

Éxécutez le programme en tapant la commande suivante :

```bash
python3 main.py
```

![Menu principal](https://i.ibb.co/r7w0B3H/chess1.png)

Voici une courte description des fonctionnalités de chacunes des fonctionnalités du menu principal :

- **Create a tournament** : Permet de créer un tournoi en précisant les informations le concernant (nom, lieu, date de début, date de fin, description, et type de contrôle du temps)
- **Add a new player** : Permet d'ajouter un nouveau joueur au tournoi venant d'être créé. Les informations suivantes sont requises : prénom, nom, date de naissance, sexe et classement.
- **Edit a player ranking** : Permet de modifier le classement (défini lors de la création du joueur) de l'un des joueurs ajoutés au tournoi en cours.
- **Start the round** : Permet de lancer un round, jusqu'à ce qu'il n'y ait plus de rounds à jouer. Le nom du round sera demandé avant de le lancer. Une fois lancé, les paires de matchs sont générés à l'aide du système suisse.
  L'utilisateur devra ensuite indiqué le vainqueur de chaque match. Les points sont attribués de la manière suivante : **1 point** pour le vainqueur, **0 point** pour le perdant, et **0.5 point** en cas de match nul.
- **Generate reports** : Permet de générer divers rapport sur le.s tournoi.s joué.s tels que : liste des joueurs, classement général, liste des matchs, liste des rounds...
- **Switch database** : Permet de changer de base de données en important une nouvelle. Le nom de la base de données en cours d'utilisation est précisée en fin de ligne.
  La base de données doit être un fichier au format `.json`. Celle-ci est générée via TinyDB.
  À noter, chaque action effectuée (ajout d'un joueur, lancement d'un round, ajout des résultats d'un match...) génére une sauvegarde automatique de la base de données.
  Afin d'utiliser une autre base de données, il faut à tout prix que le fichier `.json` soit placé dans le même répertoire que l'actuelle base de données.

## Comment générer un nouveau rapport flake8-html ?

```bash
flake8 --format=html --htmldir=flake-report
```
