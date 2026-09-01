from pydantic import BaseModel

class TextForPrediction(BaseModel):
    text: str