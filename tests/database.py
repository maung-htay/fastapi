from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.configs import settings
from app.database import get_db,Base
from app import schemas
from app.main import app
from alembic import command

# Testing database setup 
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test"
# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:root@localhost:5432/fastapi_test'

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base.metadata.create_all(bind=engine)
# Base = declarative_base()

# Dependency
# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# client = TestClient(app)

@pytest.fixture(scope='module')
def session():
    Base.metadata.drop_all(bind=engine) # drop all table 
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope='module')
def client(session):
    def override_get_db():
        # db = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()
    # command.upgrade("head")
    # Base.metadata.drop_all(bind=engine) # drop all table 
    # Base.metadata.create_all(bind=engine)
    # yield is same of return but it will continue 
    # yield TestClient(app)
    # Base.metadata.drop_all(bind=engine)
    # command.downgrade("base")
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)