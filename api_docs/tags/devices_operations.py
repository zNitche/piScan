from api_docs.spec import spec

TAG = "Devices Operations"
spec.tag({"name": TAG})


device_health_check = {
    "tags": [TAG],
    "summary": "Check if device is available",
    "parameters": [
        {
            "in": "path",
            "name": "uuid",
            "schema": {
                "type": "string"
            }
        },
    ],
    "responses": {
        "200": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "is_available": {
                                "type": "boolean"
                            }
                        }
                    }
                }
            }
        },
        "404": {
            "description": "device not not found"
        }
    }
}

spec.path(
    path="/api/devices/{uuid}/health-check",
    operations={
        "get": device_health_check
    },
)

perform_scan = {
    "tags": [TAG],
    "summary": "Perform scan",
    "parameters": [
        {
            "in": "path",
            "name": "uuid",
            "schema": {
                "type": "string"
            }
        },
    ],
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "resolution": {
                            "type": "number"
                        },
                        "extension": {
                            "type": "string"
                        },
                    }
                }
            }
        }
    },
    "responses": {
        "200": {
            "description": "ok"
        },
        "404": {
            "description": "device not not found"
        }
    }
}

spec.path(
    path="/api/devices/{uuid}/scan",
    operations={
        "post": perform_scan
    },
)
