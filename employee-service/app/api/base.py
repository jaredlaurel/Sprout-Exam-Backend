from fastapi import APIRouter, Depends
from fastapi_redis_cache import cache


from app.api.v1 import employee

from app.core import config
from app.core.fastapi.dependencies import IsAuthenticated, PermissionDependency

# Initialize api router
api_router = APIRouter(prefix="/api/v1")


# Include routers
api_router.include_router(
    employee.router,
    prefix="/employee",
    tags=["employee"],
    # dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
@api_router.get("/health-check")
@cache()  # Will be cached indefinitely
def health_check():
    """
    Health checkpoint of current app status and version
    """
    response = {
        "status": "Online",
        "app_name": config.PROJECT_NAME,
        "environment": config.ENV,
        "version": config.APP_VERSION,
    }
    return response