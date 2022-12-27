from fastapi import FastAPI
from settings import appsettings
from heroes import router as heroes_router


app = FastAPI()

app.include_router(heroes_router, prefix="/heroes")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/settings")
async def get_settings():
    return appsettings.dict()


@app.get("/{id}")
async def get_id(id: int):
    return {"id": id}