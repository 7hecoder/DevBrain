from constants.hash import HASH_FUNCTIONS


def generate_hash(text: str, algorithm: str) -> str:

    hash_function = HASH_FUNCTIONS[algorithm.lower()]

    return hash_function(
        text.encode("utf-8")
    ).hexdigest()
