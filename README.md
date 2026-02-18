# 🫀 Heart Attack Risk Prediction API

A REST API built with FastAPI that serves a trained Machine Learning model for heart attack risk prediction.
The model is packaged inside a Docker container and loaded at application startup.

## 🔬 Machine Learning Model

The model was developed and trained in a separate repository:

ML Project Repository: https://github.com/IsaacMS30/heart-attack-risk-detection

This API consumes the serialized model artifact (e.g., .pkl) and exposes it through HTTP endpoints.

## 🛠 Tools

- Python 3.11

- FastAPI

- Scikit-learn

- Docker

## 🐳 Run with Docker

### Build the image:

docker build -t heart-attack-risk-api .


### Run the container:

docker run -p 8000:80 heart-attack-risk-api


After that, API available at:

http://localhost:8000/docs

## 📡 Endpoints

**GET / – Health check**

**GET /docs – Interactive documentation**

**POST /predict – Risk prediction**

Body for this endpoint:
<pre> {
  "age": 52,
  "sex": 1,
  "chest_pain_type": 2,
  "resting_blood_pressure": 140,
  "cholesterol": 230,
  "fasting_blood_sugar": 0,
  "rest_ecg": 1,
  "max_heart_rate": 150,
  "exercise_induced_angina": 0,
  "st_depression": 1.4,
  "st_slope": 2
}
</pre>

## 📌 Notes

- The model is loaded once at startup.

- The application is fully containerized and portable.

- Stateless design allows horizontal scaling.
