from abc import ABC
from repositories.base_repository import Repository

from src.models import CoverLetter 

class CoverLetterRepository(Repository[CoverLetter, str], ABC):
    """Entity-specific repository interface for CoverLetters."""
    pass
