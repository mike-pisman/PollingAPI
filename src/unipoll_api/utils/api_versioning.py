from fastapi import APIRouter
from fastapi.openapi import utils
from unipoll_api.config import get_settings


# Get settings from configuration file
settings = get_settings()

# List of OpenAPI schemas for each version
openapi_schemas = {}


# Function to add API to the list of OpenAPI schemas
def add_api(router: APIRouter, version: int):
    openapi_schemas[version] = utils.get_openapi(title=settings.app_name,
                                                 version=settings.app_version,
                                                 routes=router.routes
                                                 )