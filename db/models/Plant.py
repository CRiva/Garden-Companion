# from flask import current_app, g
from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import validates, relationship
from garden_companion_api.database import Base
from garden_companion_api.db.models.Companion import Companion
from garden_companion_api.db.models.Pest import Pest
from garden_companion_api.db.models.Schedule import Schedule

# db = g.db

pest_association_table = Table(
    "pest_association",
    Base.metadata,
    Column("plant_id", ForeignKey("plants.id")),
    Column("pest_id", ForeignKey("pests.id")),
)


class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    description = Column(Text)
    companions = relationship(Companion, backref='plants', lazy=True)
    pests = relationship(Pest, lazy=True, secondary=pest_association_table)
    schedules = relationship(Schedule, backref='plants', lazy=True)
