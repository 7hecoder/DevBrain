
import base64
import difflib
import json
import regex as re
from urllib.parse import quote, unquote


def format_json(text: str):
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as error:
        return {
            "valid": False,
            "error": error.msg,
            "line": error.lineno,
            "column": error.colno,
        }

    return {
        "valid": True,
        "formatted": json.dumps(parsed, indent=2, ensure_ascii=False),
    }


def encode_url(text: str):
    return {"input": text, "result": quote(text, safe="")}


def decode_url(text: str):
    return {"input": text, "result": unquote(text)}


def compare_text(original: str, modified: str):
    diff = list(difflib.unified_diff(
        original.splitlines(),
        modified.splitlines(),
        fromfile="original",
        tofile="modified",
        lineterm="",
    ))

    return {
        "original_lines": len(original.splitlines()),
        "modified_lines": len(modified.splitlines()),
        "diff": "\n".join(diff),
        "identical": original == modified,
    }


def test_regex(pattern: str, text: str, flags: str = ""):
    if len(pattern) > 500:
        raise ValueError("Pattern is too long (maximum 500 characters).")

    if len(text) > 20000:
        raise ValueError("Test text is too long (maximum 20,000 characters).")

    regex_flags = 0
    if "i" in flags:
        regex_flags |= re.IGNORECASE
    if "m" in flags:
        regex_flags |= re.MULTILINE
    if "s" in flags:
        regex_flags |= re.DOTALL

    compiled = re.compile(pattern, regex_flags)
    matches = []

    for match in compiled.finditer(text, timeout=0.1):
        matches.append({
            "match": match.group(0),
            "start": match.start(),
            "end": match.end(),
            "groups": list(match.groups()),
        })

        if len(matches) >= 500:
            break

    return {
        "pattern": pattern,
        "match_count": len(matches),
        "matches": matches,
    }


def decode_jwt(token: str):
    parts = token.strip().split(".")

    if len(parts) != 3:
        raise ValueError("A JWT must contain three dot-separated parts.")

    def decode_part(part: str):
        padding = "=" * (-len(part) % 4)
        try:
            decoded = base64.urlsafe_b64decode(part + padding)
            return json.loads(decoded)
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError(
                "The JWT header or payload is not valid Base64URL JSON."
            ) from error

    header = decode_part(parts[0])
    payload = decode_part(parts[1])

    if not isinstance(header, dict) or not isinstance(payload, dict):
        raise ValueError("The JWT header and payload must be JSON objects.")

    return {
        "header": header,
        "payload": payload,
        "signature_present": bool(parts[2]),
        "verified": False,
        "warning": "Decoded only. The signature has not been verified; claims are untrusted.",
    }
