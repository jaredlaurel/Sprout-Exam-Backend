import uuid
from datetime import datetime
from typing import Any, List, Tuple

from app.domain.employee.schema import EmployeeDBSchema

test_id = uuid.uuid4()

EMPLOYEE_SCHEMA = EmployeeDBSchema(
    id=test_id,
    created=datetime.utcnow(),
    first_name="Test First Name",
    last_name="Test Last Name",
    email="test@test.com",
    number_of_leaves=15,
    benefits="Test Benefits",
    type="Regular"
)


class EmployeeManagerMock:
    async def create_employee(self, employee: Any) -> EmployeeDBSchema:
        return test_id

    async def list_employees(self) -> Tuple[List[EmployeeDBSchema], int]:
        return [EMPLOYEE_SCHEMA], 1

    async def get_employee_by_id(self, id: int) -> EmployeeDBSchema:
        return EMPLOYEE_SCHEMA

    async def update_employee(self, id: int, employee: Any) -> bool:
        return True

    async def remove_employee(self, id: int) -> bool:
        return True


def get_employee_manager_mock() -> EmployeeManagerMock:
    return EmployeeManagerMock()
