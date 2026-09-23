from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

@app.get("/")
def home():
    return {
  "message": "AI Agent Platform API",
  "status": "running"
}