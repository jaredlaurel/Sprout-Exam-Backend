from abc import ABCMeta, abstractmethod
from typing import Tuple, Union


class BaseInterface(metaclass=ABCMeta):
    """
    Abstract class for Interfaces.
    """

    @abstractmethod
    async def create(self, data: dict) -> Union[None, dict]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, data: dict, id: Union[str, int]) -> Union[None, dict]:
        raise NotImplementedError()

    @abstractmethod
    async def get(self, id: Union[str, int]) -> Union[None, dict]:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, id: Union[str, int]) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list:
        raise NotImplementedError()

    @abstractmethod
    async def delete_all(self) -> bool:
        raise NotImplementedError()
