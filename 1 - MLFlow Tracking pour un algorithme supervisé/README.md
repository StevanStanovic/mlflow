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

Le composant MLFlow Tracking est à la fois une API et une interface utilisateur. Son but est d'enregistrer des paramètres, métriques, fichiers et informations. Cette enregistrement se réalise pendant le lancement d'une expérience de code Machine Learning. Ce lancement est ensuite stocké dans un répertoire dont nous avons donné la référence. Le répertoire en question stocke tous nos lancements dans des dossiers. Ces dossiers sont composés de toutes les informations de nos lancements (paramètres, métriques, fichiers ...)  mais également d'un MLFlow Model. De plus, grâce à l'interface utilisateur de MLFlow Tracking, nous pouvons visualiser ces informations et comparer leurs résultats entre eux. L'interface utilisateur s'appelle Tracking UI.

Le composant MLFlow Model est un format standard pour packager des modèles ML. Il permet de déployer un modèle sur diverses plateformes et/ou services numériques. Plus précisément, il définit une convention qui permet de sauvegarder un modèle dans différentes "*flavors*". La génération d'un MlFlow Model est réalisé de deux manières, soit :
* il est définit par un MLFlow Project et alors l'environnement 


Visualisation des expériences et accès au Tracking UI
------------------------------

Présentation du jeu de données
------------------------------

Implémentation en local et Tracking UI
--------------------------------------

Implémentation sur Databricks et Tracking UI
--------------------------------------------
