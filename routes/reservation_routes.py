from fastapi import APIRouter
from services.reservaService import ReservationService

router = APIRouter()
service = ReservationService()

@router.post("/create")
def create_reservation(student_id: str, place_id: str, start_hour: str, end_hour: str):
    return service.create_reservation(student_id, place_id, start_hour, end_hour)

@router.get("/readReserv")
def read_reservation_route(id_user: str):
    return service.read_Reservation(id_user)

@router.delete("/deleteReserv")
def delete_reservation_route(id_user:str):
    return service.delete_Reservation(id_user)