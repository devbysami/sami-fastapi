# FastAPI PostgreSQL Project

This project demonstrates how to build a RESTful API using **FastAPI** with a **PostgreSQL** database. It includes basic **CRUD operations** for managing items and demonstrates how to interact with the PostgreSQL database using **SQLAlchemy**.

## Features
- FastAPI-based RESTful API for managing items.
- PostgreSQL database integration.
- CRUD operations (Create, Read, Update, Delete).
- Pydantic models for data validation and serialization.
- SQLAlchemy for database interaction.

## Project Structure
sami-fastapi/
├── init.py
├── auth.py # Authentication logic (if applicable)
├── curd.py # CRUD operations (PostgreSQL specific)
├── database.py # PostgreSQL database connection
├── main.py # FastAPI entry point, includes routers
├── models/
│ └── item.py # SQLAlchemy models for PostgreSQL
├── routers/
│ └── item_router.py # Router to handle item-related API routes
├── schemas/ # Pydantic models for request/response validation
└── requirements.txt # Python dependencies (FastAPI, SQLAlchemy, psycopg2)

## Prerequisites

- **Python 3.7+**: Ensure Python is installed on your machine.
- **PostgreSQL**: The application connects to a PostgreSQL instance. You can install PostgreSQL locally or use a cloud provider like **Heroku** or **ElephantSQL**.
- **Dependencies**: The necessary Python libraries are listed in `requirements.txt`.

## Setup

### 1. Clone the repository
Start by cloning the repository to your local machine.

```bash
https://github.com/devbysami/sami-fastapi.git
cd sami-fastapi
pip install -r requirements.txt
uvicorn sami-fastapi.main:app --reload
