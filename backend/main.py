from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.uuid import router as uuid_router
from routes.password import router as password_router
from routes.hash import router as hash_router
from routes.timestamp import router as timestamp_router
from routes.base64 import router as base64_router
from routes.advanced_tools import router as advanced_tools_router

app = FastAPI(
    title="DevBrain API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to DevBrain API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(uuid_router)
app.include_router(password_router)
app.include_router(hash_router)
app.include_router(timestamp_router)
app.include_router(base64_router)
app.include_router(advanced_tools_router)
