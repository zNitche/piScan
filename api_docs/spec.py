from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from configs.config import Config

spec = APISpec(
    title="piScan",
    version="1.0.0",
    openapi_version="3.0.2",
    info={"description": "API for piScan system"},
    servers=[{"url": url} for url in Config.SWAGGER_SERVERS.split(",")] if
    Config.SWAGGER_SERVERS else [{"url": "http://127.0.0.1:8000"}],

    plugins=[MarshmallowPlugin()]
)
