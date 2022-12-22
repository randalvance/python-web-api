from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{id}")
async def get_id(id: int):
    return {"id": id}
