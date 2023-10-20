import os 
import sys 
import dill 

import numpy as np
import pandas as pd 
from sklearn.metrics import accuracy_score, recall_score, precision_score, roc_auc_score

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys) 
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(list(models))):
            # get model from model dictionary in list at index i 
            model = list(models.values())[i]
            # fit current model 
            model.fit(X_train, y_train)
            # get predictions 
            y_train_preds = model.predict(X_train)
            y_test_preds = model.predict(X_test)
            # get accuracy scores for train and test data 
            train_accuracy = accuracy_score(y_train_preds, y_train)
            test_accuracy = accuracy_score(y_test_preds, y_test)
            # save test accuracy 
            report[list(models.keys())[i]] = test_accuracy
        # return accuracy scores for all models in a dictionary 
        return report
    except Exception as e: 
        raise CustomException(e, sys)

# loads .pkl file objects (for model and preprocessor pkl files) 
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)