from datetime import datetime

from pydantic import BaseModel


class ReservationSchema(BaseModel):
    restaurant_id: str
    table_id: str
    start: datetime
    end: datetime
    guests: int


class ReservationDB(ReservationSchema):
    id: int
