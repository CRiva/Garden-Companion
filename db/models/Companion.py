# from flask import current_app, g
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import validates, relationship
from garden_companion_api.database import Base

# db = g.db


class Companion(Base):
    __tablename__ = 'companions'

    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey('plants.id'), nullable=False)
    effect = Column(Text, nullable=False)
