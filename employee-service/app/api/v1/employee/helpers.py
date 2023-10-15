from app.adapters.database.employee import EmployeeQueries
from app.domain.employee.manager import EmployeeManager


class EmployeeManagerContext:
    @staticmethod
    def get_employee_manager() -> EmployeeManager:
        return EmployeeManager(EmployeeQueries())
