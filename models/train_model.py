import pandas as pd
import numpy as np
import joblib
import os
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'processed', '01_insurance.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
PREPROCESSOR_PATH = os.path.join(BASE_DIR, 'preprocessor.pkl')

numeric_features = ['age', 'bmi', 'children']
categorical_features = ['sex', 'smoker', 'region']

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(drop='first', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

df = pd.read_csv(DATA_PATH)
X = df[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = df['charges']

y_log = np.log(y)

X_transformed = preprocessor.fit_transform(X)

model = LinearRegression()
model.fit(X_transformed, y_log)

os.makedirs(BASE_DIR, exist_ok=True)
joblib.dump(model, MODEL_PATH)
joblib.dump(preprocessor, PREPROCESSOR_PATH)

print(f"Modelo guardado en: {MODEL_PATH}")
print(f"Preprocesador guardado en: {PREPROCESSOR_PATH}")
print(f"R² score: {model.score(X_transformed, y_log):.4f}")
