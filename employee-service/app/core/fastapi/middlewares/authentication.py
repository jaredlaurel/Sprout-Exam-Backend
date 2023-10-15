import os
import random
from typing import Optional, Tuple

from pydantic import BaseModel, Field
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)
from starlette.requests import HTTPConnection


class CurrentUser(BaseModel):
    id: int = Field(None, description="ID")

    class Config:
        validate_assignment = True


class AuthBackend(AuthenticationBackend):
    async def authenticate(
        self,
        conn: HTTPConnection,
    ) -> Tuple[bool, Optional[CurrentUser]]:
        current_user = CurrentUser()
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user

        if authorization != os.getenv("API_KEY"):
            return False, current_user

        current_user.id = random.randint(0, 10)
        return True, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass
