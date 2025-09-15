# Django Todo Project with Auth

## Overview
This is a **Todo web application** built with Django that includes user authentication (signup, login, logout) and CRUD functionality for tasks. Each user can manage their own tasks securely.

![Todo App Screenshot](images/todo_home.png)

## Features
- ✅ User signup, login, logout
- ✅ Create, read, update, delete (CRUD) tasks
- ✅ Search tasks by title or status
- ✅ Tasks linked to logged-in users
- ✅ Simple and clean UI (HTML templates)

## Tech Stack
- Python 3.x
- Django 5.x
- SQLite (default) / PostgreSQL (optional)
- HTML, CSS

## Workflow Diagram

```mermaid
flowchart LR
    A[Signup / Login] --> B[User Authenticated]
    B --> C[View All Tasks]
    C --> D[Create Task]
    C --> E[Update Task]
    C --> F[Delete Task]
    C --> G[Search Task]
    B --> H[Logout]
Setup Instructions
Clone the repository

bash
Copy code
git clone https://github.com/saadmeer123/django-todo-auth.git
cd django-todo-auth
Create a virtual environment

bash
Copy code
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / Mac
Install dependencies

bash
Copy code
pip install -r requirements.txt
Apply migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create superuser (for admin)

bash
Copy code
python manage.py createsuperuser
Run the development server

bash
Copy code
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.

Usage
Signup to create an account.

Login to view and manage your tasks.

Search tasks using the search bar.

Edit or delete your tasks as needed.
