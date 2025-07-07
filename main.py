# Define the app entry point for running with uvicorn
# Create the FastAPI app instance
# Include routers (like users.py) to organize endpoints
from fastapi import FastAPI
from database import Base, engine
from routes import users

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)


@app.get("/favicon.ico")
def favicon():
    return {}

@app.get("/")
def read_root():
    return {"message": "Hello World"}