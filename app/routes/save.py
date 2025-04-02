# app/routes/save.py
from fastapi import APIRouter, HTTPException
from app.models import ResponsePayload
from app.database import collection
from pymongo.errors import PyMongoError

router = APIRouter()

@router.post("/save")
def save_response(payload: ResponsePayload):
    try:
        result = collection.insert_one(payload.dict())
        return {"status": "success", "inserted_id": str(result.inserted_id)}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")