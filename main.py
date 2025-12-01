from fastapi import FastAPI
from datetime import datetime


app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "API de teste"
    }

@app.get("/date/day")
def get_date_day() -> dict:
    return {
        "datetime": datetime.now().strftime("%Y-%m-%d")
    }
