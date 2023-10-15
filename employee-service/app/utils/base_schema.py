from typing import Optional

from pydantic import BaseModel


def rstrip(string: str) -> str:
    return string.rstrip("_")


class PaginateModel(BaseModel):
    total: int = 0
    per_page: int = 0
    current_page: int = 0
    last_page: int = 0
    first_page_url: Optional[str] = None
    last_page_url: Optional[str] = None
    next_page_url: Optional[str] = None
    prev_page_url: Optional[str] = None
    path: Optional[str] = None
    from_: int = 0
    to: int = 0

    class Config:
        alias_generator = rstrip


class ResponseModel(BaseModel):
    success: bool
    message: str
    id: str
