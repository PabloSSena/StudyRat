# main.py
from fastapi import FastAPI
from activity.router import router as activity_router  

app = FastAPI()

# Incluindo o router da atividade com prefixo e tags
app.include_router(activity_router, prefix="/activity", tags=["hours"])
