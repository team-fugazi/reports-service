from datetime import datetime
from uuid import uuid4


def generate_meta(version: str = "v1"):
    return {
        "api-version": version,
        "request_timestamp": datetime.now(),
        "request_id": uuid4().hex,
    }
