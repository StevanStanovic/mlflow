import numpy as np
import pandas as pd
import mlflow
import mlflow.tensorflow
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

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
    
def mlflow_run(exp_id=None, run_name=None):
  
    with mlflow.start_run(run_name=run_name, experiment_id=exp_id) as run:
        run_id = run.info.run_uuid
        
        (X, y) = import_data('/dbfs/FileStore/tables/Churn_Modelling.csv')    
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
        
        classifier = build_model()
        mlflow.tensorflow.autolog()
        classifier.fit(X_train, y_train, batch_size = 32, epochs = 100)
        y_pred = classifier.predict(X_test)
        y_pred = (y_pred > 0.5)

        TP, FP, FN, TN = confusion_matrix(y_test, y_pred).ravel()
        sensitivity_recall_TPR = TP/(TP+FN)
        specificity_TNR = TN/(TN+FP)
        precision_PPV = TP/(TP+FP)
        NPV = TN/(TN+FN)
        fallout_FPR = 1 - specificity_TNR
        FDR = 1 - precision_PPV
        accuracy = (TP+TN)/(y_test.shape[0])
        
        mlflow.log_metric("sensitivity_recall_TPR", sensitivity_recall_TPR)
        mlflow.log_metric("specificity_TNR", specificity_TNR)
        mlflow.log_metric("precision_PPV", precision_PPV)
        mlflow.log_metric("NPV", NPV)
        mlflow.log_metric("fallout_FPR", fallout_FPR)
        mlflow.log_metric("FDR", FDR)
        mlflow.log_metric("accuracy", accuracy)

        return run_id
        
   if __name__=='__main__':
    exp_id = 524464345401946
    run_name = "ANN"
    run_id = mlflow_run(exp_id, run_name)
    print("Experience finie !\n exp_id = {} et run_id = {}".format(exp_id, run_id))
