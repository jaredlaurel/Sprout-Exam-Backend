from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.base import api_router
from app.core.fastapi.middlewares import AuthBackend, AuthenticationMiddleware


def init_middleware(_app: FastAPI) -> None:
    _app.add_middleware(
        AuthenticationMiddleware,
        backend=AuthBackend(),
    )


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    init_middleware(app)

    return app


app = create_test_app()
client = TestClient(app)
