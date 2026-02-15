from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

# CORS Configuration
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000", # If using a frontend dev server
    "*" # For development convenience, restrict in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to NPS IntelliRetire API"}

# Import and include routers later
from app.api.api import api_router
app.include_router(api_router, prefix=settings.API_V1_STR)
