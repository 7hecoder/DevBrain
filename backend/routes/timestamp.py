
from fastapi import APIRouter, HTTPException

from services.timestamp_service import convert_timestamp

router = APIRouter()


@router.get(
    "/timestamp/{timestamp}",
    responses={
        400: {"description": "Timestamp is outside the supported range."}
    },
)
def timestamp_converter(timestamp: float):
    try:
        return convert_timestamp(timestamp)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error
