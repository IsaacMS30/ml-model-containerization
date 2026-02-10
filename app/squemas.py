from pydantic import BaseModel, Field

class PatientData(BaseModel):
    age: int = Field(ge=0, le=120, description="Age in years")
    gender: int = Field(ge=0, le=1, description="Gender: 0 = female, 1 = male")
    chest_pain_type: int = Field(ge=0, le=3, description="Chest Pain Type: 0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic")
    resting_bp: int = Field(ge=50, le=250, description="Blood pressure of the patient (in mm HG)")
    cholesterol: int = Field(ge=50, le=600, description="Cholesterol in blood (in mg/dl)")
    fasting_bs: int = Field(ge=0, le=1, description="Whether the patient has > 120 mg/dl (0 = false, 1 = true)")
    resting_ecg: int = Field(ge=0, le=2, description="0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria")
    max_heart_rate: int = Field(ge=71, le=202, description="Maximun heart rate of the patient")
    exercise_angina: int = Field(ge=0, le=1, description="1 = Yes, 0 = No")
    oldpeak: float = Field(ge=0, le=6.2, description="0-6.2")
    slope: int = Field(ge=1, le=3, description="Slope of the peak exercise ST segment: 1 = upsloping, 2 = flat, 3 = downsloping")
    major_vessels: int = Field(ge=0, le=3, description="")

class PredictionResult(BaseModel):
    heart_attack_risk: int
    risk_probability: float

