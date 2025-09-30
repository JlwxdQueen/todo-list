from fastapi import APIRouter

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/")
async def get_todos():
    return {"message": "list of todos"}
