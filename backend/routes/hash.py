
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from validators.hash import validate_hash_request
from services.hash_service import generate_hash

router = APIRouter()


class HashRequest(BaseModel):
    text: str = Field(..., max_length=20000)
    algorithm: str = Field(..., max_length=20)


@router.post("/hash")
def hash_text(request: HashRequest):
    validate_hash_request(request.text, request.algorithm)

    hashed_value = generate_hash(request.text, request.algorithm)

    return {
        "input": request.text,
        "algorithm": request.algorithm,
        "hash": hashed_value,
    }
