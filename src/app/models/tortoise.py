from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class ReservationSummary(models.Model):
    # id = fields.IntField(pk=True)
    restaurant_id = fields.TextField()
    table_id = fields.TextField()
    start = fields.DatetimeField()
    end = fields.DatetimeField()
    guests = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.guests} people starting on {self.start}"


ReservationSchema = pydantic_model_creator(ReservationSummary)
