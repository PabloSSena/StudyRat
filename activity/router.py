from fastapi import APIRouter
from database import activityCollection
from activity.model import ActivityModel

router = APIRouter()

@router.post("/teste")
async def create_activity(activity:ActivityModel):
    print("activity", activity)
    newActivity = await activityCollection.insert_one(activity.model_dump(by_alias=True, exclude=["id"]))
    print("new activity",newActivity)
    createdActivity = await activityCollection.find_one({"_id":newActivity.inserted_id})
    return {"message": "Atividade salva", "data": activity}