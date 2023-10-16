from datetime import datetime
from unittest.mock import patch

import pytest
from app.adapters.database.models.employee import EmployeeModel

from .mock import EMPLOYEE_BASE_SCHEMA, get_employee_manager, test_id

pytestmark = pytest.mark.asyncio


class TestEmployeeManager:
    @patch("app.adapters.database.employee.EmployeeQueries.__init__")
    @patch("app.adapters.database.employee.EmployeeQueries.get")
    @patch("app.adapters.database.employee.EmployeeQueries.create")
    async def test_create_employee(self, create, get, init) -> None:
        init.return_value = None

        # Test Success
        create.return_value = test_id
        get.return_value = {"id": test_id}
        result = await get_employee_manager().create_employee(EMPLOYEE_BASE_SCHEMA)
        assert test_id == result

        # Test Failed
        create.return_value = 0
        result = await get_employee_manager().create_employee(EMPLOYEE_BASE_SCHEMA)
        assert not result

    @patch("app.adapters.database.employee.EmployeeQueries.__init__")
    @patch("app.adapters.database.employee.EmployeeQueries.get_all")
    async def test_list_employees(self, get_all, init) -> None:
        init.return_value = None

        # Test with Value
        get_all.return_value = [EmployeeModel(id=test_id, created_at=datetime.now())], 1
        result, total = await get_employee_manager().list_employees()
        assert total
        assert test_id == result[0].id

        # Test Empty
        get_all.return_value = [], 0
        result, total = await get_employee_manager().list_employees()
        assert not total
        assert not result

    @patch("app.adapters.database.employee.EmployeeQueries.__init__")
    @patch("app.adapters.database.employee.EmployeeQueries.get")
    async def test_get_employee_by_id(self, get, init) -> None:
        init.return_value = None

        # Test with Value
        get.return_value = EmployeeModel(id=test_id, created_at=datetime.now())
        result = await get_employee_manager().get_employee_by_id(employee_id=test_id)
        assert result
        assert test_id == result.id

        # Test Empty
        get.return_value = {}
        result = await get_employee_manager().get_employee_by_id(employee_id=test_id)
        assert not result

    @patch("app.adapters.database.employee.EmployeeQueries.__init__")
    @patch("app.adapters.database.employee.EmployeeQueries.get")
    @patch("app.adapters.database.employee.EmployeeQueries.update")
    async def test_update_employee(self, update, get, init) -> None:
        init.return_value = None

        # Test Success
        update.return_value = True
        get.return_value = {"id": test_id}
        result = await get_employee_manager().update_employee(
            test_id, EMPLOYEE_BASE_SCHEMA
        )
        assert result is True

        # Test Failed
        update.return_value = False
        result = await get_employee_manager().update_employee(
            test_id, EMPLOYEE_BASE_SCHEMA
        )
        assert result is False

    @patch("app.adapters.database.employee.EmployeeQueries.__init__")
    @patch("app.adapters.database.employee.EmployeeQueries.delete")
    async def test_remove_employee(self, delete, init) -> None:
        init.return_value = None

        # Test Success
        delete.return_value = True
        result = await get_employee_manager().remove_employee(test_id)
        assert result is True

        # Test Failed
        delete.return_value = False
        result = await get_employee_manager().remove_employee(test_id)
        assert result is False
