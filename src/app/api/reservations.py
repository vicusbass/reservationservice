from fastapi import APIRouter

from app.api import crud
from app.api.models import ReservationDB, ReservationSchema

router = APIRouter()


@router.post("/", response_model=ReservationDB, status_code=201)
async def create_reservation(payload: ReservationSchema):
    reservation_id = await crud.post(payload)
    response = {
        "id": reservation_id,
        "restaurant_id": payload.restaurant_id,
        "table_id": payload.table_id,
        "start": payload.start,
        "end": payload.end,
        "guests": payload.guests,
    }
    return response
