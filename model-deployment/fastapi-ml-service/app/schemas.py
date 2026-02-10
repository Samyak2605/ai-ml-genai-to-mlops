from pydantic import BaseModel


class PredictionRequest(BaseModel):
    years_experience: float
