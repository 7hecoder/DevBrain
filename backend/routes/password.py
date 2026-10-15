from fastapi import APIRouter
from validators.password import validate_password_length
from services.password_service import generate_secure_password


router = APIRouter()


@router.get("/password", responses={400: {"description": "Password length must be between 4 and 128."}},)
def generate_password(length: int = 12):

    validate_password_length(length)

    return generate_secure_password(length)
