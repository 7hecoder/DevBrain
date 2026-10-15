
import base64
import binascii


def encode_base64(text: str) -> dict:
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    encoded_text = encoded_bytes.decode("utf-8")

    return {
        "original": text,
        "encoded": encoded_text
    }


def decode_base64(encoded_text: str) -> dict:
    try:
        decoded_bytes = base64.b64decode(
            encoded_text,
            validate=True
        )
        decoded_text = decoded_bytes.decode("utf-8")

        return {
            "encoded": encoded_text,
            "decoded": decoded_text
        }

    except (binascii.Error, UnicodeDecodeError, ValueError):
        raise ValueError(
            "Invalid Base64 input or decoded content is not valid UTF-8 text."
        )
