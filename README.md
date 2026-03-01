# 🫀 Heart Attack Risk Prediction API

A REST API built with FastAPI that serves a trained Machine Learning model for heart attack risk prediction.

The application is containerized using Docker and deployed to Render.


## 🔬 Machine Learning Model

The model was developed and trained in a separate repository:

ML Project Repository: https://github.com/IsaacMS30/heart-attack-risk-detection

This API consumes the serialized model artifact (e.g., .pkl) and exposes it through HTTP endpoints.


## 🌍 Live Demo

The API is deployed and publicly accessible:

Base URL (Health Check): https://ml-model-containerization.onrender.com

Interactive Docs (Swagger): https://ml-model-containerization.onrender.com/docs


## 🛠 Tools

- Python 3.11

- FastAPI

- Scikit-learn

- Docker


## 🐳 Run Locally with Docker

Build the image:

docker build -t ml-api .

Run the container:

docker run -p 8000:8000 -e PORT=8000 ml-api

Access the API at:
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
