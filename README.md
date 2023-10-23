## ML PROJECT

Problem Statement: Be able to accurately predict if a patient has heart disease 

Dataset used: https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data/data

Folders:
1. src -> contains project files
2. src -> components -> contains modules for reading and processing data
3. notebook -> data -> contains ipynb files for EDA/Model Training and Training Dataset 
4. templates -> contains HTML files 
5. static -> contains CSS files
6. artifact contains model and preprocessor .pkl files 

To Run: 
1. Open Terminal 
2. Clone repo -> git clone https://github.com/RezaP117/mlproject.git in terminal 
3. Install packages if not already on your machine -> pip install -r requirements.txt in terminal 
4. Start running -> Python app.py in terminal 
5. A Flask App is created and the root directory page is located at -> http://127.0.0.1:5000
6. Click on predict data -> This will take you to http://127.0.0.1:5000/predictdata
7. Input the patients data into the required fields and click submit
8. Heart Disease result will be displayed at the bottom of the page after it refreshes
9. 0.0 means no heart disease, 1.0 means heart disease 
