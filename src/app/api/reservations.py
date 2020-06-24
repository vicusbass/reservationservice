from typing import List

from fastapi import APIRouter, HTTPException, Path

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
async def get_reservation(reservation_id: int = Path(..., gt=0)) -> ReservationResponseSchema:
    reservation = await crud.get(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation


@router.get("", response_model=List[ReservationResponseSchema])
async def get_reservations() -> List[ReservationResponseSchema]:
    return await crud.get_all()


@router.delete("/{reservation_id}", status_code=204)
async def delete_reservation(reservation_id: int) -> ReservationResponseSchema:
    reservation = await crud.get(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return await crud.delete(reservation_id)
