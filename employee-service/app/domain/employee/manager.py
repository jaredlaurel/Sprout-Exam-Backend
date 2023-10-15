from typing import Any, List, Optional, Tuple
from uuid import uuid4

from app.domain.employee.schema import (
    EmployeeBaseSchema,
    EmployeeDBSchema,
)


class EmployeeManager:
    def __init__(self, db_queries: Any):
        self.__db_queries = db_queries

    async def create_employee(self, employee: EmployeeBaseSchema) -> EmployeeDBSchema:
        """Create Employee

        Args:
            employee (EmployeeBaseSchema): Employee object

        Returns:
            EmployeeDBSchema: Result
        """
        create = EmployeeDBSchema(**employee.dict())
        create.id = uuid4()
        id = await self.__db_queries.create(employee.dict())
        return id

    async def list_employees(self) -> Tuple[List[EmployeeDBSchema], int]:
        """List of Employees

        Returns:
            List[EmployeeDBSchema]: List of employees object
        """
        result, total = await self.__db_queries.get_all()
        if not result:
            return [], 0

        return [EmployeeDBSchema.from_orm(i) for i in result], total

    async def get_employee_by_id(self, employee_id: str) -> Optional[EmployeeDBSchema]:
        """Get Employee by ID

        Args:
            employee_id (str): Employee ID

        Returns:
            Optional[EmployeeDBSchema]: Employee object
        """
        result = await self.__db_queries.get(id=employee_id)
        return {} if not result else EmployeeDBSchema.from_orm(result)

    async def update_employee(self, employee_id: str, employee: EmployeeBaseSchema) -> bool:
        """Update employee

        Args:
            employee_id (str): Employee ID
            new_employee (EmployeeBaseSchema): Employee Object

        Returns:
            bool: True if success, False otherwise
        """
        current = await self.__db_queries.get(id=employee_id)
        if not current:
            return False

        result = await self.__db_queries.update(employee_id, employee.dict())
        return False if not result else True

    async def remove_employee(self, employee_id: str) -> bool:
        """Remove Employee

        Args:
            employee_id (str): Employee ID

        Returns:
            bool: True if success, False otherwise
        """
        result = await self.__db_queries.delete(id=employee_id)
        return False if not result else True
