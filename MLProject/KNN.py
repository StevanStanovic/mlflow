# K-Nearest Neighbors (KNN)

# Importing Python modules
import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import sys

# Importing data
def import_data(path):
    dataset = pd.read_csv(path)
    X = dataset.iloc[:, 3:-1].values
    y = dataset.iloc[:, -1].values
    le = LabelEncoder()
    X[:, 2] = le.fit_transform(X[:, 2])
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))
    sc = StandardScaler()
    X = sc.fit_transform(X)
    return (X, y)

# Starting a MLFlow experiment
def mlflow_run(parameters, run_name=None):
  
    with mlflow.start_run(run_name=run_name) as run:
        
        # Recovering run ID and experiment ID
        run_id = run.info.run_uuid
        exp_id = run.info.experiment_id
        
        # Importing and splitting data
        (X, y) = import_data('Churn_Modelling.csv')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
        
        # Creating classifier
        classifier = KNeighborsClassifier(n_neighbors = parameters[0], metric = parameters[1], p = parameters[2])
        
        # Logging tags and parameters
        mlflow.set_tag("Number of parameters", len(parameters))
        mlflow.log_params({
          "n_neighbors" : parameters[0],
          "metrics" : parameters[1],
          "p" : parameters[2]
        })
        mlflow.set_tag("Theorical information", "metrics->minkowski + p->2 = euclidian norm")
        
        # Fitting the training set and predicting the test set
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        
        # Storing confusion matrix metrics in variables
        TP, FP, FN, TN = confusion_matrix(y_test, y_pred).ravel()
        sensitivity_recall_TPR = TP/(TP+FN)
        specificity_TNR = TN/(TN+FP)
        precision_PPV = TP/(TP+FP)
        NPV = TN/(TN+FN)
        fallout_FPR = 1 - specificity_TNR
        FDR = 1 - precision_PPV
        accuracy = (TP+TN)/(y_test.shape[0])
        
        # Logging metrics
        mlflow.log_metric("sensitivity_recall_TPR", sensitivity_recall_TPR)
        mlflow.log_metric("specificity_TNR", specificity_TNR)
        mlflow.log_metric("precision_PPV", precision_PPV)
        mlflow.log_metric("NPV", NPV)
        mlflow.log_metric("fallout_FPR", fallout_FPR)
        mlflow.log_metric("FDR", FDR)
        mlflow.log_metric("accuracy", accuracy)
        
        # Logging model
        mlflow.sklearn.log_model(classifier, run_name + "_Model")

        return (run_id, exp_id)

# Running the experiment
if __name__=='__main__':
    # Setting run name
    run_name = "KNN"
    nb_neighbors = int(sys.argv[1])
    metric = str(sys.argv[2])
    p = int(sys.argv[3])
    params = [nb_neighbors, metric, p]
    (run_id, exp_id) = mlflow_run(params, run_name)
    print("Finish experiment !\n exp_id = {} et run_id = {}".format(exp_id, run_id))
