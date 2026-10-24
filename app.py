from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="JennyOma Cloud API", version="1.0.0")

@app.get("/")
def home():
    return {
        "message": "Welcome to JennyOma's Cloud API!",
        "project": "Project 07",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
