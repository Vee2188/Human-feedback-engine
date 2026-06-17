from sqlalchemy import Column, Integer, Float
from backend.database import Base

class DailyLogDB(Base):
    __tablename__ = "daily_logs"

    id = Column(Integer, primary_key=True, index=True)
    sleep_hours = Column(Float)
    exercise_minutes = Column(Integer)
    mood = Column(Integer)
