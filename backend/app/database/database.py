from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# 1. Create the Engine
# check_same_thread: False is required ONLY for SQLite.
# This allows multiple threads to interact with the database.
if settings.DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        settings.DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(settings.DATABASE_URL)

# 2. Create a Session Factory
# autocommit=False: We want to manually control when we save (commit) data.
# autoflush=False: We don't want it to send data to the DB before we are ready.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create the Declarative Base
# Our future models (User, Transaction) will inherit from this class.
Base = declarative_base()

# 4. Dependency for FastAPI routes
# This function creates a new DB session for every request and closes it after.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()