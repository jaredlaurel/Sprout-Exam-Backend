from datetime import date, datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.utils.base_schema import PaginateModel


class EmployeeBaseSchema(BaseModel):
    """
    Class for Employee Base Schema
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    number_of_leaves: Optional[int] = None
    benefits: Optional[str] = None
    type: Optional[str] = None
    contract_end_date: Optional[date] = None
    project: Optional[str] = None

    class Config:
        orm_mode = True


class EmployeeDBSchema(EmployeeBaseSchema):
    id: Optional[UUID] = None
    created_at: datetime = datetime.utcnow()
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class EmployeePaginationSchema(BaseModel):
    data: List[EmployeeDBSchema]