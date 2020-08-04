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

![Comparison of a metric wit a parameter for a SVM classifier](Images/Comparing_metric_with_parameter_SVM.PNG)

Présentation du jeu de données
------------------------------

Implémentation en local et Tracking UI
--------------------------------------

Implémentation sur Databricks et Tracking UI
--------------------------------------------
