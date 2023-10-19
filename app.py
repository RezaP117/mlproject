from flask import Flask, request, render_template 
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler

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
        pass 