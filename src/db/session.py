from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the connection URL to PostgreSQL
DATABASE_URL = "postgresql://myuser:mypassword@postgres:5432/mydb"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Provides a database session for FastAPI.
    To be used as a dependency in your endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
