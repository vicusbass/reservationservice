import os

from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

reservations = Table(
    "reservations",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("restaurant_id", String(50)),
    Column("table_id", String(50)),
    Column("start", DateTime, nullable=False),
    Column("end", DateTime, nullable=False),
    Column("guests", Integer),
)

database = Database(DATABASE_URL)
