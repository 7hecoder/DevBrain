from fastapi import APIRouter
import uuid

router = APIRouter()


@router.get("/uuid")
def generate_uuid():
    return {
        "uuid": str(uuid.uuid4())
    }
