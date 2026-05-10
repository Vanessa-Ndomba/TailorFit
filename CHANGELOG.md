# Changelog

All notable changes to this project will be documented in this file.

## Assignment 10 Updates

### Added
- Source Code (`/src`): Implemented core business models (`ApplicationSession`, `JobDescription`, `CoverLetterDraft`) based on Assignment Class Diagrams.
- Creational Patterns (`/creational_patterns`): 
  - `Simple Factory`: Added `DocumentFactory` for dynamically generating Document types.
  - `Factory Method`: Added `LLMProcessor` abstraction.
  - `Abstract Factory`: Added `PromptFactory` for Professional and Creative prompt generation.
  - `Builder`: Added `CoverLetterBuilder` for complex string/object building.
  - `Prototype`: Added `PromptCache` to clone expensive objects.
  - `Singleton`: Added thread-safe `DatabaseConnection`.
- Unit Tests (`/tests`): Extensive test suite covering creational object lifecycles, attribute initialisation, and edge cases.
- GitHub Activity: Moved issue #13 - #18 to done.

## Assignment 11 Updates

### Added
- Repository Interfaces (`/repositories`): 
  - `Repository[T, ID]` generic interface defining standard CRUD operations
  - `CoverLetterRepository` entity-specific interface extending the generic base
- In-Memory Implementation (`/repositories/inmemory`):
  - `InMemoryCoverLetterRepository` using Python Dictionary for transient storage
- Storage Abstraction (`/factories`):
  - `RepositoryFactory` using Factory Pattern to abstract storage backend selection
- Filesystem Stubs (`/repositories/filesystem`):
  - `FileSystemCoverLetterRepository` stub for future JSON file-based persistence
- Unit Tests (`/tests`):
  - `test_repositories.py` with comprehensive CRUD test coverage
- Code Diagram (`/docs`):
  - Updated the [Class Diagram](/assignment9/assignment9_models.md) to show repository and factory layers
      The updated class diagram is viewable here: [Class Diagram](/assignment11/Assignment_11_Updated_Class_Diagram.md)
### Changed
- `CoverLetter` model: Added `id` attribute for persistence identification

### Justification
- Used generics to eliminate duplication across entity repositories
- Factory Pattern chosen over DI to complement creational patterns from Assignment 10
- Design ensures easy addition of new backends (SQL, NoSQL, REST APIs) without affecting application services

---
