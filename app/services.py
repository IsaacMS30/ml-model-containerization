from fastapi import HTTPException, status
from .model import model
from .squemas import PatientData
import numpy as np

def predict_heart_disease(data: PatientData):
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

    try:
        prediction = int(model.predict(features)[0])
        probability = float(model.predict_proba(features)[0][1])
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Model prediction failed")

    return prediction, probability
