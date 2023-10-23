from flask import Flask, request, render_template, jsonify 
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictionPipeline 
from src.logger import logging 

# create application name 
# flask __name__ gives us the entry point (root path) to the application 
application = Flask(__name__)
app = application 

@app.route('/')
# index handles the logic for this specified route 
def index(): 
    return render_template("index.html")

@app.route("/predictdata", methods = ["GET", "POST"])
def predict_datapoint():
    # this page will be a basic template with fields to input data 
    if request.method == "GET":
        return render_template("home.html")
    else:
        logging.info("Getting user inputs from HTML page")
        # Get data from the HTML form
        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        dataset = request.form.get("dataset")
        cp = request.form.get("cp")
        trestbps = int(request.form.get("trestbps"))
        chol = int(request.form.get("cholesterol"))
        fbs = request.form.get("fbs")
        restecg = request.form.get("restecg")
        thalch = int(request.form.get("thalch"))
        exang = request.form.get("exang")
        oldpeak = float(request.form.get("oldpeak"))
        slope = request.form.get("slope")
        ca = int(request.form.get("ca"))
        thal = request.form.get("thal")
        logging.info("Successfully obtained user input from HTML page")
        data = CustomData(age, sex, dataset, cp, trestbps, 
                          chol, fbs, restecg, thalch, exang, oldpeak, slope, ca, thal)
        pred_df = data.get_data_as_frame()
        logging.info(pred_df)

        # initializing predictino pipeline 
        predict_pipeline = PredictionPipeline()
        result = predict_pipeline.predict(pred_df)
        return render_template("home.html", result = result[0])
        #return jsonify(result = result[0])

    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
        