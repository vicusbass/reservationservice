from typing import Union

from app.models.pydantic import ReservationPayloadSchema
from app.models.tortoise import ReservationSummary


async def post(payload: ReservationPayloadSchema) -> int:
    reservation = ReservationSummary(
        restaurant_id=payload.restaurant_id,
        table_id=payload.table_id,
        start=payload.start,
        end=payload.end,
        guests=payload.guests,
    )
    await reservation.save()
    return reservation.id


async def get(reservation_id: int) -> Union[dict, None]:
    reservations = await ReservationSummary.filter(id=reservation_id).first().values()
    if reservations:
        return reservations[0]
    return None
