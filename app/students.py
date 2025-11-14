from fastapi import APIRouter

router = APIRouter()

@router.get("/get_info")
async def get_students():
    return {"Students":"student Info"}