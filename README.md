# InsightHub

**A Python database application built with PostgreSQL and SQLAlchemy ORM.**

InsightHub is a command-line application for managing users, user profiles, documents, and tags. It demonstrates relational database design, SQLAlchemy ORM, database relationships, transaction management, and database operations using Python.

## Features

- **User Management**
  - Create new users
  - List all users
  - Search users by name
  - Edit user profile information
  - Delete users

- **Document Management**
  - Search documents by keyword
  - Search document titles and content
  - Retrieve documents with pagination

- **Tag Management**
  - Create and store tags
  - Define relationships between documents and tags

- **Database Integration**
  - PostgreSQL database
  - SQLAlchemy ORM
  - Foreign key constraints
  - Database transactions
  - Automatic transaction commit and rollback using transaction contexts

## Technologies

- Python
- PostgreSQL
- SQLAlchemy ORM
- Psycopg
- python-dotenv
- Git and GitHub

## Project Structure

```text
insighthub-sqlalchemy/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── user_profile.py
│   │   ├── document.py
│   │   ├── document_tag.py
│   │   └── tag.py
│   │
│   └── services/
│       ├── user_service.py
│       ├── document_service.py
│       └── tag_service.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

*Note: The structure above shows the main project files. Additional files may exist in the repository.*

## Database Design

The application uses a relational database with the following tables:

| Table | Purpose |
|---|---|
| `users` | Stores user account information |
| `user_profiles` | Stores additional user profile information |
| `document` | Stores documents and their content |
| `tags` | Stores reusable tags |
| `document_tags` | Connects documents and tags through a many-to-many relationship |

### Relationships

- A user can have a profile containing additional information.
- A user can own multiple documents.
- A document can have multiple tags.
- A tag can be associated with multiple documents.
- Foreign key constraints maintain referential integrity.
- `ON DELETE CASCADE` is used for selected relationships to remove dependent records when their referenced records are deleted.

## Requirements

Before running the application, make sure you have installed:

- Python 3.10 or later
- PostgreSQL
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aliimdev/insighthub-sqlalchemy.git
cd insighthub-sqlalchemy
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, install the dependencies with:

```bash
pip install sqlalchemy "psycopg[binary]" python-dotenv
```

## Database Configuration

### 1. Create the database

Open PostgreSQL and create a database for the project:

```sql
CREATE DATABASE insighthub;
```

### 2. Configure environment variables

Create a `.env` file in the project root directory.

Add your PostgreSQL connection string:

```env
DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@localhost:5432/insighthub
```

Replace `USERNAME` and `PASSWORD` with your PostgreSQL credentials.

**Security:** Never commit your `.env` file or expose database credentials in your source code. Keep `.env` in `.gitignore` and provide placeholders in `.env.example`.

### 3. Create the database tables

Create the required tables and constraints in PostgreSQL before running the application. Use the project's database schema SQL, if provided, or the corresponding table definitions from your database setup.

Make sure the table names and foreign key references match the SQLAlchemy models.

## Run the Application

From the project root, execute:

```bash
python main.py
```

The application displays a command-line menu similar to:

```text
==== InsightHub ====
1) Insert a new user
2) List users
3) Search user by name
4) Edit a user
5) Delete a user
6) Add a tag
7) List documents
8) Exit
```

Enter the corresponding number to select an operation.

## Application Architecture

The project separates database configuration, ORM models, and application services.

### Models

The `app/models/` package defines the database tables, columns, foreign keys, and ORM relationships.

### Services

The `app/services/` package contains the application logic for working with users, documents, and tags. Keeping this logic separate from the command-line interface makes the code easier to maintain and test.

### Database Configuration

The `app/database.py` module manages the database engine, SQLAlchemy session factory, and declarative base class.

### Main Application

The `main.py` file provides the command-line interface and connects user input to the appropriate service functions.

## Learning Objectives

This project demonstrates practical experience with:

- Relational database design
- PostgreSQL and SQL
- SQLAlchemy ORM models
- One-to-one, one-to-many, and many-to-many relationships
- Primary keys and foreign keys
- Database constraints and cascading deletes
- CRUD operations
- Search queries using SQLAlchemy
- Database transactions and session management
- Python project organization
- Environment variable configuration
- Git version control

## Future Improvements

Potential improvements include:

- Automated tests with pytest
- Input validation and improved error handling
- Document creation, editing, and deletion
- More advanced search and filtering
- Database migrations with Alembic
- A REST API using FastAPI
- Logging and improved application documentation

## Author

**Ali Mazaheri**

GitHub: [@aliimdev](https://github.com/aliimdev)

## License

A license has not yet been specified. Add a `LICENSE` file if you intend to distribute this project under an open-source license.
