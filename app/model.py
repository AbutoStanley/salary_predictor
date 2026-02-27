# app/model.py

import joblib
import pandas as pd

model = joblib.load("salary_model.pkl")

def predict_salary(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return float(prediction)