from abc import ABC, abstractclassmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractclassmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """ " abstractmethod"""

        raise Exception("Method not implemented")

    @abstractclassmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """ " abstractmethod"""

        raise Exception("Method not implemented")
