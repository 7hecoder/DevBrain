
from datetime import datetime, UTC


def convert_timestamp(timestamp: float):
    try:
        dt = datetime.fromtimestamp(timestamp, UTC)

        return {
            "timestamp": timestamp,
            "timestamp_ms": int(timestamp * 1000),
            "utc": dt.isoformat(),
            "date": dt.strftime("%Y-%m-%d"),
            "time": dt.strftime("%H:%M:%S"),
            "year": dt.year,
            "month": dt.month,
            "day": dt.day,
            "hour": dt.hour,
            "minute": dt.minute,
            "second": dt.second,
            "weekday": dt.strftime("%A"),
        }

    except (OverflowError, OSError, ValueError) as error:
        raise ValueError("Invalid timestamp.") from error
