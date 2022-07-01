# from flask import current_app, g
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import validates, relationship
from garden_companion_api.database import Base

# db = g.db


class Pest(Base):
    __tablename__ = 'pests'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    description = Column(Text)
    detection = Column(Text)
    deterrent = Column(Text)
