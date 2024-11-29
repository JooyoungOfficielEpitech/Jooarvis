from fastapi import FastAPI
from backend.app.routes import router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}
