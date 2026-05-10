import json
from typing import Optional, List
from repositories.cover_letter_repository import CoverLetterRepository
from src.models import CoverLetter

class FileSystemCoverLetterRepository(CoverLetterRepository):
    """Stub implementation for future JSON file-system storage."""
    
    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, cover_letter: CoverLetter) -> None:
        raise NotImplementedError("Filesystem save operation is pending implementation.")

    def find_by_id(self, entity_id: str) -> Optional[CoverLetter]:
        raise NotImplementedError("Filesystem read operation is pending implementation.")

    def find_all(self) -> List[CoverLetter]:
        raise NotImplementedError("Filesystem read-all operation is pending implementation.")

    def delete(self, entity_id: str) -> None:
        raise NotImplementedError("Filesystem delete operation is pending implementation.")