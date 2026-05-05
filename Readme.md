Lunch Decision API

A professional backend service designed to streamline lunch decisions for employees. This API allows restaurants to manage daily menus and enables users to vote for their preferred options with real-time result tracking.

---

Tech Stack
Runtime: Python 3.11+
Framework: Django 5.0 + Django REST Framework
Database: PostgreSQL
Auth: JWT (SimpleJWT)
Infrastructure: Docker & Docker Compose
Quality: Flake8 (PEP8) & Pytest

---

Architecture Highlights
JWT Security: All internal endpoints are protected via JSON Web Tokens.
API Versioning: Flexible version management via the `X-Build-Version` custom header.
Data Integrity: Strict database constraints ensure the "one employee — one vote per day" rule.
Optimized ORM: Utilizing `annotate()` and `Count()` for high-performance real-time leaderboards.

---

Deployment & Setup
1. Prerequisites
Ensure you have **Docker** and **Docker Compose** installed. Create a `.env` file in the root directory based on the provided template.
2. Quick Start
Build and launch the entire infrastructure (API + PostgreSQL) with a single command in Terminal:

    docker-compose up --build

The service will be available at: http://localhost:8000/

3. Administrative Setup
Create a superuser to manage restaurants and menus via the Django Admin panel:
    
    docker-compose exec web python manage.py createsuperuser

Running Tests run command:

    docker-compose exec web pytest

Static Analysis (Linter) run command:

    flake8 .

---

Key API Endpoints

Authentication:

POST	/api/token/   Obtain Access & Refresh tokens ||
POST  /api/register/    Register a new employee account ||

Core Services

GET	  /api/menu/today/	  List all menus available for the current date ||
POST	/api/vote/	  Submit a vote for a specific restaurant menu ||
GET	  /api/results/   Real-time voting leaderboard ||

---

Versioning

To access version-specific logic, include the following header in your requests:
X-Build-Version: 2.0
