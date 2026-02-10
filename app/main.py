from fastapi import FastAPI
from .squemas import PatientData, PredictionResult
import joblib
import numpy as np

app = FastAPI(title="Heart Attack Risk API")

# Load model
model = joblib.load("app/model.joblib")

@app.get("/")
def health_check():
    return {"status": "Ok"}

@app.post("/predict", response_model=PredictionResult)
def predict(data: PatientData):
    features = np.array([[
        data.age,
        data.gender,
        data.chest_pain_type,
        data.resting_bp,
        data.cholesterol,
        data.fasting_bs,
        data.resting_ecg,
        data.max_heart_rate,
        data.exercise_angina,
        data.oldpeak,
        data.slope,
        data.major_vessels
    ]])

    prediction = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])


    return PredictionResult(
        heart_attack_risk=prediction,
        risk_probability=probability
    )
