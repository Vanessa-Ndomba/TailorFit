from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(Generic[T, ID], ABC):
    """Generic repository interface defining standard CRUD operations."""
    
    @abstractmethod
    def save(self, entity: T) -> None:
        """Creates or updates an entity."""
        pass

    @abstractmethod
    def find_by_id(self, entity_id: ID) -> Optional[T]:
        """Reads a single entity by its ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """Reads all entities."""
        pass

    @abstractmethod
    def delete(self, entity_id: ID) -> None:
        """Deletes an entity by its ID."""
        pass
