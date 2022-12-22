from fastapi import FastAPI
from settings import appsettings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/settings")
async def get_settings():
    return appsettings.dict()


@app.get("/{id}")
async def get_id(id: int):
    return {"id": id}