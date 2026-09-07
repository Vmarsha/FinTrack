from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from sqlalchemy import text
from app.database.database import engine
# Initialize the FastAPI app
app = FastAPI(title=settings.PROJECT_NAME)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows your React frontend to communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins_list,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": f"Welcome to the {settings.PROJECT_NAME}!"}

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "FinTrack backend is running"}
@app.get("/database-test")
def database_test():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "Database connection successful"}
    except Exception as e:
        return {
            "status": "Database connection failed",
            "error": str(e)
        }