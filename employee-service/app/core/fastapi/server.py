import datetime
import logging

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.base import api_router
from app.core.config import APP_VERSION, CORS_ORIGINS
from app.core.db import db
from app.core.exceptions import CustomException

LOGGER = logging.getLogger(__name__)


def init_cors(_app: FastAPI) -> None:
    cors_origins = [i.strip() for i in CORS_ORIGINS.split(",")]
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(_app: FastAPI) -> None:
    _app.include_router(api_router)


def init_listeners(_app: FastAPI) -> None:
    # Exception handler
    @_app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={
                "detail": [
                    {
                        "code": exc.error_code,
                        "message": exc.message,
                        "status": int(exc.code),
                        "path": str(request.url).replace(str(request.base_url), ""),
                        "timestamp": str(datetime.datetime.now()),
                        "detail": exc.message,
                    },
                ],
            },
        )


def on_auth_error(request: Request, exc: Exception):
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={
            "detail": [
                {
                    "code": error_code,
                    "message": message,
                    "status": status_code,
                    "path": str(request.url).replace(str(request.base_url), ""),
                    "timestamp": str(datetime.datetime.now()),
                    "detail": message,
                },
            ],
        },
    )


def init_database(_app: FastAPI) -> None:
    db.init_app(app=_app)


def create_app() -> FastAPI:
    try:
        LOGGER.info("Initiliase fast-API app")
        _app = FastAPI(
            title="employee_management",
            description="Employee Service",
            version=APP_VERSION,
        )
        init_routers(_app=_app)
        init_cors(_app=_app)
        init_listeners(_app=_app)
        init_database(_app=_app)
        return _app
    except Exception as e:
        LOGGER.error(f"Error in fast-API app initialisation => {e}")


app: FastAPI = create_app()

if __name__ == "__main__":
    uvicorn.run(app, log_level="debug", reload=True)
