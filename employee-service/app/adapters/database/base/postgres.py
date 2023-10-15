from typing import Dict, List, Union

from app.adapters.database.models.employee import EmployeeModel
from app.domain.base_interface import BaseInterface


class BaseQueries(BaseInterface):
    """
    Class for Base Queries using Postgres

    """

    async def create(self, data: dict):
        """Create Query

        Args:
            data (dict): Data object to be created

        Returns:
            Postgres Result
        """
        data = await EmployeeModel.create(**data)
        if data:
            return data.id
        return None

    async def update(self, id: str, new_data: dict) -> Union[bool, None]:
        """Update Query

        Args:
            id (dict): id to be updated
            new_data (dict): Data object to be update

        Returns:
            bool|str : Postgres Result
        """
        result = await EmployeeModel.query.where(EmployeeModel.id == id).gino.first()
        if result:
            await result.update(**new_data).apply()
            return result
        return None

    async def delete(self, id: str) -> Union[bool, None]:
        """Delete Query

        Args:
            id (str): ID of document to be deleted

        Returns:
            bool|str : Postgres Result
        """
        result = await EmployeeModel.query.where(EmployeeModel.id == id).gino.first()
        if result:
            await result.delete()
            return result
        return None

    async def get(self, id: str) -> Union[Dict, None]:
        """Get Query

        Args:
            id (str): ID of document

        Returns:
            Union[Dict, None]: Postgres Result
        """
        result = await EmployeeModel.query.where(EmployeeModel.id == id).gino.first()
        return result

    async def get_all(self) -> Union[List, None]:
        """Get All Query

        Returns:
            Union[List, None]: Postgres Result
        """
        result = await EmployeeModel.query.gino.all()
        return result, len(result)

    async def delete_all(self):
        """Delete Query"""
