## Updated Class Diagram

```mermaid
classDiagram
    class UserSession {
        -sessionId: String
        -tone: String
        +setTone(tone: String) void
        +initiateGeneration() void
        +clearSession() void
    }

    class APIKey {
        -keyString: String
        -isValid: Boolean
        +validate() Boolean
        +mask() String
        +clear() void
    }

    class JobDescription {
        -text: String
        -maxLimit: Integer = 3000
        +validateLength() Boolean
        +getText() String
    }

    class Resume {
        -text: String
        -maxLimit: Integer = 6000
        +validateLength() Boolean
        +getText() String
    }

    class CoverLetter {
        -id: String
        -content: String
        -status: String
        -templateVersion: String
        +updateContent(newContent: String) void
        +copyToClipboard() Boolean
    }

    class AIGenerationService {
        -endpoint: String
        -timeout: Integer
        +compilePrompt(resume: Resume, jd: JobDescription, tone: String) String
        +callExternalAPI(prompt: String, key: APIKey) Response
        +parseResponse() CoverLetter
    }

    class SystemLog {
        -timestamp: DateTime
        -status: Integer
        -latency: Integer
        -errorType: String
        +sanitizeData() void
        +writeLog() void
    }

    class Repository {
        <<interface>>
        +save(entity: T) void
        +find_by_id(id: ID) Optional~T~
        +find_all() List~T~
        +delete(id: ID) void
    }

    class CoverLetterRepository {
        <<interface>>
    }

    class InMemoryCoverLetterRepository {
        -_storage: Dict
        +save(cover_letter: CoverLetter) void
        +find_by_id(id: String) Optional~CoverLetter~
        +find_all() List~CoverLetter~
        +delete(id: String) void
    }

    class FileSystemCoverLetterRepository {
        -_file_path: String
        +save(cover_letter: CoverLetter) void
        +find_by_id(id: String) Optional~CoverLetter~
        +find_all() List~CoverLetter~
        +delete(id: String) void
    }

    class RepositoryFactory {
        +get_cover_letter_repository(storage_type: String) CoverLetterRepository
    }

    %% Domain Model Relationships
    UserSession "1" *-- "1" JobDescription : contains
    UserSession "1" *-- "1" Resume : contains
    UserSession "1" o-- "1" APIKey : authenticates with
    UserSession "1" -- "0..*" CoverLetter : reviews
    UserSession "1" ..> "1" AIGenerationService : requests
    AIGenerationService "1" ..> "1" CoverLetter : creates
    AIGenerationService "1" -- "1" SystemLog : writes

    %% Persistence Layer Relationships
    CoverLetterRepository --|> Repository : extends
    InMemoryCoverLetterRepository --|> CoverLetterRepository : implements
    FileSystemCoverLetterRepository --|> CoverLetterRepository : implements
    RepositoryFactory ..> CoverLetterRepository : creates
    CoverLetterRepository "1" -- "0..*" CoverLetter : manages
  ```