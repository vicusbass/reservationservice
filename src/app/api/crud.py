from app.api.models import ReservationSchema
from app.db import reservations, database


async def post(payload: ReservationSchema):
    query = reservations.insert().values(
        restaurant_id=payload.restaurant_id,
        table_id=payload.table_id,
        start=payload.start,
        end=payload.end,
        guests=payload.guests,
    )
    return await database.execute(query=query)
