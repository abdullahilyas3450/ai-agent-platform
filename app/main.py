from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
  "message": "AI Agent Platform API",
  "status": "running"
}