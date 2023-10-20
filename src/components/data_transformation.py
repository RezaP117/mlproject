# feature engineering, data cleaning 
import sys 
import os 
from dataclasses import dataclass  

import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import StandardScaler, OneHotEncoder 

from src.exception import CustomException 
from src.logger import logging 
from src.utils import save_object 

@dataclass 
class DataTransformationConfig: 
    preprocessor_obj_file_path = os.path.join("artifact", "preprocessor.pkl")

class DataTransformation: 
    def __init__(self): 
        self.data_transformation_config = DataTransformationConfig()

    '''
    This function is responsible for data transformation 
    '''
    def get_data_transformer_object(self):
        try: 
            categorical_features = ["sex", "dataset", "cp", "fbs", "restecg", "exang", "slope", "thal"]
            numerical_features = ["age", "trestbps", "chol", "thalch", "oldpeak", "ca"]

            numerical_pipeline = Pipeline([
                #("imputer", SimpleImputer(strategy = "median")), 
                ("scaler", StandardScaler())
            ])
            categorical_pipeline = Pipeline([
                #("imputer", SimpleImputer(strategy = "most_frquent"))
                ("encoder", OneHotEncoder(drop = "first")),
                #("scaler", StandardScaler())
            ])

            logging.info("Numerical categories encoding finished")
            logging.info("Categorical categories encoding finished")

            preprocessor = ColumnTransformer(
                transformers = [
                    ("num_pipeline", numerical_pipeline, numerical_features), 
                    ("cat_pipeline", categorical_pipeline, categorical_features)
                ]
            )

            return preprocessor 
        
        except Exception as e: 
            raise CustomException(e, sys)
            
    def initaite_data_transformation(self, train_path, test_path):
        try: 
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            # drop NaN rows 
            train_df = train_df.dropna()
            test_df = test_df.dropna()

            train_df["num"] = train_df["num"].map({0 : 0, 1 : 1, 2 : 1, 3 : 1, 4 : 1})
            test_df["num"] = test_df["num"].map({0 : 0, 1 : 1, 2 : 1, 3 : 1, 4 : 1})
            logging.info("successfully read train and test data")
            logging.info("Getting preprocessing object")

            preprocessor_obj = self.get_data_transformer_object()
            target_col_name = "num"
            non_important_col = "id"

            logging.info(f"obtained preprocessor object {preprocessor_obj}")
            input_feature_train_df = train_df.drop(columns = [target_col_name, non_important_col], axis = 1)
            target_feature_train_df = train_df[target_col_name]
            # changing fbs and exang to strings to avoid errors when using .transform on user input 
            '''
            X["fbs"] = X["fbs"].astype(str)
            X["exang"] = X["exang"].astype(str)
            '''
            input_feature_train_df["fbs"] = input_feature_train_df["fbs"].astype(str)
            input_feature_train_df["exang"] = input_feature_train_df["exang"].astype(str)

            input_feature_test_df = test_df.drop(columns = [target_col_name, non_important_col], axis = 1)
            target_feature_test_df = test_df[target_col_name]

            input_feature_test_df["fbs"] = input_feature_test_df["fbs"].astype(str)
            input_feature_test_df["exang"] = input_feature_test_df["exang"].astype(str)

            logging.info("Applying preprocessing object on train and test data")
            # using preprocessor on training and testing dataframes 
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            # np.c_ concatenates numpy arrays together along their columns
            # (combines arrays that have the same number of rows)
            train_array = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_array = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
        
            save_object(self.data_transformation_config.preprocessor_obj_file_path,
                        preprocessor_obj
            )

            logging.info("Preprocessing of data completed")
            return (train_array, test_array, 
                    self.data_transformation_config.preprocessor_obj_file_path)
        except Exception as e: 
            raise CustomException(e, sys)