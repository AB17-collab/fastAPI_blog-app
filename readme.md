# 🚀 Full Stack Blog Platform (FastAPI + Streamlit)

A production-style full-stack blog application built using **FastAPI (backend)** and **Streamlit (frontend)**, following a clean layered architecture and modern backend engineering practices.

---

## 🌟 Overview

This project demonstrates how to design and build a scalable backend system with:

* Clean architecture (Router → Service → Repository → Database)
* JWT-based authentication
* RESTful API design
* Frontend integration using Streamlit
* SQLAlchemy ORM for database operations

---

## 🏗️ Architecture

```
User (Browser / Streamlit UI)
        ↓
Frontend (Streamlit)
        ↓
FastAPI Backend (API Layer)
        ↓
Service Layer (Business Logic)
        ↓
Repository Layer (Database Queries)
        ↓
Database (SQLite - blog.db)
```

---

## 📂 Folder Structure

```
blog-app/
│
├── backend/
│   ├── app/
│   │   ├── api/            # API Routes (Controllers)
│   │   ├── services/       # Business Logic
│   │   ├── repositories/   # Database Queries
│   │   ├── models/         # SQLAlchemy Models
│   │   ├── schemas/        # Pydantic Schemas
│   │   ├── core/           # Config & Security
│   │   ├── db/             # Database connection
│   │   └── main.py         # Entry point
│   │
│   ├── blog.db             # SQLite database
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── app.py              # Streamlit UI
│
├── .gitignore
└── README.md
```

---

## 🔄 Application Workflow

### 🔐 Authentication Flow

1. User enters username & password (Streamlit UI)
2. Request sent to FastAPI `/login`
3. Backend verifies credentials from database
4. JWT token is generated
5. Token returned and used for further requests

---

### 📝 Create Blog Flow

1. User submits blog form
2. Frontend sends POST request with JWT token
3. Backend validates token
4. Service layer processes request
5. Repository saves data to database
6. Blog stored in `blog.db`

---

### 📖 Fetch Blogs Flow

1. Frontend sends GET request
2. Backend retrieves data
3. Data returned as JSON
4. UI displays blogs

---

## 🧠 Architecture Explanation

### 🔹 API Layer (Routers)

* Handles HTTP requests
* Example: `/login`, `/blogs`

### 🔹 Service Layer

* Contains business logic
* Validates and processes data

### 🔹 Repository Layer

* Handles DB queries
* Uses SQLAlchemy ORM

### 🔹 Database Layer

* SQLite database (`blog.db`)
* Stores users and blogs

---

## 🗄️ Database Schema

### Users Table

| id | name | email | age | password |
|----|------|-------|-----|----------|

### Blogs Table

| id | title | content | published | user_id |
|----|-------|---------|-----------|---------|

---

## ⚙️ How to Run the Project

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/AB17-collab/fastAPI_blog-app.git
cd fastAPI_blog-app
```

---

### 🔹 Step 2: Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 3: Create Environment File

Create `.env` inside `backend/`:

```
SECRET_KEY=mysecretkey
```

---

### 🔹 Step 4: Run Backend

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 🔹 Step 5: Run Frontend

```bash
cd frontend
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

## 🧪 How to Test

1. Register a user
2. Login to get JWT token
3. Create blog
4. View blogs

---

## 🔐 Authentication

* JWT-based authentication
* Required for protected routes

Header format:

```
Authorization: Bearer <token>
```

---

## 📦 Data Storage

* Data is stored in `backend/blog.db`
* SQLite database
* Automatically created on first run

---

## ⚡ Features

* User Registration & Login
* Secure JWT Authentication
* Blog CRUD Operations
* Clean Layered Architecture
* Streamlit UI Integration

---

## 🚀 Future Improvements

* PostgreSQL integration
* Docker support
* CI/CD pipeline
* Role-based access
* Caching (Redis)

---

## 🧠 Key Learnings

* FastAPI backend development
* SQLAlchemy ORM usage
* JWT authentication
* Clean architecture design
* Full-stack integration

---

## 👨‍💻 Author

Arnab Deb
