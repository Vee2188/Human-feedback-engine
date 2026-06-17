from pydantic import BaseModel

class DailyLog(BaseModel):
    sleep_hours: float
    exercise_minutes: int
    mood: int