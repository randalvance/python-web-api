from fastapi import APIRouter

router = APIRouter(tags=["heroes"])


@router.get("/")
async def get_heroes():
    return [{"id": 1, "name": "Batman"}, {"id": 2, "name": "Superman"}]


@router.get("/{id}")
async def get_heroes(id: str):
    return {"id": id, "name": "Batman"}
