MLFlow Model Registry et déploiement d'un algorithme sur Azure Machine Learning (AML)
=====================================================================================


Objectifs
---------

* **Compréhension de MLFlow Model Registry**
* **Gestion d'un registre de modèles avec MLFlow en local et sur Databricks**
* **Déploiement d'un modèle MLFlow sur Azure Machine Learning (AML)**

Composition du dossier
----------------------

Le dossier est composé d'un seul dossier comportant l'implémentation de MLFlow Model Registry sur Databricks. En ce qui concerne l'implémentation en local, les notebooks Databricks peuvent être réutilisés et adaptés facilement.

Présentation du composant MLFlow Model Registry
-----------------------------------------------

Le composant MLFlow Model Registry est à la fois un registre de modèles centralisés, une API et une interface utilisateur. Il permet de gérer de manière collaborative le cycle de vie complet d'un modèle MLflow :
* Ajout d'un MLFlow Model à un regitre
* Enregistrer des versions de modèle ML
* Ajouter ou modifier une description à un modèle ou un registre
* Renommer un modèle
* Manager les transitions d'un modèle dans plusieurs états
* Archiver et supprimer un modèle

Implémentation
--------------

L'implémentation de MLFlow Registry est inspiré d'un workshop Databricks et d'une présentation de Databricks de leur composant. Ci-dessous, vous trouverez les vidéos YouTube de ces derniers.

   * [Workshop *Managing the Complete Machine Learning Lifecycle with MLflow* de Databricks par Jules S. Damji](https://www.youtube.com/watch?v=AxYmj8ufKKY&list=PLTPXxbhUt-YWjDg318nmSxRqTgZFWQ2ZC&index=3)
   * [Présentation de MLFlow par Matei Zaharia & Corey Zumar](https://www.youtube.com/watch?v=MSUTaCBhD7A&list=PLTPXxbhUt-YVstcW1-OrYoRiAipXRManO)
