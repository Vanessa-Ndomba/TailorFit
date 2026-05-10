import unittest
from repositories.inmemory.in_memory_cover_letter_repository import InMemoryCoverLetterRepository
from src.models import CoverLetter


class TestInMemoryCoverLetterRepository(unittest.TestCase):
    
    def setUp(self):
        """Initialize repository before each test."""
        self.repo = InMemoryCoverLetterRepository()
        self.test_letter = CoverLetter(
            id="letter_001",
            content="Dear Hiring Manager...",
            status="draft",
            template_version="v1.0"
        )
    
    # CREATE operation
    def test_save_new_cover_letter(self):
        """Test saving a new cover letter."""
        self.repo.save(self.test_letter)
        retrieved = self.repo.find_by_id("letter_001")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.content, "Dear Hiring Manager...")
    
    # READ operations
    def test_find_by_id_existing(self):
        """Test finding a cover letter by ID."""
        self.repo.save(self.test_letter)
        found = self.repo.find_by_id("letter_001")
        self.assertIsNotNone(found)
        self.assertEqual(found.id, "letter_001")
    
    def test_find_by_id_nonexistent(self):
        """Test finding a non-existent cover letter returns None."""
        found = self.repo.find_by_id("nonexistent")
        self.assertIsNone(found)
    
    def test_find_all_empty(self):
        """Test finding all when repository is empty."""
        all_letters = self.repo.find_all()
        self.assertEqual(len(all_letters), 0)
    
    def test_find_all_multiple(self):
        """Test finding all with multiple cover letters."""
        letter2 = CoverLetter(id="letter_002", content="Another letter", status="sent", template_version="v1.0")
        self.repo.save(self.test_letter)
        self.repo.save(letter2)
        all_letters = self.repo.find_all()
        self.assertEqual(len(all_letters), 2)
    
    # UPDATE operation
    def test_save_updates_existing(self):
        """Test that saving overwrites existing entry."""
        self.repo.save(self.test_letter)
        updated_letter = CoverLetter(id="letter_001", content="Updated content", status="sent", template_version="v2.0")
        self.repo.save(updated_letter)
        retrieved = self.repo.find_by_id("letter_001")
        self.assertEqual(retrieved.content, "Updated content")
        self.assertEqual(retrieved.status, "sent")
    
    # DELETE operation
    def test_delete_existing(self):
        """Test deleting an existing cover letter."""
        self.repo.save(self.test_letter)
        self.repo.delete("letter_001")
        found = self.repo.find_by_id("letter_001")
        self.assertIsNone(found)
    
    def test_delete_nonexistent(self):
        """Test deleting a non-existent letter doesn't raise error."""
        # Should not raise an exception
        self.repo.delete("nonexistent")


if __name__ == '__main__':
    unittest.main()