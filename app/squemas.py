from pydantic import BaseModel

class PatientData(BaseModel):
    age: int
    gender: int # 0 = female, 1 = male
    chest_pain_type: int # 0-3
    resting_bp: int
    cholesterol: int
    fasting_bs: int
    resting_ecg: int # 0-2
    max_heart_rate: int
    exercise_angina: int
    oldpeak: float
    slope: int
    major_vessels: int

