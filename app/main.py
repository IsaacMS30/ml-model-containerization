from fastapi import FastAPI
from .squemas import ModelInput
import joblib

app = FastAPI(title="Heart Attack Risk API")

# Load model
model = joblib.load("app/model.joblib")

@app.get("/")
def health_check():
    return {"status": "Ok"}




