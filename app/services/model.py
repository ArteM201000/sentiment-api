import joblib

pipe = joblib.load("model/sentiment_pipeline.pkl")

tfidf = pipe.named_steps["tfidf"]
clf = pipe.named_steps["clf"]