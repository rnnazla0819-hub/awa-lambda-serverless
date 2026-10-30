import json
from datetime import datetime, timezone


def lambda_handler(event, context):
    """Return a small JSON greeting. Works with an API Gateway HTTP API (payload v2)."""
    params = event.get("queryStringParameters") or {}
    name = params.get("name") or "friend"

    body = {
        "message": f"Hello {name}! This response comes from AWS Lambda.",
        "time": datetime.now(timezone.utc).isoformat(),
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(body),
    }
