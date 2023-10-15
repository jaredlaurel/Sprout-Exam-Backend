from app.adapters.database.base.postgres import BaseQueries
from app.domain.employee.interface import EmployeeInterface


class EmployeeQueries(BaseQueries, EmployeeInterface):
    """
    Class for Employee Queries using Postgres

    Inherits:
        - BaseQueries (Base methods for Postgres)
        - EmployeeInterface (Base Class for Employees specifics Interface)
    """