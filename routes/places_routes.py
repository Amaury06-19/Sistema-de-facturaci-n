from fastapi import APIRouter
from services.placeService import placeService

router = APIRouter(prefix="/places", tags=["Places"])
places = placeService()

@router.post("/create")
def create_place_route(id_espacio: str):
    return places.create_place(id_espacio)

@router.get("/get")
def get_place_route():
    return places.read_available_place()