import re
import responses
import uuid
import random


def random_str() -> str:
    return uuid.uuid4().hex


def random_int() -> int:
    return random.randint(1, 100000000)


def mock_http_response(
    method, uri, body_data, http_status=200, headers=None, response_data=""
):
    if headers is None:
        headers = {}

    def decorator(fn):
        @responses.activate
        def wrapper(*args, **kwargs):
            responses.add(
                method,
                re.compile(".*" + uri),
                json=body_data,
                status=http_status,
                headers=headers,
            )
            return fn(*args, **kwargs)

        return wrapper

    return decorator
