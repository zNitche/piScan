from api_docs.spec import spec


TAG = "Scan Formats"
spec.tag({"name": TAG})


get_scan_formats = {
    "tags": [TAG],
    "summary": "Get Scan Formats",
    "responses": {
        "200": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": "ScanFormat"
                    }
                }
            }
        }
    }
}

create_scan_format = {
    "tags": [TAG],
    "summary": "Create Scan Format",
    "requestBody": {
        "content": {
            "application/json": {
                "schema": "ScanFormat"
            }
        }
    },
    "responses": {
        "201": {
            "description": "format successfully created"
        },
        "400": {
            "description": "error while creating scan format"
        }
    }
}


spec.path(
    path="/api/scan-formats",
    operations={
        "get": get_scan_formats,
        "post": create_scan_format,
    },
)

get_scan_format = {
    "tags": [TAG],
    "summary": "Get Scan Format by uuid",
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
                    "schema": "ScanFormat"
                }
            }
        },
        "404": {
            "description": "NOT FOUND"
        }
    }
}

remove_scan_format = {
    "tags": [TAG],
    "summary": "Delete Scan Format by uuid",
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
            "description": "Scan Format removed successfully"
        },
        "404": {
            "description": "NOT FOUND"
        }
    }
}

spec.path(
    path="/api/scan-formats/{uuid}",
    operations={
        "get": get_scan_format,
        "delete": remove_scan_format,
    },
)
