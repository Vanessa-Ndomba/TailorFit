from repositories.cover_letter_repository import CoverLetterRepository
from repositories.inmemory.in_memory_cover_letter_repository import InMemoryCoverLetterRepository
from repositories.filesystem.file_system_cover_letter_repository import FileSystemCoverLetterRepository

class RepositoryFactory:
    """Factory to abstract and instantiate the correct storage backend."""
    
    @staticmethod
    def get_cover_letter_repository(storage_type: str) -> CoverLetterRepository:
        if storage_type == "MEMORY":
            return InMemoryCoverLetterRepository()
        elif storage_type == "FILESYSTEM":
            # Future implementation stub
            return FileSystemCoverLetterRepository("data/cover_letters.json")
        else:
            raise ValueError(f"Invalid storage type provided: {storage_type}")