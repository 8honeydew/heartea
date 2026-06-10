# Heartea Development Journal

## Phase 1

### What I Did
- Created repository
- Initialized Git
- Created project structure
- Set up Python virtual environment

### What I Learned
- Git initialization
- Repository structure
- Python virtual environments

### Questions
-

## Phase 2.1 — First Backend and Search System

### Features Built
- FastAPI backend
- Place and Review data models
- Search endpoint
- Automated testing setup

### Skills Learned
- FastAPI
- REST APIs
- Query parameters
- Pydantic models
- Python package imports
- pytest
- Git workflow

### Biggest Challenges
- Git branch initialization
- Python import resolution
- pytest package discovery
- use 'python -m pytest' instead of 'pytest'

### Key Takeaway
Building software = designing data structures, organizing projects correctly, and debugging environment issues.

## Interlude—Backend Foundations Review

### What I Did

* Created a separate learning workspace to study the Heartea codebase line-by-line:
* Learned about the FastAPI request flow from endpoint to response,
* the project structure and Python environment files,
* and the search logic, data models, and testing setup.

### Skills Learned

* FastAPI route decorators
* Query parameters
* JSON responses
* Python packages and imports
* Virtual environments
* Dependency management (`pip`, `requirements.txt`)
* Pydantic validation
* pytest configuration and test discovery

### Biggest Challenges

* Understanding Python project structure and syntax
* Distinguishing source code from generated files and caches
* Learning how imports and package paths are resolved

### Key Takeaway

Understanding frameworks, dependencies, testing tools, and project structure.

## Phase 2.2 — Experience Tags and Recommendation Ranking

### What I Did

- Added experience tags to the `Place` model
- Tagged places with attributes 
- Built a `/tag-search` endpoint
- Created experience profiles that group related tags into experiences
- Built a recommendation scoring system
- Added a `/recommend` endpoint that ranks places by experience match
- Added test for recommendation scoring

### Skills Learned

- Recommendation system fundamentals
- Ranking and scoring logic
- Type hints
- Python dictionaries as configuration data
- Sorting data by custom criteria
- Separating business logic into modules

### Biggest Challenges

- Deciding how experiences should be represented
- Understanding the difference between search and recommendation

### Key Takeaway

Search finds exact matches. Recommendation estimates how well something satisfies a user's goal. Experiences can be represented as combinations of smaller attributes and used to rank results.