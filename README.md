# 📚 Course Management API

A RESTful API built with **FastAPI** for managing courses.
This project implements full CRUD operations, input validation, and proper HTTP status handling.

---

## 🚀 Features

* Create, read, update, and delete courses (CRUD)
* Data validation using **Pydantic**
* Proper HTTP status codes (200, 201, 204, 404)
* In-memory database (Python dictionary)
* Clean and structured code following REST principles

---

## 🛠️ Technologies

* Python 3
* FastAPI
* Uvicorn
* Pydantic

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/bertollimb/course-api.git
cd course-api
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install fastapi gunicorn uvicorn
pip freeze > requirements.txt
```

---

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📑 Interactive Documentation

FastAPI provides automatic docs:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 📌 Endpoints

### 🔹 Get all courses

```
GET /courses
```

### 🔹 Get a course by ID

```
GET /courses/{course_id}
```

### 🔹 Create a new course

```
POST /courses
```

### 🔹 Update a course

```
PUT /courses/{course_id}
```

### 🔹 Delete a course

```
DELETE /courses/{course_id}
```

---

## 📥 Example Request (POST)

```json
{
  "title": "Python for Beginners",
  "course_classes": 50,
  "hours": 40
}
```

---

## 📤 Example Response

```json
{
  "title": "Python for Beginners",
  "course_classes": 50,
  "hours": 40
}
```

---

## ⚠️ Error Handling

* `404 Not Found` → Course does not exist
* `201 Created` → Resource successfully created
* `204 No Content` → Resource successfully deleted

---

## 📈 Future Improvements

* Integration with a real database (PostgreSQL)
* Authentication and authorization (JWT)
* Pagination and filtering
* Deployment (Docker + Cloud)

---

## 👨‍💻 Author

Developed by Matheus Bertolli
Aspiring Backend Developer focused on Python and FastAPI

---
