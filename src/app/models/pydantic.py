from datetime import datetime

from pydantic import BaseModel


class ReservationPayloadSchema(BaseModel):
    restaurant_id: int
    table_id: int
    start: datetime
    end: datetime
    guests: int


class ReservationResponseSchema(ReservationPayloadSchema):
    id: int
