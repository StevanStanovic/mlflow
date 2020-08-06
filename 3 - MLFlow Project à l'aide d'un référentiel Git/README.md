MLFlow Project à l'aide d'un référentiel Git et prédiction de nouvelles instances
=================================================================================


Objectifs
---------

* **Compréhension de MLFlow Project**
* **Configuration de l'environnement du MLFlow Model**
* **Execution en local et sur Databricks d'un MLProject à l'aide d'un référentiel GitHub ou GitLab**
* **Prédiction de nouvelles instances**

Composition du dossier
----------------------

Le dossier est composé de deux dossiers comportant d'une part les notebooks Databricks et d'une autre les commandes MLFlow a éxecuté sur l'invite de commande/terminal (fichiers texte). 

Les référentiels GitHub et GitLab de cet exemple se trouve respectivement aux adresses suivantes : [GitHub](https://github.com/StevanStanovic/mlflow/tree/master/MLFlowProject) et [GitLab](https://gitlab.com/stevan.stanovic/mlflow).

Pour la partie prédiction de nouvelles instances, la seconde partie des notebooks Databricks peuvent être réutilisés pour une implémentation locale.


Présentation du composant MLFlow Projects
-----------------------------------------

Le composant MLFlow Projects est un format pour packager du code ML afin de pouvoir le réutiliser et reproduire les mêmes résultats à tout moment. Cela est rendu possible à l'aide de certaines conventions, elles permettent d'organiser et de décrire son code afin de permettre à d'autres utilisateurs de l'exécuter.

Chaque MLFlow Project est simplement un répertoire de fichiers ou un référentiel Git contenant le code. En plus de ce code, un fichier nommé MLproject est présent, c'est la description de notre MLFlow Project. Celui-ci est souvent relié à un autre fichier décrivant l'environnement dans lequel les codes ML vont être exécutés. Ce fichier peut être une description d'un environnement Conda en format YAML ou une image Docker.

En outre, le fichier MLproject possède trois sections :
* **Name** : le nom du projet
* **Entry Points** : les points d'entrées, ce sont des commandes permettant de lancer des exécutables Python ou Shell, on peut préciser si besoin des paramètres (paramètrages par défauts possible)
* **Environnement** : environnement du projet, comme expliqué plus haut, il est décrit soit dans un fichier YAML (environnement Conda uniquement) ou soit dans une image Docker

**Description d'un environnement Conda dans un fichier YAML**

![Image of example of Conda environnement in YAML format](Images/Example_of_conda_environement_YAML.PNG)

**Exemple d'un fichier MLproject**

![Image of example of MLproject](Images/Example_of_MLproject.PNG)

Pour plus d'informations sur les MLFlow Projects, vous pouvez vous référer à la documentation de MLFlow ou de Databricks :
   * [Documentation MLFlow](https://www.mlflow.org/docs/latest/projects.html)
   * [Documentation Databricks](https://docs.databricks.com/applications/mlflow/projects.html)

Présentation du jeu de données
------------------------------

Le jeu de données est le même que pour celui de l'exmeple 1. Je vous invite à vous référer au [`README.md`](https://github.com/StevanStanovic/mlflow/blob/master/1%20-%20MLFlow%20Tracking%20pour%20un%20algorithme%20supervis%C3%A9/README.md) de ce dernier.

Implémentation
--------------

Le jeu de données ainsi que les codes de l'exemple 1 ont été repris dans cet exemple. Ils ont été adaptés. Si vous voulez voir les modifications, cliquez [ici](https://github.com/StevanStanovic/mlflow/tree/master/MLFlowProject). A ces fichiers, il a été rajouté un fichier décrivant un environnement Conda [`conda.yaml`](https://github.com/StevanStanovic/mlflow/blob/master/MLFlowProject/conda.yaml) et un fichier [`MLproject`](https://github.com/StevanStanovic/mlflow/blob/master/MLFlowProject/MLproject).

Dans le ficher YAML, on donne un nom à l'environnement Conda puis on décrit les dépendances et les installations à effectuer dans le Conda.

Dans le ficher MLproject, on donne également un nom et on précise le fichier YAML associé, et enfin, pour chaque modèle (ou fichier Python), on crée un point d'entrée afin de lancer une exécution du code et crée une nouvelle expérience.

Exécution en local
-----------------------

L'exécution en local d'un point d'entrée se fait de la manière suivante :
1. Ouvrir un invite de commande/terminal.
2. Se déplacer dans le répertoire où l'on souhaite créer le `mlruns`.
3. Dans l'invite de commande/terminal, utiliser les lignes de commande dans les fichiers textes présent dans le dossier [Local](https://github.com/StevanStanovic/mlflow/tree/master/3%20-%20MLFlow%20Project%20%C3%A0%20l'aide%20d'un%20r%C3%A9f%C3%A9rentiel%20Git/Local).

*Remarque :* l'installation d'un Anaconda ou Miniconda est nécessaire ainsi que le paramètrage de la variable d'environnement associée (voir le [`README.md`](https://github.com/StevanStanovic/mlflow/blob/master/README.md) du dépôt).

En cas de besoin, la documention MLFlow peut vous aider ([lien documentation MLFlow](https://www.mlflow.org/docs/latest/projects.html#running-projects)).

Exécution sur Databricks
-----------------------------


