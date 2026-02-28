import joblib
import pandas as pd

model = joblib.load("salary_model.pkl")

def predict_salary(data: dict) -> float:
    df = pd.DataFrame([data])
    df = df.reindex(columns=model.feature_names_in_)
    prediction = model.predict(df)[0]
    return float(prediction)