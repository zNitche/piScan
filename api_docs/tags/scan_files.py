from api_docs.spec import spec

TAG = "Scan Files"
spec.tag({"name": TAG})

get_scan_files = {
    "tags": [TAG],
    "summary": "Get Scan Files",
    "responses": {
        "200": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": "ScanFile"
                    }
                }
            }
        }
    }
}

spec.path(
    path="/api/scan-files",
    operations={
        "get": get_scan_files,
    },
)

get_scan_file = {
    "tags": [TAG],
    "summary": "Get Scan File by uuid",
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
                    "schema": "ScanFile"
                }
            }
        },
        "404": {
            "description": "NOT FOUND"
        }
    }
}

remove_scan_file = {
    "tags": [TAG],
    "summary": "Delete Scan File by uuid",
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
            "description": "Scan File removed successfully"
        },
        "404": {
            "description": "NOT FOUND"
        }
    }
}

update_scan_file = {
    "tags": [TAG],
    "summary": "update Scan File",
    "parameters": [
        {
            "in": "path",
            "name": "uuid",
            "schema": {
                "type": "string"
            }
        }
    ],
    "requestBody": {
        "content": {
            "application/json": {
                "schema": "ScanFile"
            }
        }
    },
    "responses": {
        "200": {
            "description": "file successfully updated"
        },
        "400": {
            "description": "error while updating scan file"
        }
    }
}

spec.path(
    path="/api/scan-files/{uuid}",
    operations={
        "get": get_scan_file,
        "put": update_scan_file,
        "delete": remove_scan_file,
    },
)


download_scan_file = {
    "tags": [TAG],
    "summary": "Download Scan File by uuid",
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
        "200": {},
        "404": {
            "description": "NOT FOUND"
        }
    }
}


spec.path(
    path="/api/scan-files/{uuid}/download",
    operations={
        "get": download_scan_file
    },
)

scan_file_preview = {
    "tags": [TAG],
    "summary": "Preview Scan File by uuid",
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
        "200": {},
        "404": {
            "description": "NOT FOUND"
        }
    }
}


spec.path(
    path="/api/scan-files/{uuid}/preview",
    operations={
        "get": scan_file_preview
    },
)
