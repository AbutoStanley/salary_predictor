# app/main.py
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from fastapi import FastAPI
from app.schemas import SalaryRequest
from app.model import predict_salary
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Salary Prediction API",
    description="Predict tech salary based on experience and company attributes",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

@app.post("/predict")
def predict(request: SalaryRequest):
    prediction = predict_salary(request.dict())
    return {
        "predicted_salary_usd": round(prediction, 2)
    }

