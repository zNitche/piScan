from api_docs.spec import spec

TAG = "Core"
spec.tag({"name": TAG})

health_check = {
    "tags": [TAG],
    "summary": "Check if service is available",
    "responses": {
        "200": {
            "description": "ok"
        }
    }
}

spec.path(
    path="/health-check",
    operations={
        "get": health_check
    },
)
