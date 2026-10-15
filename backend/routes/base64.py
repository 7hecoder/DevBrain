
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from services.base64_service import encode_base64, decode_base64

router = APIRouter()


class Base64Request(BaseModel):
    text: str = Field(..., min_length=1, max_length=20000)


@router.post("/base64/encode")
def base64_encode(request: Base64Request):
    return encode_base64(request.text)


@router.post(
    "/base64/decode",
    responses={
        400: {
            "description": "Invalid Base64 input or decoded content is not valid UTF-8 text."
        }
    },
)
def base64_decode(request: Base64Request):
    try:
        return decode_base64(request.text)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error
