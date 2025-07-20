from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import vulnerability

app = FastAPI(title="ChainSage API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vulnerability.router, prefix="/vulnerability", tags=["Smart Contracts"])

@app.get("/")
def root():
    return {
        "message": "🚀 Welcome to ChainSage API!",
        "endpoints": {
            "Vulnerability Check": "/vulnerability/analyze"
        }
    }
