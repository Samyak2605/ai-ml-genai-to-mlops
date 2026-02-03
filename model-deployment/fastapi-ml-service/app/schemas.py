from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    years_experience: float = Field(..., ge=0, example=3.5)

class PredictionResponse(BaseModel):
    predicted_salary: float
