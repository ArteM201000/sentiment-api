from fastapi import FastAPI
from app.api.users import router as users_router
from app.api.predict import router as predict_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI"}

@app.get("/about")
def about():
    return {
        "Name": "Artem",
        "age": 16,
        "field": "Machine-Learning"
    }

@app.get("/products/{product_id}")
def get_prod(product_id: int, quantity: int = 1):
    return {
        "product_id": product_id,
        "quantity": quantity
    }

@app.get("/search")
def search(query: str | None = None, limit: int = 10):
    return {
        "query": query,
        "limit": limit,
        }

app.include_router(users_router)
app.include_router(predict_router)