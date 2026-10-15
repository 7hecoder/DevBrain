from fastapi import HTTPException


def validate_password_length(length: int):

    if length < 4:
        raise HTTPException(
            status_code=400,
            detail="Length must be at least 4"
        )

    if length > 128:
        raise HTTPException(
            status_code=400,
            detail="Length cannot exceed 128"
        )
