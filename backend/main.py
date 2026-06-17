# importing required libraries
from fastapi import FastAPI
from backend.schemas import DailyLog
from backend.database import SessionLocal
from backend.models import DailyLogDB


app = FastAPI()

@app.get("/")

def test():

    return {"status": "ok"}
    
# @app.get("/")
# def home():
#     return{"message": "Human Feedback Engine is running."}

@app.post("/daily-log")
def create_log(log: DailyLog):
    db = SessionLocal()
    db_log = DailyLogDB(
        sleep_hours=log.sleep_hours,
        exercise_minutes=log.exercise_minutes,
        mood=log.mood
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    db.close()

    return{"message": "saved", "id": db_log.id}
