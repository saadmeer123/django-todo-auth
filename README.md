# Django Todo Project with Auth

A simple **Django Todo application** featuring user authentication, CRUD operations, and task search. Each user can manage their own tasks securely.

---

## Features

- User Signup & Login (Auth)
- CRUD operations for tasks
- Task search functionality
- User-specific task view
- Logout

---

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
Clone the repository:

bash
Copy code
git clone https://github.com/saadmeer123/django-todo-auth.git
cd django-todo-auth
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Open the browser at http://127.0.0.1:8000/.

Usage
Signup as a new user or login.

Create, update, delete, or search tasks.

Logout when done.

Notes
Each user sees only their own tasks.

The project uses SQLite by default but can be switched to PostgreSQL.

Designed for learning Django Auth & CRUD patterns.

License
This project is open-source and free to use.

pgsql
Copy code

This format will render **Mermaid diagrams correctly** on GitHub, and the instructions are clear for anyone to follow.  

If you want, I can also add **screenshots + badges** for a more “professional” GitHub README look.  

Do you want me to do that next?
Edit or delete your tasks as needed.
