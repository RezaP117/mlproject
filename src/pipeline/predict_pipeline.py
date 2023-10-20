import sys 
import pandas as pd 

from src.exception import CustomException
from src.utils import load_object 
from src.logger import logging 

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

class PredictionPipeline():
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            model_path = "artifact/model.pkl"
            preprocessor_path = "artifact/preprocessor.pkl"
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            # transform features 
            data_scaled = preprocessor.transform(features)
            # predict 
            pred = model.predict(data_scaled)
            return pred 
        except Exception as e: 
            raise CustomException(e, sys)

# responsible for mapping all inputs we are getting from the html 
class CustomData: 
    # age,sex,dataset,cp,trestbps,chol,fbs,restecg,thalch,exang,oldpeak,slope,ca,thal
    def __init__(self, age:int, sex:str, dataset:str, cp:str, trestbps:int, 
                 chol:int, fbs:str, restecg:str, thalch:int, exang:str, oldpeak:float,
                 slope:str, ca:int, thal:str):
        self.age = age
        self.sex = sex
        self.dataset = dataset
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalch = thalch
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal 

    def get_data_as_frame(self):
        # create dataframe out of user input 
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "dataset": [self.dataset],
                "cp": [self.cp],
                "trestbps": [self.trestbps],
                "chol": [self.chol],
                "fbs": [self.fbs],
                "restecg": [self.restecg],
                "thalch": [self.thalch],
                "exang": [self.exang],
                "oldpeak": [self.oldpeak],
                "slope": [self.slope],
                "ca": [self.ca],
                "thal": [self.thal]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e: 
            raise CustomException(e, sys) 
        
