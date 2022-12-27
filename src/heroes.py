from fastapi import APIRouter, Depends

from auth import Authorize

router = APIRouter(tags=["heroes"])


@router.get("/")
async def get_heroes(user=Depends(Authorize())):
    print(user)
    return [{"id": 1, "name": "Batman"}, {"id": 2, "name": "Superman"}]


@router.get("/{id}")
async def get_heroes(id: str):
    return {"id": id, "name": "Batman"}
