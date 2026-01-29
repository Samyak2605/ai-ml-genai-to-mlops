from fastapi import FastAPI
from app.model import predict_salary

app = FastAPI(title="ML Inference Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: dict):
    years = data.get("years_experience", 0)
    salary = predict_salary(years)
    return {"predicted_salary": salary}
