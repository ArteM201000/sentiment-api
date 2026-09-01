from fastapi import APIRouter
from app.schemas.prediction import TextForPrediction
from app.services.model import pipe, tfidf, clf

router = APIRouter()

posneg = {
    1: "positive",
    0: "negative",
    }

@router.post("/predict")
def predicted_text(request: TextForPrediction):
    prediction = pipe.predict([request.text])

    return {"prediction": posneg[prediction[0]], 
            "weights": [{word: [clf.coef_[0][tfidf.vocabulary_.get(word)]] for word in request.text.split() if word in tfidf.vocabulary_}], 
            "text": request.text.split()}