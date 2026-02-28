# app/main.py

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI
from app.schemas import SalaryRequest
from app.model import predict_salary
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Salary Prediction API",
    description="Predict tech salary based on experience and company attributes",
    version="1.0.0"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # app/
PROJECT_ROOT = os.path.dirname(BASE_DIR)                # project/

STATIC_DIR = os.path.join(PROJECT_ROOT, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


@app.post("/predict")
def predict(request: SalaryRequest):
    logger.info(f"Prediction request: {request.dict()}")
    prediction = predict_salary(request.dict())
    return {"predicted_salary_usd": round(prediction, 2)}