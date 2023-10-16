import pytest
from tests.test_server import app, client

from app.api.v1.employee.helpers import EmployeeManagerContext
from app.domain.employee.schema import EmployeeDBSchema

from .mock import EMPLOYEE_SCHEMA, get_employee_manager_mock, test_id

app.dependency_overrides[EmployeeManagerContext.get_employee_manager] = get_employee_manager_mock


@pytest.fixture
def employee_schema() -> EmployeeDBSchema:
    return EMPLOYEE_SCHEMA


class TestEmployeeRouter:
    def test_create_employee(self, employee_schema: EmployeeDBSchema) -> None:

        response = client.post(
            "/api/v1/employee/",
            json={
                "first_name": "Test First Name",
                "last_name": "Test Last Name",
                "email": "test@test.com",
                "number_of_leaves": 15,
                "benefits": "Test Benefits",
                "type": "Regular"
            },
        )
        assert response.status_code == 200

        data = response.json()
        assert EmployeeDBSchema(**data).id == employee_schema.id

    def test_update_employee(self) -> None:

        response = client.put(
            f"/api/v1/employee/{test_id}",
            json={
                "first_name": "Test First Name EDIT",
                "last_name": "Test Last Name EDIT",
                "email": "test@test.com",
                "number_of_leaves": 10,
                "benefits": "Test Benefits EDIT",
                "type": "Regular"
            },
        )
        assert response.status_code == 200
        assert response.json()

    def test_list_employees(self, employee_schema: EmployeeDBSchema) -> None:

        response = client.get("/api/v1/employee/all")
        data = response.json()
        assert response.status_code == 200
        assert len(data["data"]) > 0
        assert EmployeeDBSchema(**data["data"][0]).id == employee_schema.id

    def test_remove_employee(self) -> None:

        response = client.delete(f"/api/v1/employee/{test_id}")
        assert response.status_code == 200
        assert response.json()

    def test_get_employee_by_id(self, employee_schema: EmployeeDBSchema) -> None:

        response = client.get(f"/api/v1/employee/{test_id}")
        data = response.json()
        assert response.status_code == 200
        assert EmployeeDBSchema(**data).id == employee_schema.id
