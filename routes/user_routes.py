from fastapi import APIRouter
from services.studentService import create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create")
def create_user_route(id_user: str, name_user: str):
    return create_user(id_user, name_user)

