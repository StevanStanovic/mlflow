MLFLOW TRACKING POUR UN ALGORITHME SUPERVISÉ
============================================


Objectifs
---------

* **Compréhension de MLFlow Tracking & Model**
* **Implémentation en local et sur Datavricks de MLFlow Tracking**
* **Création d'un MLFlow Model (configuration par défaut)**
* **Utilisation de Tracking UI**

Présentation des composants MLFlow Tracking & Model
---------------------------------------------------

Le composant MLFlow Tracking est à la fois une API et une interface utilisateur. Son but est d'enregistrer des paramètres, métriques, fichiers et informations (rajouter des annotations aussi). Cette enregistrement se réalise pendant le lancement d'une expérience de code Machine Learning. Ce lancement est ensuite stocké dans un répertoire dont la référence est précisé. Le répertoire en question stocke tous nos lancements dans des dossiers. Ces dossiers sont composés de toutes les informations de nos lancements (paramètres, métriques, fichiers ...)  mais également d'un MLFlow Model. De plus, grâce à l'interface utilisateur de MLFlow Tracking, nous pouvons visualiser ces informations et comparer leurs résultats entre eux. L'interface utilisateur s'appelle Tracking UI.

Le composant MLFlow Model est un format standard pour packager des modèles ML. Il permet de déployer un modèle sur diverses plateformes et/ou services numériques. Plus précisément, il définit une convention qui permet de sauvegarder un modèle dans différentes "*flavors*". La génération d'un MlFlow Model est réalisé de deux manières, soit :
* il est définit par un MLFlow Project : la configuration de l'environnement (versions de Python, des bibliothéques, des installations ...) est décrite dans ce dernier (nous verrons cela dans l'exemple 3)
* il n'est pas définit par un MLFlow Project : la configuration de l'environnement est la même que l'environnement du lancement de l'expérience

Visualisation des expériences et accès au Tracking UI
------------------------------

La visualisation des résultats se réalise sur l'interface utilisateur de MLFlow : Tracking UI. On peut visualiser des paramètres, des métriques et des fichiers ou encore comparer ces derniers grâce à celui-ci. Le but principal de cet outil est de nous aider à choisir un modèle performant. Par exemple, si on souhaite que notre modèle soit un classifieur SVM, on peut réaliser plusieurs lancements d'expérience avec différents paramètres afin d'optimiser une métrique (accuracy, sensibilité, spécificité ...) et comparer cette métrique par rapport aux paramètres d'entrée sur l'interface.

![Image of the comparison example](Images/Comparing_metric_with_parameter_SVM.PNG)

**Accès au Tracking UI en local**

0. Lancer vos expériences. Un dossier intitulé `mlruns` (ce nouveau dossier contient les répertoires de vos epériences) a été crée dans votre dossier contenant vos scripts Python.
1. Ouvrir un invite de commande/terminal.
2. Se déplacer jusqu'au dossier des scripts Python à l'aide de la commande `cd`.
3. Taper sur l'invite de commande/terminal `mlflow ui`.
   * Si un message d'erreur apparaît précisant que la commande `mlflow` n'est pas reconnu comme un exécutable, cela signifie que vous n'avez pas configuré une variable d'environnement pour MLFlow. Je vous recommande de (re)lire le fichier [`README.md`](https://github.com/StevanStanovic/mlflow/blob/master/README.md) de la racine du dépôt.
   * Sinon, un message vous informe que Tracking UI a été lancé sur une adresse Internet local.
4. Ne pas fermer l'invite de commande/terminal, ouvrir son navigateur web et copier-coller l'adresse web ou alors taper http://localhost:5000/ (cela revient normalement au même)
5. L'interface Tracking UI apparaît.

![Image of Tracking UI interface](Images/Tracking_UI_interface.png)

Pour plus d'informations, je vous recommande le tutoriel de la [documentation de MLFlow](https://www.mlflow.org/docs/latest/quickstart.html#quickstart).

**Accès au Tracking UI sur Databricks**

0. Créer un fichier expérience MLFlow `Mlflow Experiment`, cliquer sur le fichier et récupérer la référence de l'ID expérience (`Experiment ID`).
1. Lancer vos expériences.
2. Retourner dans le fichier expérience MLFlow et visualiser votre répertoire d'expérience.
![Image of Tracking UI in Databricks](Images/Tracking_UI_databricks.PNG)

Présentation du jeu de données
------------------------------

Implémentation en local
-----------------------

Implémentation sur Databricks
-----------------------------
