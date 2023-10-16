from typing import List, Optional

from fastapi import APIRouter, Depends, Request

from app.api.v1.employee.helpers import EmployeeManagerContext
from app.core.exceptions import NotFoundException
from app.domain.employee.manager import EmployeeManager
from app.domain.employee.schema import (
    EmployeeBaseSchema,
    EmployeeDBSchema,
    EmployeePaginationSchema,
)
from app.utils.base_schema import ResponseModel

router = APIRouter()


@router.post("/", response_model=ResponseModel)
async def create_employee(
    employee: EmployeeBaseSchema,
    employee_manager: EmployeeManager = Depends(
        EmployeeManagerContext.get_employee_manager
    ),
) -> ResponseModel:
    create = await employee_manager.create_employee(employee)
    if create:
        return ResponseModel(
            **{
                "id": str(create),
                "success": True,
                "message": "Employee successfully created.",
            }
        )

    return ResponseModel(
        **{
            "id": str(create.id),
            "success": False,
            "message": "Employee failed to create.",
        }
    )


@router.get("/all", response_model=EmployeePaginationSchema)
async def list_employees(
    request: Request,
    employee_manager: EmployeeManager = Depends(
        EmployeeManagerContext.get_employee_manager
    ),
) -> EmployeePaginationSchema:
    employees, total = await employee_manager.list_employees()

    return EmployeePaginationSchema(**{"data": employees})


@router.get("/{employee_id}", response_model=EmployeeDBSchema)
async def get_employee_by_id(
    employee_id: str,
    employee_manager: EmployeeManager = Depends(
        EmployeeManagerContext.get_employee_manager
    ),
) -> Optional[EmployeeDBSchema]:
    employee = await employee_manager.get_employee_by_id(employee_id)
    if employee:
        return employee
    raise NotFoundException(
        f"Employee with id:{employee_id} not found"
    )  # pragma: no cover


@router.put("/{employee_id}", response_model=ResponseModel)
async def update_employee(
    employee_id: str,
    new_employee: EmployeeBaseSchema,
    employee_manager: EmployeeManager = Depends(
        EmployeeManagerContext.get_employee_manager
    ),
) -> ResponseModel:
    employee_updated = await employee_manager.update_employee(employee_id, new_employee)
    if employee_updated:
        return ResponseModel(
            **{
                "id": employee_id,
                "success": True,
                "message": "Employee successfully updated.",
            }
        )

    return ResponseModel(
        **{"id": employee_id, "success": False, "message": "Employee failed to update."}
    )


@router.delete("/{employee_id}", response_model=ResponseModel)
async def remove_employee(
    employee_id: str,
    employee_manager: EmployeeManager = Depends(
        EmployeeManagerContext.get_employee_manager
    ),
) -> ResponseModel:
    employee_removed = await employee_manager.remove_employee(employee_id)

    if employee_removed:
        return ResponseModel(
            **{
                "id": employee_id,
                "success": True,
                "message": "Employee successfully deleted.",
            }
        )

    return ResponseModel(
        **{"id": employee_id, "success": False, "message": "Employee failed to delete."}
    )
