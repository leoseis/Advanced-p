# ================================================================
# ADVANCED PYTHON: API CONSUMPTION AND FASTAPI
# SIMPLIFIED STEP-BY-STEP TEACHING GUIDE
# ================================================================
#
# HOW TO USE THIS FILE
# 1. Open this .py file in VS Code.
# 2. Teach the sections in order.
# 3. Copy each labelled example into the separate file named in the guide.
# 4. Run terminal commands in the VS Code terminal, not in this file.
# 5. The objective questions and teacher's answer key are at the end.
#
# WHAT STUDENTS WILL BUILD
# - First, a Python client that consumes an existing API.
# - Next, a Student Records API using FastAPI.
# - Then, CRUD endpoints, validation, documentation and tests.
#
# NOTE: The first Student API stores records in a Python dictionary.
# Data is temporary and resets when the server restarts. Database storage
# will be covered later in the ORM / SQLAlchemy topic.

# ================================================================
# PART 1: API FUNDAMENTALS
# ================================================================

# 1. WHAT IS AN API?
# API means Application Programming Interface. It allows two software
# systems to communicate using agreed rules.
# Example: a mobile weather app asks a weather API for today's forecast.
# The API sends data back, and the app displays it.
#
# Analogy:
# Customer = client application.
# Waiter = API interface.
# Kitchen = system providing the data.
# Order = request.
# Food delivered = response.

# 2. IMPORTANT API TERMS
# Client: the program sending a request.
# Server: the system receiving the request and providing a response.
# Endpoint: a URL/path used to access an API operation.
# Request: data sent from client to server.
# Response: data returned from server to client.
# JSON: a common format for sending structured data.
# Status code: a number describing the result of a request.
#
# Common HTTP methods:
# GET     - read/retrieve data.
# POST    - create/submit data.
# PUT     - replace/update a resource.
# PATCH   - update selected fields.
# DELETE  - delete a resource.
#
# Common status codes:
# 200 OK                    Request succeeded.
# 201 Created               A resource was created.
# 204 No Content            Succeeded; no response body is returned.
# 400 Bad Request           The request is invalid.
# 401 Unauthorized          Authentication is missing or invalid.
# 403 Forbidden             The client is not allowed to do this.
# 404 Not Found             The requested resource does not exist.
# 405 Method Not Allowed    The HTTP method is not supported for the path.
# 422 Unprocessable Entity  Request data failed validation in FastAPI.
# 500 Internal Server Error Unexpected server-side error.

# ================================================================
# PART 2: CONSUMING AN EXISTING API WITH REQUESTS
# ================================================================

# 3. WHAT DOES CONSUMING AN API MEAN?
# It means using a client program to send requests to an API that already
# exists, then reading and using the response.
# In this section we use JSONPlaceholder, a public fake/demo REST API.
# Its write endpoints simulate changes; they do not permanently store them.

# 4. CREATE THE PROJECT AND INSTALL REQUESTS
# Create a folder named api_fastapi_class and open it in VS Code.
# Linux / macOS:
#     python3 -m venv .venv
#     source .venv/bin/activate
# Windows PowerShell:
#     py -m venv .venv
#     .venv\Scripts\Activate.ps1
# Install the packages used in this guide:
#     python -m pip install requests "fastapi[standard]" pytest httpx
#
# 5. FIRST REQUEST: GET ALL POSTS
# Create consume_api.py and paste:
#
#     import requests
#
#     url = "https://jsonplaceholder.typicode.com/posts"
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()
#
#     print("Status:", response.status_code)
#     posts = response.json()
#     print(posts)
#
# Explanation:
# - requests.get() sends an HTTP GET request.
# - timeout=10 means do not wait longer than 10 seconds for the response.
# - raise_for_status() raises an exception for unsuccessful HTTP responses.
# - response.json() converts JSON into Python dictionaries/lists.
# Run: python consume_api.py
#
# 6. GET ONE POST
#     import requests
#     post_id = 1
#     url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()
#     post = response.json()
#     print("Title:", post["title"])
#     print("Body:", post["body"])
#
# 7. QUERY PARAMETERS
# Query parameters are extra values after ? in a URL.
# Example URL: /posts?userId=1
#     params = {"userId": 1}
#     response = requests.get(
#         "https://jsonplaceholder.typicode.com/posts",
#         params=params,
#         timeout=10
#     )
#     response.raise_for_status()
#     print(response.url)
#     print(response.json())
#
# 8. HEADERS
# Headers provide additional request information.
#     headers = {"Accept": "application/json"}
#     response = requests.get(
#         "https://jsonplaceholder.typicode.com/posts",
#         headers=headers,
#         timeout=10
#     )
#     print(response.status_code)
#
# 9. CREATE WITH POST
#     new_post = {
#         "title": "Learning FastAPI",
#         "body": "I am learning API consumption with Python.",
#         "userId": 1
#     }
#     response = requests.post(
#         "https://jsonplaceholder.typicode.com/posts",
#         json=new_post,
#         timeout=10
#     )
#     response.raise_for_status()
#     print(response.status_code)
#     print(response.json())
# json=new_post sends the dictionary as a JSON request body.
#
# 10. UPDATE WITH PUT
#     post_id = 1
#     updated_post = {
#         "id": post_id,
#         "title": "Updated title",
#         "body": "Updated content",
#         "userId": 1
#     }
#     response = requests.put(
#         f"https://jsonplaceholder.typicode.com/posts/{post_id}",
#         json=updated_post,
#         timeout=10
#     )
#     response.raise_for_status()
#     print(response.json())
#
# 11. PARTIAL UPDATE WITH PATCH
#     changes = {"title": "Only the title changed"}
#     response = requests.patch(
#         "https://jsonplaceholder.typicode.com/posts/1",
#         json=changes,
#         timeout=10
#     )
#     response.raise_for_status()
#     print(response.json())
#
# 12. DELETE
#     response = requests.delete(
#         "https://jsonplaceholder.typicode.com/posts/1",
#         timeout=10
#     )
#     print("Status:", response.status_code)
#
# 13. HANDLE REQUEST ERRORS
#     import requests
#
#     try:
#         response = requests.get(
#             "https://jsonplaceholder.typicode.com/posts",
#             timeout=10
#         )
#         response.raise_for_status()
#         print(response.json())
#     except requests.exceptions.Timeout:
#         print("The request took too long.")
#     except requests.exceptions.RequestException as error:
#         print("API request failed:", error)
#
# Remember:
# GET reads, POST creates, PUT replaces, PATCH partially updates, DELETE
# removes. Use params= for query parameters, headers= for headers, json=
# for a JSON body, and timeout= so the client does not wait indefinitely.

# ================================================================
# PART 3: BUILD YOUR OWN API WITH FASTAPI
# ================================================================

# 14. WHAT IS FASTAPI?
# FastAPI is a Python framework for building APIs.
# Earlier we consumed an API. Now we build an API and let other programs
# consume it.
# FastAPI features include:
# - Route decorators for GET, POST, PUT, PATCH and DELETE.
# - Path and query parameters.
# - Request body handling.
# - Data validation with Pydantic and type hints.
# - Response models and status codes.
# - Automatic interactive documentation.
# - Dependencies, routers, middleware and CORS support.
# - Synchronous def and asynchronous async def endpoints.

# 15. CREATE A FASTAPI PROJECT
# In api_fastapi_class, create a folder named student_api.
# Open a terminal in student_api.
# Create/activate a virtual environment if needed:
#     python3 -m venv .venv
#     source .venv/bin/activate
# Install:
#     python -m pip install "fastapi[standard]" pytest httpx requests
# Create a file named main.py.

# 16. FIRST FASTAPI APP
# Put this into main.py:
#
#     from fastapi import FastAPI
#
#     app = FastAPI(
#         title="Student API",
#         description="A simple API for learning FastAPI",
#         version="1.0.0"
#     )
#
#     @app.get("/")
#     async def home():
#         return {"message": "Welcome to my first API"}
#
# Explanation:
# - FastAPI() creates the application instance.
# - title, description and version customise the API documentation.
# - @app.get("/") registers a GET endpoint at the root path.
# - the function returns a Python dictionary, which FastAPI sends as JSON.
#
# 17. RUN THE SERVER
# From the folder containing main.py, run either:
#     fastapi dev main.py
# or:
#     uvicorn main:app --reload
#
# In uvicorn main:app:
# - main refers to main.py.
# - app refers to the FastAPI variable named app.
# - --reload restarts the development server when code changes.
#
# Open these in your browser:
#     http://127.0.0.1:8000/
#     http://127.0.0.1:8000/docs
#     http://127.0.0.1:8000/redoc
#     http://127.0.0.1:8000/openapi.json
# /docs is interactive Swagger UI documentation. Students can try API
# endpoints there without writing a separate client first.

# ================================================================
# PART 4: IMPORTANT FASTAPI ATTRIBUTES AND PARAMETERS
# ================================================================

# 18. APPLICATION ATTRIBUTES
# Example:
#     app = FastAPI(
#         title="Student Records API",
#         description="Manage student records",
#         version="1.0.0",
#         docs_url="/docs",
#         redoc_url="/redoc",
#         openapi_url="/openapi.json"
#     )
#
# title         Name shown in API documentation.
# description   Explains the API; Markdown can be used.
# version       API version label.
# docs_url      Path for Swagger UI; set to None to disable it.
# redoc_url     Path for ReDoc; set to None to disable it.
# openapi_url   Path for generated OpenAPI schema.
# These are application settings. Do not change them without a reason.
#
# 19. ROUTE DECORATOR OPTIONS
# Example:
#     @app.get(
#         "/students",
#         response_model=list[StudentOut],
#         status_code=200,
#         tags=["Students"],
#         summary="Get students",
#         description="Returns student records",
#         deprecated=False
#     )
#
# response_model  Describes/validates the response data structure.
# status_code     Sets the HTTP response status code.
# tags            Groups endpoints in /docs.
# summary         Short endpoint description.
# description     Longer endpoint description.
# deprecated      Marks an endpoint as deprecated in documentation.
# include_in_schema=False hides a route from generated API documentation.
# Use only the options that help explain and document your endpoint.
#
# 20. PATH PARAMETERS
# Path values are part of the URL.
# URL: /students/5
# Code:
#     @app.get("/students/{student_id}")
#     async def get_student(student_id: int):
#         return {"student_id": student_id}
# The {student_id} placeholder is read from the URL. FastAPI converts it
# to int and validates the type.
#
# 21. QUERY PARAMETERS
# Query values come after ? in the URL.
# URL: /students?course=Python&limit=5
# Code:
#     @app.get("/students")
#     async def list_students(course: str | None = None, limit: int = 10):
#         return {"course": course, "limit": limit}
# The default value makes a query parameter optional.
#
# 22. REQUEST BODY AND PYDANTIC
# A request body carries data from the client, usually JSON.
# Example JSON:
#     {"name": "Ada", "age": 20, "course": "Python"}
#
# Code:
#     from pydantic import BaseModel
#
#     class StudentCreate(BaseModel):
#         name: str
#         age: int
#         course: str
#
#     @app.post("/students")
#     async def create_student(student: StudentCreate):
#         return student
# FastAPI reads the JSON body and validates it against StudentCreate.
# Missing fields or invalid types normally produce a 422 response.
#
# 23. PYDANTIC Field() VALIDATION
#     from pydantic import BaseModel, Field
#
#     class StudentCreate(BaseModel):
#         name: str = Field(min_length=2, max_length=50)
#         age: int = Field(ge=1, le=120)
#         course: str = Field(min_length=2, max_length=80)
#
# Field constraints:
# min_length / max_length - string length limits.
# gt - greater than.
# ge - greater than or equal to.
# lt - less than.
# le - less than or equal to.
# pattern - regular-expression pattern for strings.
# description - field explanation shown in documentation.
# examples - example values for documentation.
#
# 24. PATH, QUERY, BODY, HEADER AND COOKIE
# FastAPI can read request data from several places:
# - Path: /students/12
# - Query: /students?course=Python
# - Body: JSON sent with POST/PUT/PATCH.
# - Header: request metadata such as Authorization or User-Agent.
# - Cookie: browser-stored values sent with a request.
#
# Helpers include Path(), Query(), Body(), Header(), Cookie(), Form(), File().
# Example imports:
#     from typing import Annotated
#     from fastapi import Path, Query, Header
#
#     student_id: Annotated[int, Path(ge=1)]
#     limit: Annotated[int, Query(ge=1, le=100)] = 10
#     user_agent: Annotated[str | None, Header()] = None
#
# 25. RESPONSE MODEL
# A request model describes accepted input. A response model describes output.
#     class StudentOut(BaseModel):
#         id: int
#         name: str
#         age: int
#         course: str
#
#     @app.get("/students/{student_id}", response_model=StudentOut)
#     async def get_student(student_id: int):
#         return students_db[student_id]
#
# response_model documents and validates returned data and filters out fields
# that are not part of the declared response model.
#
# 26. HTTPException AND STATUS CODES
# Use HTTPException to return an HTTP error response:
#     from fastapi import HTTPException, status
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Student not found"
#     )
# status provides readable constants, including:
# HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT,
# HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN,
# HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY,
# HTTP_500_INTERNAL_SERVER_ERROR.

# ================================================================
# PART 5: PRACTICAL STUDENT RECORDS CRUD API
# ================================================================

# 27. CREATE THE COMPLETE MAIN APP
# Replace main.py with the following code. It uses temporary in-memory data.
#
#     from typing import Annotated
#     from fastapi import FastAPI, HTTPException, Path, Query, status
#     from pydantic import BaseModel, Field
#
#     app = FastAPI(
#         title="Student Records API",
#         description="A beginner project for learning FastAPI CRUD",
#         version="1.0.0"
#     )
#
#     class StudentCreate(BaseModel):
#         name: str = Field(min_length=2, max_length=50)
#         age: int = Field(ge=1, le=120)
#         course: str = Field(min_length=2, max_length=80)
#
#     class StudentUpdate(BaseModel):
#         name: str | None = Field(default=None, min_length=2, max_length=50)
#         age: int | None = Field(default=None, ge=1, le=120)
#         course: str | None = Field(default=None, min_length=2, max_length=80)
#
#     class StudentOut(BaseModel):
#         id: int
#         name: str
#         age: int
#         course: str
#
#     students_db = {
#         1: {"id": 1, "name": "Ada", "age": 20, "course": "Python"},
#         2: {"id": 2, "name": "Tunde", "age": 22, "course": "FastAPI"}
#     }
#     next_student_id = 3
#
#     @app.get("/", tags=["General"])
#     async def home():
#         return {"message": "Welcome to the Student Records API"}
#
#     @app.get("/health", tags=["General"])
#     async def health_check():
#         return {"status": "healthy"}
#
#     @app.get(
#         "/students",
#         response_model=list[StudentOut],
#         tags=["Students"],
#         summary="Get all students"
#     )
#     async def get_students(
#         course: str | None = None,
#         skip: Annotated[int, Query(ge=0)] = 0,
#         limit: Annotated[int, Query(ge=1, le=100)] = 10
#     ):
#         students = list(students_db.values())
#         if course:
#             students = [
#                 student for student in students
#                 if student["course"].lower() == course.lower()
#             ]
#         return students[skip:skip + limit]
#
#     @app.get(
#         "/students/{student_id}",
#         response_model=StudentOut,
#         tags=["Students"]
#     )
#     async def get_student(student_id: Annotated[int, Path(ge=1)]):
#         student = students_db.get(student_id)
#         if student is None:
#             raise HTTPException(status_code=404, detail="Student not found")
#         return student
#
#     @app.post(
#         "/students",
#         response_model=StudentOut,
#         status_code=status.HTTP_201_CREATED,
#         tags=["Students"]
#     )
#     async def create_student(student: StudentCreate):
#         global next_student_id
#         new_student = {"id": next_student_id, **student.model_dump()}
#         students_db[next_student_id] = new_student
#         next_student_id += 1
#         return new_student
#
#     @app.put(
#         "/students/{student_id}",
#         response_model=StudentOut,
#         tags=["Students"]
#     )
#     async def replace_student(
#         student_id: Annotated[int, Path(ge=1)],
#         student: StudentCreate
#     ):
#         if student_id not in students_db:
#             raise HTTPException(status_code=404, detail="Student not found")
#         updated = {"id": student_id, **student.model_dump()}
#         students_db[student_id] = updated
#         return updated
#
#     @app.patch(
#         "/students/{student_id}",
#         response_model=StudentOut,
#         tags=["Students"]
#     )
#     async def patch_student(
#         student_id: Annotated[int, Path(ge=1)],
#         student: StudentUpdate
#     ):
#         existing = students_db.get(student_id)
#         if existing is None:
#             raise HTTPException(status_code=404, detail="Student not found")
#         changes = student.model_dump(exclude_unset=True)
#         updated = {**existing, **changes}
#         students_db[student_id] = updated
#         return updated
#
#     @app.delete("/students/{student_id}", tags=["Students"])
#     async def delete_student(student_id: Annotated[int, Path(ge=1)]):
#         deleted = students_db.pop(student_id, None)
#         if deleted is None:
#             raise HTTPException(status_code=404, detail="Student not found")
#         return {"message": "Student deleted successfully"}
#
# Explanation:
# StudentCreate validates the required fields when creating/replacing a student.
# StudentUpdate makes fields optional for partial updates.
# StudentOut describes the fields returned to the client.
# students_db is a temporary Python dictionary, not a real database.
# GET /students reads all students and supports course, skip and limit filters.
# GET /students/{id} reads one student.
# POST /students creates a student and returns 201.
# PUT replaces all editable student fields.
# PATCH updates only the fields supplied by the client.
# DELETE removes a student or returns 404 if the ID does not exist.
# model_dump(exclude_unset=True) includes only fields supplied to PATCH.
#
# 28. RUN THE API
# From the folder containing main.py, run:
#     fastapi dev main.py
# OR:
#     uvicorn main:app --reload
# Open http://127.0.0.1:8000/docs
# Try GET, POST, PUT, PATCH, and DELETE from the interactive documentation.
#
# Example POST body:
#     {"name": "Chidi", "age": 24, "course": "Advanced Python"}
# Example PATCH body:
#     {"course": "FastAPI"}
# Try invalid data, such as age=-5, to observe Pydantic validation.
#
# 29. ROUTE ORDER
# If you have a fixed path such as /students/me and a parameter path such as
# /students/{student_id}, declare the fixed route first so it is not mistaken
# for a student ID.
#
# ================================================================
# PART 6: MORE FASTAPI FEATURES
# ================================================================

# 30. DEPENDENCY INJECTION WITH Depends
# Dependencies provide reusable logic to endpoint functions.
# Example:
#     from typing import Annotated
#     from fastapi import Depends, FastAPI
#     app = FastAPI()
#
#     def pagination(skip: int = 0, limit: int = 10):
#         return {"skip": skip, "limit": limit}
#
#     @app.get("/pagination-demo")
#     async def pagination_demo(
#         paging: Annotated[dict, Depends(pagination)]
#     ):
#         return paging
# Depends(pagination) tells FastAPI to call the dependency and pass its
# returned value to the endpoint.
#
# 31. HEADERS
# Headers carry request metadata such as User-Agent or Authorization.
# Example:
#     from typing import Annotated
#     from fastapi import FastAPI, Header
#     app = FastAPI()
#
#     @app.get("/client-info")
#     async def client_info(
#         user_agent: Annotated[str | None, Header()] = None
#     ):
#         return {"user_agent": user_agent}
# A User-Agent is not proof of identity and must not be used as authentication.
#
# 32. APIRouter — ORGANISE A LARGER PROJECT
# When an API grows, putting all routes in main.py becomes difficult.
# APIRouter groups related endpoints in separate files.
# Suggested structure:
#     student_api/
#         main.py
#         routers/
#             __init__.py
#             students.py
#
# In routers/students.py:
#     from fastapi import APIRouter
#     router = APIRouter(prefix="/students", tags=["Students"])
#
#     @router.get("/")
#     async def list_students():
#         return [{"id": 1, "name": "Ada"}]
#
# In main.py:
#     from fastapi import FastAPI
#     from routers.students import router as students_router
#     app = FastAPI(title="Student API")
#     app.include_router(students_router)
# prefix adds /students to routes in that router.
# include_router connects the router to the main application.
#
# 33. CORS — CONNECTING A FRONTEND
# CORS means Cross-Origin Resource Sharing. Browsers use CORS rules when
# JavaScript from one origin calls an API on another origin.
# Example: Vite at http://localhost:5173 calls FastAPI at http://127.0.0.1:8000.
# Add to main.py when the browser frontend needs access:
#
#     from fastapi.middleware.cors import CORSMiddleware
#
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["http://localhost:5173"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"]
#     )
# Use the exact origin your frontend runs on. CORS is not authentication and
# does not stop non-browser clients such as Requests or curl.
#
# 34. MIDDLEWARE
# Middleware runs shared logic around requests and responses.
# Example:
#     import time
#     from fastapi import Request
#
#     @app.middleware("http")
#     async def measure_time(request: Request, call_next):
#         start = time.perf_counter()
#         response = await call_next(request)
#         response.headers["X-Process-Time"] = str(time.perf_counter() - start)
#         return response
# This example adds an X-Process-Time header to each response.
#
# 35. TEST FASTAPI WITH pytest AND TestClient
# Install testing packages:
#     python -m pip install pytest httpx
# Create tests/test_main.py:
#
#     from fastapi.testclient import TestClient
#     from main import app
#     client = TestClient(app)
#
#     def test_home():
#         response = client.get("/")
#         assert response.status_code == 200
#
#     def test_get_students():
#         response = client.get("/students")
#         assert response.status_code == 200
#         assert isinstance(response.json(), list)
#
#     def test_create_student():
#         payload = {"name": "Test Student", "age": 20, "course": "Python"}
#         response = client.post("/students", json=payload)
#         assert response.status_code == 201
#         assert response.json()["name"] == "Test Student"
#
# Run from project root:
#     python -m pytest -v
# TestClient calls the application directly; a separate live server is not
# required for these tests. These tests use the app's in-memory state, so
# more advanced tests should reset data between tests.
#
# 36. AUTHENTICATION — INTRODUCTION
# Authentication checks who a user is. Authorization checks what that user
# is allowed to do. API approaches include API keys, bearer tokens, OAuth2,
# and JWT access tokens. Never hard-code credentials or store plain-text
# passwords. Real applications need secure password hashing, HTTPS, token
# handling, and permission checks. Teach authentication as its own lesson.
#
# ================================================================
# PART 7: PRACTICAL ASSIGNMENT AND QUICK REFERENCE
# ================================================================

# 37. STUDENT ASSIGNMENT: STUDENT RECORDS API
# Students must:
# 1. Create a FastAPI project.
# 2. Create StudentCreate and StudentOut Pydantic models.
# 3. Validate name, age and course.
# 4. Add GET /students.
# 5. Add GET /students/{student_id}.
# 6. Add POST /students.
# 7. Add PUT /students/{student_id}.
# 8. Add PATCH /students/{student_id}.
# 9. Add DELETE /students/{student_id}.
# 10. Return 404 if a student does not exist.
# 11. Add course filtering and skip/limit pagination.
# 12. Test all endpoints in /docs.
# 13. Write at least five pytest tests.
# 14. Write a Requests client to consume their own API.
# Extension: add APIRouter, CORS, a count endpoint, and a Depends dependency.
# Submission: project folder/GitHub repo, README, /docs screenshot and test result.
#
# 38. QUICK REFERENCE
# Requests:
# requests.get(url, timeout=10)
# requests.post(url, json=data, timeout=10)
# requests.put(url, json=data, timeout=10)
# requests.patch(url, json=data, timeout=10)
# requests.delete(url, timeout=10)
# response.json(), response.status_code, response.raise_for_status()
#
# FastAPI:
# app = FastAPI(title=..., description=..., version=...)
# @app.get(), @app.post(), @app.put(), @app.patch(), @app.delete()
# BaseModel, Field(), Path(), Query(), Body(), Header(), Cookie()
# response_model=, status_code=, tags=, summary=, description=
# HTTPException, status, Depends(), APIRouter, include_router()
# CORSMiddleware, @app.middleware("http"), TestClient
#
# ================================================================
# PART 8: OBJECTIVE TEST — 25 QUESTIONS
# Choose ONE answer (A, B, C, or D). One mark each. Total: 25 marks.
# ================================================================
#
# 1. What does API stand for?
# A. Application Programming Interface
# B. Application Python Internet
# C. Automated Program Installation
# D. Advanced Programming Input
#
# 2. What does it mean to consume an API?
# A. Build a database table
# B. Send requests to an existing API and use its response
# C. Delete an API
# D. Install Python
#
# 3. Which HTTP method is commonly used to read data?
# A. POST   B. GET   C. DELETE   D. PATCH
#
# 4. Which HTTP method commonly creates a resource?
# A. GET   B. POST   C. DELETE   D. OPTIONS
#
# 5. Which status code commonly means a resource was created?
# A. 200   B. 201   C. 404   D. 500
#
# 6. What does response.json() do in Requests?
# A. Converts JSON into Python data
# B. Deletes the response
# C. Starts a server
# D. Installs Requests
#
# 7. Why use timeout= in an HTTP request?
# A. To enlarge JSON
# B. To limit how long the client waits
# C. To change the method
# D. To create an endpoint
#
# 8. What does FastAPI help developers build?
# A. APIs using Python
# B. Spreadsheet formulas
# C. Operating systems
# D. Image files
#
# 9. What does app = FastAPI() create?
# A. A database table
# B. The FastAPI application instance
# C. A virtual environment
# D. An HTTP client
#
# 10. What does @app.get("/") define?
# A. A GET endpoint at the root path
# B. A POST body
# C. A database model
# D. A test case
#
# 11. What is a path parameter?
# A. A value inside the URL path, such as /students/5
# B. A cookie only
# C. A Python package
# D. A response status
#
# 12. Where do query parameters appear?
# A. After ? in a URL
# B. Only inside a Python class
# C. Only inside a response model
# D. In the terminal prompt
#
# 13. What is Pydantic BaseModel commonly used for?
# A. Defining and validating structured data
# B. Starting Git
# C. Styling a webpage
# D. Creating a virtual environment
#
# 14. What does Field(ge=1, le=120) mean for an integer?
# A. It must be between 1 and 120, inclusive
# B. It must be a string
# C. It must be negative
# D. It is always optional
#
# 15. What does response_model do?
# A. Defines and validates response structure
# B. Installs the server
# C. Deletes the request
# D. Automatically creates a database connection
#
# 16. What is HTTPException used for?
# A. Returning an HTTP error response
# B. Installing FastAPI
# C. Creating a Pydantic model
# D. Starting pytest
#
# 17. What is the usual meaning of HTTP 404?
# A. Created   B. Not Found   C. OK   D. Internal Server Error
#
# 18. What is FastAPI /docs for?
# A. Interactive API documentation and testing
# B. A source-code folder
# C. A database backup
# D. A virtual environment
#
# 19. What does APIRouter help with?
# A. Grouping related endpoints into separate route modules
# B. Downloading Python
# C. Replacing HTTP
# D. Creating passwords
#
# 20. What does Depends() provide?
# A. Dependency injection for reusable logic
# B. A Git commit
# C. A CSV file
# D. A browser cookie automatically
#
# 21. What is CORS concerned with?
# A. Browser requests between different origins
# B. Python list sorting
# C. Database table creation
# D. Password hashing
#
# 22. What does middleware do?
# A. Runs shared logic around requests and responses
# B. Deletes all routes
# C. Converts Python into HTML
# D. Creates a virtual environment
#
# 23. Which HTTP method is commonly used for partial updates?
# A. GET   B. PATCH   C. OPTIONS   D. HEAD
#
# 24. What does FastAPI TestClient allow?
# A. Testing endpoints without starting a separate live server
# B. Publishing a package
# C. Creating a React app
# D. Installing PostgreSQL
#
# 25. Why does in-memory student data disappear after restart?
# A. A Python dictionary is temporary and not persisted
# B. FastAPI cannot return JSON
# C. GET requests delete data
# D. Pydantic removes records
#
# TEACHER'S ANSWER KEY — HIDE BEFORE DISTRIBUTING
# 1 A, 2 B, 3 B, 4 B, 5 B, 6 A, 7 B, 8 A, 9 B, 10 A,
# 11 A, 12 A, 13 A, 14 A, 15 A, 16 A, 17 B, 18 A, 19 A,
# 20 A, 21 A, 22 A, 23 B, 24 A, 25 A.
#
# OFFICIAL REFERENCE DOCUMENTATION
# FastAPI: https://fastapi.tiangolo.com/tutorial/
# Requests: https://requests.readthedocs.io/en/stable/user/quickstart/
# Pydantic: https://docs.pydantic.dev/latest/
#
# END OF TEACHING GUIDE

if __name__ == "__main__":
    print("API Consumption and FastAPI — Teaching Guide")
    print("Read the commented lessons and copy the examples into project files.")
    print("Install packages as instructed before running the individual examples.")
