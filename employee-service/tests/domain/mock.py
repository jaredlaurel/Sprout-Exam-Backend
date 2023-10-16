import uuid

from app.adapters.database.employee import EmployeeQueries
from app.domain.employee.manager import EmployeeManager
from app.domain.employee.schema import EmployeeBaseSchema

test_id = uuid.uuid4()


EMPLOYEE_BASE_SCHEMA = EmployeeBaseSchema(
    first_name="Test First Name",
    last_name="Test Last Name",
    email="test@test.com",
    number_of_leaves=15,
    benefits="Test Benefits",
    type="Regular",
)


def get_employee_manager() -> EmployeeManager:
    return EmployeeManager(EmployeeQueries())
