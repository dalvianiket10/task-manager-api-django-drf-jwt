# Task Manager API

## Overview

Task Manager API is a RESTful backend application developed using **Django** and **Django REST Framework (DRF)**. It allows authenticated users to manage their tasks securely using JWT authentication.

This project was developed as part of a Django Backend Intern Assessment.

---

## Features

* User Login using JWT Authentication
* Refresh Access Token
* Create Task
* View All Tasks
* View Task by ID
* Update Task
* Delete Task
* Role-Based Access Control (RBAC)
* Search Tasks
* Filter Tasks by Status
* Order Tasks
* Pagination

---

## Tech Stack

* Python 3
* Django
* Django REST Framework
* Simple JWT
* SQLite
* Postman

---

## Project Structure

```text
Codesis_Django_Task_Manager/
│
├── task_manager/
├── tasks/
├── postman/
│   └── Task Manager API Assignment.postman_collection.json
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/dalvianiket10/task-manager-api-django-drf-jwt.git
cd task-manager-api-django-drf-jwt
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env File

```text
SECRET_KEY=your_secret_key
DEBUG=True
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Server URL

```
http://127.0.0.1:8000/
```

---

# Authentication

## Login

**POST**

```
/api/token/
```

Example Request

```json
{
    "username": "aniket",
    "password": "your_password"
}
```

Response

```json
{
    "refresh": "...",
    "access": "..."
}
```

---

## Refresh Token

**POST**

```
/api/token/refresh/
```

Example Request

```json
{
    "refresh": "your_refresh_token"
}
```

Response

```json
{
    "access": "new_access_token"
}
```

---

# API Endpoints

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/token/`         | Login                |
| POST   | `/api/token/refresh/` | Refresh Access Token |
| GET    | `/api/tasks/`         | Get All Tasks        |
| POST   | `/api/tasks/`         | Create Task          |
| GET    | `/api/tasks/<id>/`    | Get Task by ID       |
| PUT    | `/api/tasks/<id>/`    | Update Task          |
| DELETE | `/api/tasks/<id>/`    | Delete Task          |

---

# RBAC (Role-Based Access Control)

### Normal User

* Can create tasks
* Can view only their own tasks
* Can update only their own tasks
* Can delete only their own tasks

### Admin User

* Can view all users' tasks
* Can update any task
* Can delete any task

---

# Search

Search tasks by title or description.

Example

```
GET /api/tasks/?search=python
```

---

# Filter

Filter tasks by status.

```
GET /api/tasks/?status=true
```

or

```
GET /api/tasks/?status=false
```

---

# Ordering

Newest First

```
GET /api/tasks/?ordering=-created_at
```

Oldest First

```
GET /api/tasks/?ordering=created_at
```

---

# Pagination

```
GET /api/tasks/?page=1
```

```
GET /api/tasks/?page=2
```

---

# Testing

The APIs were tested using **Postman**.

Tested Features:

* Login
* Refresh Token
* CRUD Operations
* RBAC
* Search
* Filter
* Ordering
* Pagination

The Postman collection is available in the **postman** folder.

---

# HTTP Status Codes

| Code | Description  |
| ---- | ------------ |
| 200  | OK           |
| 201  | Created      |
| 204  | No Content   |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 404  | Not Found    |

---

# Future Improvements

* User Registration API
* Due Date for Tasks
* Email Notifications
* Docker Support
* PostgreSQL Integration

---

# Author

**Aniket Dalvi**

GitHub: https://github.com/dalvianiket10
