# Databricks notebook source
import mlflow
from mlflow import projects

# COMMAND ----------

token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
dbutils.fs.put("file:///root/.databrickscfg","[DEFAULT]\nhost=https://community.cloud.databricks.com\ntoken = "+token,overwrite=True)
print(token)

# COMMAND ----------

ml_project_uri = "https://github.com/StevanStanovic/mlflow.git"
exp = mlflow.run(ml_project_uri, entry_point="main")
#exp2 = projects.run(ml_project_uri)