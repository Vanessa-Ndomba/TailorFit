from typing import Optional, List
from repositories.cover_letter_repository import CoverLetterRepository
from src.models import CoverLetter

class InMemoryCoverLetterRepository(CoverLetterRepository):
    """In-memory HashMap implementation of the CoverLetterRepository."""
    
    def __init__(self):
        self._storage = {}

    def save(self, cover_letter: CoverLetter) -> None:
        self._storage[cover_letter.id] = cover_letter

    def find_by_id(self, entity_id: str) -> Optional[CoverLetter]:
        return self._storage.get(entity_id)

    def find_all(self) -> List[CoverLetter]:
        return list(self._storage.values())

    def delete(self, entity_id: str) -> None:
        if entity_id in self._storage:
            del self._storage[entity_id]
