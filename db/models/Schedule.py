# from flask import current_app, g
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.types import JSON
from sqlalchemy.orm import validates, relationship
from garden_companion_api.database import Base

# db = g.db


class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey(
        'plants.id'), nullable=False)
    zone = Column(String(10))
    indoor_months = Column(JSON)
    outdoor_months = Column(JSON)
