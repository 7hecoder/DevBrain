from fastapi import HTTPException
from constants.hash import HASH_FUNCTIONS

def validate_hash_request(text: str, algorithm: str):

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty."
        )

    if algorithm.lower() not in HASH_FUNCTIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported algorithm. Choose from: {', '.join(HASH_FUNCTIONS.keys())}"
        )
