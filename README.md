# Axsos_Boot_camp_project
Repository for bootcamp project in Django

---

## Task Manager Project Overview
Task Manager is a web application for managing daily tasks.  
It allows users to register, log in, and organize their tasks efficiently.  
The system provides CRUD operations, AJAX-based dynamic updates, responsive design, and deployment on AWS.
The system includes modular models for tasks, projects, and notes, allowing scalable task organization. 
Future scope includes adding smart features like task prioritization and productivity insights.

---

## Features
- User Authentication (Register, Login, Logout)
- Task Management (Create, Read, Update, Delete)
- Dashboard with task statistics (Completed vs Pending)
- AJAX integration for live search and dynamic updates
- Responsive design using Bootstrap
- RESTful API endpoint for tasks:
  - `GET /api/tasks` → Returns all tasks for the logged-in user
  - `POST /api/tasks` → Adds a new task
- Security: CSRF protection, input validation, password hashing
- Deployment on AWS (EC2 + MySQL RDS + Nginx + Gunicorn)
- Project Management (Create, Assign, View Projects)
- Notes on Tasks (Add contextual notes per task)
- Soft Delete & Archive (Trash view for deleted tasks)
- Task Prioritization (Low, Medium, High, Critical)
- Status Tracking (To Do, In Progress, Done, Archived)


---

## Tech Stack
- **Backend:** Django (Python)
- **Database:** MySQL
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **AJAX:** For dynamic updates
- **API:** RESTful endpoint for tasks

---

## Documentation
- GitHub Repo: [Axsos_Boot_camp_project](https://github.com/SuleimanAlqassem/Axsos_Boot_camp_project/)
- Trello Board: [Project Management](https://trello.com/u/suliemanalqassem/boards)

---

## ERD Diagram
**Entities:**
- **Project:** id, name, description, owner_id (FK → User), created_at, updated_at
- **User:** id, email, password, name, date_joined
- **Task:** id, title, description, status, owner_id (FK → User), created_at, updated_at
- **Note:** id, task_id (FK → Task), body, created_at

**Relationships:**
- User ↔ Project (1:N)
- Project ↔ Task (1:N)
- Task ↔ Note (1:N)


---

## Wireframes
- Login/Registration Page
- Dashboard (Summary of tasks)
- Task List (CRUD operations with AJAX search)
- Task Detail (Task info + dynamic updates)
- About Us Page
- Project Creation Page
- Note Addition Modal or Page
- Trash View (Archived/Deleted Tasks)


---

## Future Scope
- Task prioritization
- Reminders and productivity insights
- Integration with external APIs (e.g., calendar, notifications)
- Project-level analytics
- Tag-based filtering
- Multi-user collaboration (future)
- Calendar integration for due dates

