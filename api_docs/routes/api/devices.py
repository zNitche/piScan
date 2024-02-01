from api_docs.spec import spec

spec.path(
    path="/api/devices",
    operations=dict(
        get=dict(
            responses={
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
        )
    ),
)
