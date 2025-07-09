from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base

class Flight(Base):
    __tablename__ = "flights"

    id             = Column(Integer, primary_key=True, index=True)
    number         = Column(String, nullable=False, unique=True, index=True)
    departure_time = Column(DateTime, nullable=False)
    arrival_time   = Column(DateTime, nullable=False)
    status         = Column(String, nullable=False, default="scheduled")
