# Axsos_Boot_camp_project
Repository for bootcamp project  in Django 

Task Manager
Project Overview
Task Manager is a web application for managing daily tasks.
It allows users to register, log in, and organize their tasks efficiently.
The system provides CRUD operations, AJAX-based dynamic updates, responsive design, and deployment on AWS.
Future scope includes adding smart features like task prioritization and productivity insights.

Features
User Authentication (Register, Login, Logout).
Task Management (Create, Read, Update, Delete).
Dashboard with task statistics (Completed vs Pending).
AJAX integration for live search and dynamic updates.
Responsive design using Bootstrap.
RESTful API endpoint for tasks:
GET /api/tasks → Returns all tasks for the logged-in user.
POST /api/tasks → Adds a new task.
Security: CSRF protection, input validation, password hashing.
Deployment on AWS (EC2 + MySQL RDS + Nginx + Gunicorn).
Tech Stack
Backend: Django (Python)
Database: MySQL
Frontend: HTML, CSS (Bootstrap), JavaScript
AJAX: For dynamic updates
API: RESTful endpoint for tasks
Documentation: GitHub repository with README and setup instructions
ERD Diagram
Entities:

User: id, email, password, name, date_joined
Task: id, title, description, status, owner_id (FK → User), created_at, updated_at
Note : id, task_id (FK → Task), body, created_at
Relationships:

User ↔ Task (1:N)
Task ↔ Note (1:N)
Wireframes
Login/Registration Page
Dashboard (Summary of tasks)
Task List (CRUD operations with AJAX search)
Task Detail (Task info + dynamic updates)
About Us Page
Project Management
GitHub Repo: [https://github.com/SuleimanAlqassem/Axsos_Boot_camp_project/]
Trello Board: [https://trello.com/u/suliemanalqassem/boards]
Future Scope
task prioritization
Reminders and productivity insights
Integration with external APIs (e.g., calendar, notifications)
