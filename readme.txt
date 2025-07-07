FastAPI User Management App

----Technologies Used
This project uses the following key technologies and libraries:

    FastAPI
    A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
    Why: FastAPI allows easy creation of RESTful APIs with automatic data validation, serialization, and interactive API documentation (Swagger UI).

    SQLAlchemy
    The Python SQL toolkit and Object Relational Mapper (ORM) used to interact with the database in an efficient, pythonic way.
    Why: SQLAlchemy abstracts away raw SQL and allows defining Python classes that map directly to database tables, making database operations easier and safer.

    SQLite
    A lightweight, serverless SQL database engine used here as the default development database.
    Why: SQLite is simple to set up (no separate server needed) and great for prototyping and small apps.

    Alembic
    A database migration tool for SQLAlchemy to manage changes to the database schema over time.
    Why: Alembic lets you version control your database schema and apply incremental changes (migrations) safely as your models evolve.

    Uvicorn
    A lightning-fast ASGI server used to run the FastAPI app.
    Why: Uvicorn is lightweight and supports asynchronous operations, enabling high-performance async APIs.

    Pydantic
    A data validation and parsing library used by FastAPI to define and enforce data schemas.
    Why: It ensures that incoming and outgoing data is validated and typed correctly, improving reliability and security of the API.

----What This App Does
This application manages user data — it allows you to:

    Create new users

    Retrieve existing users

    Update user details and passwords

    Delete users

All operations are performed via REST API endpoints that communicate with the SQLite database through SQLAlchemy models, ensuring clean, maintainable, and scalable code.

----Setup & Run
1. Activate the virtual environment
    Windows (PowerShell): venv\Scripts\Activate.ps1
    MacOS / Linux: source venv/bin/activate

2. Run the FastAPI app
With the virtual environment activated, run this command in your terminal:
    uvicorn main:app --reload
This starts the development server with auto-reload on code changes.

3. Open the app in your browser
    App URL: http://127.0.0.1:8000
    Interactive API docs (Swagger UI): http://127.0.0.1:8000/docs

4. Check installed dependency versions
Run:
    pip show fastapi
    pip show sqlalchemy