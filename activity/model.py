from pydantic import BaseModel, Field
from datetime import date, time

class ActivityModel(BaseModel):
    day: date = Field(...,example="2025-04-13")
    begning: time = Field(...,example="08:00:00") 
    end: time = Field(...,example="10:00:00") 
