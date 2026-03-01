from pathlib import Path
import joblib

# Get path
BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "models" / "model.joblib"

# Load model
model = joblib.load(model_path)
