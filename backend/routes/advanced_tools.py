
import regex as re

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from services.advanced_tools_service import (
    format_json,
    encode_url,
    decode_url,
    compare_text,
    test_regex,
    decode_jwt,
)

router = APIRouter()


class TextRequest(BaseModel):
    text: str = Field(..., max_length=100000)


class DiffRequest(BaseModel):
    original: str = Field(..., max_length=50000)
    modified: str = Field(..., max_length=50000)


class RegexRequest(BaseModel):
    pattern: str = Field(..., max_length=500)
    text: str = Field(..., max_length=20000)
    flags: str = Field(default="", max_length=3)


class JWTRequest(BaseModel):
    token: str = Field(..., max_length=20000)


@router.post("/json/format")
def json_format(request: TextRequest):
    return format_json(request.text)


@router.post("/url/encode")
def url_encode(request: TextRequest):
    return encode_url(request.text)


@router.post("/url/decode")
def url_decode(request: TextRequest):
    return decode_url(request.text)


@router.post("/diff")
def text_diff(request: DiffRequest):
    return compare_text(request.original, request.modified)


@router.post("/regex")
def regex_test(request: RegexRequest):
    try:
        return test_regex(
            request.pattern,
            request.text,
            request.flags,
        )
    except TimeoutError as error:
        raise HTTPException(
            status_code=400,
            detail="Regex matching timed out. Try a simpler pattern or shorter text.",
        ) from error
    except (ValueError, re.error) as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@router.post("/jwt/decode")
def jwt_decode(request: JWTRequest):
    try:
        return decode_jwt(request.token)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
