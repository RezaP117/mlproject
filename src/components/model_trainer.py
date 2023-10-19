import os 
import sys 
from dataclasses import dataclass 

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, r2_score, mean_absolute_error, mean_squared_error
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, evaluate_models 

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifact", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    # output of data transformation is passed to model trainer function 
    def start_model_trainer(self, train_array, test_array): 
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            # dictionary of models to try 
            models = {
                "Logistic Regression" : LogisticRegression(penalty = "l2", solver = "liblinear"), 
                "KNN" : KNeighborsClassifier(n_neighbors = 7), 
                "Decision Tree" : DecisionTreeClassifier(max_depth = 5), 
                "SVM" : SVC(kernel = "rbf")
            }

            model_report:dict = evaluate_models(X_train, y_train, X_test, y_test, models)
            logging.info("MODEL REPORT")
            logging.info(model_report)
            logging.info("END MODEL REPORT")
            # get best model 
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.7:
                raise CustomException("No sufficient model accuracy", sys)

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model 
            )

            predicted = best_model.predict(X_test)
            acc = accuracy_score(y_test, predicted)
            return acc 
        
        except Exception as e: 
            raise CustomException(e, sys)