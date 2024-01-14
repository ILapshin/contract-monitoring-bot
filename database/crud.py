import time

from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from sqlalchemy.sql import functions

from database.database import SessionLocal
from database.models import Event
from database.schemas import EventSchema


def get_last_block_number():
    with SessionLocal() as session:
        last_block_number = select(functions.max(Event.block_number))
        return session.scalar(last_block_number)


def get_day_events():
    now = int(time.time())
    day_gap = 24 * 60 * 60

    with SessionLocal() as session:
        day_events = (
            select(Event)
            .where(Event.timestamp.between(now - day_gap, now))
            .order_by(Event.timestamp)
        )
        return session.scalars(day_events).all()


def add_events(events: list[EventSchema]):
    with SessionLocal() as session:
        session.execute(insert(Event), events)
        session.commit()
