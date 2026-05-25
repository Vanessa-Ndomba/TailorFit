# TailorFit Development Roadmap

Welcome to the TailorFit roadmap! This document outlines the planned enhancements and future trajectory of the project. If you're looking to contribute, these are excellent areas to focus on (look for matching `feature request` labels in our issues!).

## Short-Term Goals (Next Release)
- **PDF and Word Parsing**: Move beyond plain-text inputs by allowing users to upload their `.pdf` or `.docx` resumes directly.
- **Enhanced Prompts**: Add more tone selections (e.g., "Aggressive", "Passionate", "Academic").
- **Persistent Storage Layer**: Implement an SQL database repository (e.g., PostgreSQL or SQLite) replacing the current In-Memory and FileSystem mechanisms.

## Medium-Term Goals
- **User Accounts & Authentication**: Add JWT-based user login to safely encrypt and store BYOK (Bring Your Own Key) credentials across sessions.
- **Redis Caching**: Implement Redis caching for frequently used system prompts to improve generation speed and lower redundant processing times.
- **UI Polish**: Transition the lightweight HTML/JS frontend into a modern React or Vue.js Single Page Application.

## Long-Term Vision
- **Browser Extension**: Build a Chrome/Firefox extension that auto-extracts job descriptions from platforms like LinkedIn or Indeed and auto-fills the TailorFit generation context.