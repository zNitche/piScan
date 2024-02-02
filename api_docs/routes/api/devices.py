from api_docs.spec import spec


spec.tag({"name": "Devices"})


get_devices = {
    "tags": ["Devices"],
    "summary": "Get Devices",
    "responses": {
        "200": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": "Device"
                    }
                }
            }
        }
    }
}

create_device = {
    "tags": ["Devices"],
    "summary": "Create device",
    "requestBody": {
        "content": {
            "application/json": {
                "schema": "Device"
            }
        }
    },
    "responses": {
        "201": {
            "description": "device successfully created"
        },
        "400": {
            "description": "error while creating device"
        }
    }
}


spec.path(
    path="/api/devices",
    operations={
        "get": get_devices,
        "post": create_device,
    },
)

get_device = {
    "tags": ["Devices"],
    "summary": "Get device by uuid",
    "parameters": [
        {
            "in": "path",
            "name": "uuid",
            "schema": {
                "type": "string"
            }
        }
    ],
    "responses": {
        "200": {
            "content": {
                "application/json": {
                    "schema": "Device"
                }
            }
        },
        "404": {
            "description": "NOT FOUND"
        }
    }
}

remove_device = {
    "tags": ["Devices"],
    "summary": "Delete device by uuid",
    "parameters": [
        {
            "in": "path",
            "name": "uuid",
            "schema": {
                "type": "string"
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Device removed successfully"
        },
        "404": {
            "description": "NOT FOUND"
        }
    }
}

spec.path(
    path="/api/devices/{uuid}",
    operations={
        "get": get_device,
        "delete": remove_device,
    },
)
