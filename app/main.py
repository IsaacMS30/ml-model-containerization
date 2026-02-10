from fastapi import FastAPI
from .squemas import PatientData, PredictionResult
from .services import predict_heart_disease

app = FastAPI(title="Heart Attack Risk API")

@app.get("/")
def health_check():
    return {"status": "Ok"}

@app.post("/predict", response_model=PredictionResult)
def predict(data: PatientData):
    prediction, probability = predict_heart_disease(data)

    return PredictionResult(
        heart_attack_risk=prediction,
        risk_probability=probability
    )
