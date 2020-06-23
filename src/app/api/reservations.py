from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import ReservationResponseSchema, ReservationPayloadSchema

router = APIRouter()


@router.post("", response_model=ReservationResponseSchema, status_code=201)
async def create_reservation(payload: ReservationPayloadSchema) -> ReservationResponseSchema:
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


@router.get("/{reservation_id}", response_model=ReservationResponseSchema)
async def get_reservation(reservation_id: int) -> ReservationResponseSchema:
    reservation = await crud.get(reservation_id)
    return reservation
