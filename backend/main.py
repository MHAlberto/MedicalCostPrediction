import os
import numpy as np
import pandas as pd
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="MediCare Plus - API de Predicción")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'model.pkl')
PREPROCESSOR_PATH = os.path.join(BASE_DIR, '..', 'models', 'preprocessor.pkl')

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

VALID_REGIONS = ['northeast', 'northwest', 'southeast', 'southwest']
COLUMN_ORDER = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

class PredictionInput(BaseModel):
    age: int = Field(ge=18, le=80)
    sex: str
    bmi: float = Field(ge=10, le=60)
    children: int = Field(ge=0, le=10)
    smoker: str
    region: str

class PredictionOutput(BaseModel):
    predicted_charges: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: PredictionInput):
    if data.region not in VALID_REGIONS:
        return {"error": f"Region must be one of {VALID_REGIONS}"}

    input_df = pd.DataFrame(
        [[data.age, data.sex, data.bmi, data.children, data.smoker, data.region]],
        columns=COLUMN_ORDER
    )
    X_transformed = preprocessor.transform(input_df)
    log_pred = model.predict(X_transformed)[0]
    prediction = float(np.exp(log_pred))

    return {"predicted_charges": round(prediction, 2)}
