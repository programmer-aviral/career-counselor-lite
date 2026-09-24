# CAREER COUNSELOR LITE

## Complete Backend Learning & Viva Notes

---

# 1. PROJECT OVERVIEW

## 1.1 What is Career Counselor Lite?

Career Counselor Lite is a career guidance platform designed to help students and professionals make informed career decisions.

The platform can help users with:

* Career choices after Class 10
* Career choices after Class 12
* Undergraduate course selection
* Higher education
* Career exploration
* Skill development
* Career changes
* Entrepreneurship
* Career assessments
* Personalized career recommendations
* Career roadmaps
* AI-based career counseling

The backend is responsible for:

```text
User management
Authentication
Profiles
Education data
Career data
Assessments
Recommendations
Roadmaps
AI counseling
Database operations
Security
API communication
```

---

# 2. HIGH-LEVEL ARCHITECTURE

The application follows this architecture:

```text
                FRONTEND
            React / TypeScript
                   |
                   | HTTP / REST
                   ↓
          DJANGO REST FRAMEWORK
                   |
                   ↓
          Django Views / APIs
                   |
                   ↓
          Business Logic / Services
                   |
                   ↓
             Django ORM
                   |
                   ↓
              PostgreSQL
```

The AI layer is separate:

```text
Frontend
   ↓
Django API
   ↓
Counselor Service
   ↓
AI Provider abstraction
   ↓
Gemini / Mock AI
```

This separation is important.

The frontend should not directly communicate with the database.

The frontend should also not contain the Gemini API key.

---

# 3. TECHNOLOGY STACK

The backend uses:

```text
Python
Django
Django REST Framework
PostgreSQL
psycopg
SimpleJWT
django-cors-headers
python-dotenv
Gemini provider
```

## What each technology does

### Python

Python is the programming language.

Django and Django REST Framework are Python frameworks.

---

### Django

Django is a web framework.

It provides:

* URL routing
* Models
* ORM
* Authentication
* Admin panel
* Middleware
* Forms
* Security features
* Database migrations

---

### Django REST Framework

Django itself can generate web pages.

DRF adds tools for building APIs.

For example:

```text
GET /api/careers/
```

can return:

```json
{
  "id": 1,
  "title": "Software Engineer"
}
```

instead of returning an HTML page.

---

### PostgreSQL

PostgreSQL is the relational database.

It stores:

* users
* profiles
* careers
* education data
* assessments
* answers
* recommendations
* roadmaps
* conversations
* messages

---

### psycopg

Django needs a database driver to communicate with PostgreSQL.

Your project uses:

```text
psycopg
```

The flow is:

```text
Django
 ↓
Django PostgreSQL backend
 ↓
psycopg
 ↓
PostgreSQL
```

---

### SimpleJWT

SimpleJWT provides JWT authentication.

It creates:

```text
Access Token
Refresh Token
```

---

### django-cors-headers

CORS allows the frontend and backend to communicate when they are hosted on different origins.

Example:

```text
Frontend:
http://localhost:5173

Backend:
http://127.0.0.1:8000
```

These are different origins.

CORS controls whether the browser permits the frontend to call the backend.

---

### python-dotenv

Loads environment variables from `.env`.

This allows sensitive configuration to stay outside source code.

Example:

```env
SECRET_KEY=...
DB_PASSWORD=...
GEMINI_API_KEY=...
```

---

# 4. REST API

REST stands for:

**Representational State Transfer.**

It is an architectural style commonly used for APIs.

Your frontend communicates with Django using HTTP.

Example:

```text
Frontend
   |
   | GET /api/careers/
   ↓
Django
   |
   ↓
PostgreSQL
```

Django returns JSON.

---

# 5. HTTP METHODS

The main HTTP methods are:

## GET

Used to retrieve data.

Example:

```text
GET /api/careers/
```

Means:

> Give me the careers.

---

## POST

Used to create something.

Example:

```text
POST /api/auth/register/
```

Means:

> Create a new user.

---

## PUT

Used for a complete update.

Example:

```text
PUT /api/profile/
```

Conceptually:

> Replace/update the complete profile representation.

---

## PATCH

Used for partial updates.

Example:

```text
PATCH /api/profile/
```

Conceptually:

> Change only the fields I provided.

---

## DELETE

Used to delete a resource.

The current backend doesn't make DELETE central to the main user workflow.

---

# 6. HTTP STATUS CODES

Important codes:

```text
200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
429 Too Many Requests
500 Internal Server Error
```

### Example

Successful registration:

```text
201 Created
```

Invalid input:

```text
400 Bad Request
```

No authentication:

```text
401 Unauthorized
```

Authenticated but not allowed:

```text
403 Forbidden
```

Object doesn't exist:

```text
404 Not Found
```

---

# 7. JSON

JSON means:

**JavaScript Object Notation.**

It is a common data format used between frontend and backend.

Example:

```json
{
  "username": "aviral",
  "email": "example@gmail.com",
  "education_level": "12th",
  "career_goal": "Software Engineering"
}
```

The frontend sends JSON to Django.

Django processes it.

Django returns JSON.

---

# 8. PROJECT STRUCTURE

The backend contains:

```text
backend/
│
├── accounts/
├── profiles/
├── education/
├── careers/
├── assessments/
├── recommendations/
├── roadmaps/
├── counselor/
├── common/
│
├── config/
│
├── manage.py
├── requirements.txt
├── .env
└── .env.example
```

Each application has a responsibility.

---

# 9. WHY DJANGO APPS ARE SEPARATED

Instead of putting everything into one huge application, functionality is separated.

```text
accounts
    ↓
Authentication

profiles
    ↓
User information

education
    ↓
Education reference data

careers
    ↓
Career knowledge

assessments
    ↓
Tests and results

recommendations
    ↓
Career matching

roadmaps
    ↓
Career plans

counselor
    ↓
AI counselor

common
    ↓
Shared utilities
```

This follows separation of concerns.

---

# 10. manage.py

`manage.py` is Django's command-line utility.

Examples:

```powershell
python manage.py runserver
```

Starts the development server.

```powershell
python manage.py migrate
```

Applies database migrations.

```powershell
python manage.py makemigrations
```

Creates migration files from model changes.

```powershell
python manage.py createsuperuser
```

Creates an admin user.

```powershell
python manage.py check
```

Checks the Django project for configuration problems.

```powershell
python manage.py test
```

Runs tests.

---

# 11. DJANGO SETTINGS

`config/settings.py` contains project configuration.

Important settings include:

```python
SECRET_KEY
DEBUG
ALLOWED_HOSTS
INSTALLED_APPS
MIDDLEWARE
DATABASES
AUTH_USER_MODEL
REST_FRAMEWORK
SIMPLE_JWT
CORS_ALLOWED_ORIGINS
```

---

# 12. SECRET_KEY

Django uses `SECRET_KEY` for security-related cryptographic operations.

It should not be publicly exposed.

Bad:

```python
SECRET_KEY = "my-real-secret"
```

Better:

```env
SECRET_KEY=...
```

and:

```python
SECRET_KEY = os.environ.get("SECRET_KEY")
```

---

# 13. DEBUG

During development:

```env
DEBUG=True
```

During production:

```env
DEBUG=False
```

Why?

Because Django's debug mode can expose detailed error information.

Never use:

```text
DEBUG=True
```

on a public production server.

---

# 14. ALLOWED_HOSTS

Django uses `ALLOWED_HOSTS` to control which host/domain names are accepted.

Development might contain:

```text
localhost
127.0.0.1
```

Production should contain your actual domain.

---

# 15. ENVIRONMENT VARIABLES

Environment variables store configuration outside source code.

Example:

```env
SECRET_KEY=...
DEBUG=True

DB_NAME=career_counselor_db
DB_USER=career_counselor_app
DB_PASSWORD=...
DB_HOST=127.0.0.1
DB_PORT=5432

GEMINI_API_KEY=...
```

Why?

Because source code can be:

```text
uploaded to GitHub
shared
copied
reviewed
deployed
```

Passwords and API keys should not be inside it.

---

# 16. .env VS .env.example

`.env`

Contains real secrets.

It should not be committed.

`.env.example`

Contains placeholders.

Example:

```env
SECRET_KEY=your-secret-key
DB_NAME=career_counselor_db
DB_USER=career_counselor_app
DB_PASSWORD=your-password
GEMINI_API_KEY=your-key
```

This file tells another developer what variables are required.

---

# 17. DATABASE

The project uses PostgreSQL.

Database:

```text
career_counselor_db
```

Application database user:

```text
career_counselor_app
```

The application connects through:

```text
127.0.0.1:5432
```

---

# 18. DATABASE ARCHITECTURE

Conceptually:

```text
PostgreSQL
│
├── accounts_user
├── profiles_profile
├── education_...
├── careers_...
├── assessments_...
├── recommendations_...
├── roadmaps_...
└── counselor_...
```

Django models become database tables.

---

# 19. DJANGO ORM

ORM means:

**Object Relational Mapper.**

It lets Python code interact with the database without manually writing SQL for every operation.

Example:

```python
User.objects.all()
```

means approximately:

```sql
SELECT * FROM accounts_user;
```

Another example:

```python
User.objects.get(id=1)
```

means approximately:

```sql
SELECT *
FROM accounts_user
WHERE id = 1;
```

---

# 20. WHY ORM IS USEFUL

Without ORM, developers would constantly write SQL.

With Django ORM:

```python
Career.objects.filter(category="Technology")
```

Django converts it into database queries.

ORM also handles:

* relationships
* filtering
* ordering
* creating
* updating
* deleting
* transactions

---

# 21. DJANGO MODELS

A model represents a database entity.

Example:

```python
class User(AbstractUser):
    pass
```

This creates the basis of the user database table.

Another example:

```python
class Message(models.Model):
    conversation = models.ForeignKey(...)
    role = models.CharField(...)
    content = models.TextField()
```

Each model field corresponds to database information.

---

# 22. CUSTOM USER MODEL

The project uses:

```python
class User(AbstractUser):
    pass
```

This is important.

Instead of using Django's default User directly, the project creates:

```text
accounts.User
```

based on Django's `AbstractUser`.

---

# 23. WHY CUSTOM USER?

Because future requirements may include fields such as:

```text
phone
user type
verification status
preferences
etc.
```

Using a custom user model from the beginning avoids major authentication migrations later.

---

# 24. AUTH_USER_MODEL

The project configures:

```python
AUTH_USER_MODEL = "accounts.User"
```

This tells Django:

> Use accounts.User as the project's authentication user model.

Other applications should refer to it using:

```python
settings.AUTH_USER_MODEL
```

rather than hardcoding:

```python
accounts.User
```

---

# 25. USER VS PROFILE

This distinction is very important.

The User contains identity/authentication information.

Conceptually:

```text
User
├── username
├── email
├── password
├── first_name
└── last_name
```

Profile contains career information:

```text
Profile
├── date of birth
├── phone
├── location
├── education
├── skills
├── interests
├── career goal
├── experience
└── work style
```

So:

```text
User = identity
Profile = career/person information
```

---

# 26. ONE-TO-ONE RELATIONSHIP

Profile uses a OneToOne relationship with User.

Conceptually:

```text
User 1 ───────── 1 Profile
```

One user has one profile.

---

# 27. FOREIGN KEY

A ForeignKey represents a many-to-one relationship.

Example:

```text
Conversation
    ↓
User
```

Many conversations can belong to one user.

```text
User
 ├── Conversation 1
 ├── Conversation 2
 └── Conversation 3
```

---

# 28. DATABASE RELATIONSHIPS IN THE PROJECT

Important relationships include:

```text
User
 ├── Profile
 ├── AssessmentAttempt
 ├── Recommendation
 ├── UserRoadmap
 └── Conversation

Conversation
 └── Messages

Assessment
 └── Questions
       └── Options

Roadmap
 └── Stages
       └── Tasks

UserRoadmap
 └── UserTaskProgress
```

Understanding these relationships is essential.

---

# 29. MIGRATIONS

Migrations are Django's way of tracking database schema changes.

Suppose you add:

```python
phone = models.CharField(...)
```

Then:

```powershell
python manage.py makemigrations
```

creates a migration.

Then:

```powershell
python manage.py migrate
```

actually changes the database.

---

# 30. MAKEMIGRATIONS VS MIGRATE

This is a common professor question.

### makemigrations

Creates migration instructions.

```text
Model change
    ↓
migration file
```

### migrate

Applies those instructions to the database.

```text
migration file
    ↓
database schema
```

---

# 31. MIGRATION EXAMPLE

Suppose:

```python
class Profile(models.Model):
    bio = models.TextField()
```

Later you add:

```python
phone = models.CharField(max_length=20)
```

Then:

```text
models.py changed
      ↓
makemigrations
      ↓
0002_add_phone.py
      ↓
migrate
      ↓
database gets phone column
```

---

# 32. ADMIN PANEL

Django Admin provides a web-based management interface.

URL:

```text
/admin/
```

It allows administrators to manage:

* users
* profiles
* careers
* education
* assessments
* recommendations
* roadmaps
* conversations

This is useful for managing reference data without building a separate admin frontend.

---

# 33. AUTHENTICATION VS AUTHORIZATION

Very important distinction.

### Authentication

Answers:

> Who are you?

Example:

```text
username + password
```

### Authorization

Answers:

> What are you allowed to do?

Example:

```text
User A cannot edit User B's profile.
```

The project uses both.

---

# 34. JWT AUTHENTICATION

JWT means:

**JSON Web Token.**

Instead of maintaining traditional server-side login state for every API request, the client sends a token.

Typical flow:

```text
Login
  ↓
Django validates credentials
  ↓
Access token + refresh token
  ↓
Frontend stores token appropriately
  ↓
Frontend sends access token
  ↓
Django verifies token
  ↓
Request is authenticated
```

---

# 35. ACCESS TOKEN

The access token is short-lived.

The client sends it when accessing protected APIs.

Conceptually:

```http
Authorization: Bearer <access-token>
```

---

# 36. REFRESH TOKEN

The refresh token is longer-lived.

When the access token expires:

```text
Refresh token
      ↓
new access token
```

This avoids requiring the user to log in every hour.

The exact lifetimes are configuration choices.

---

# 37. TOKEN BLACKLIST

The project uses:

```text
rest_framework_simplejwt.token_blacklist
```

This allows refresh tokens to be invalidated.

Logout flow:

```text
User clicks logout
       ↓
Frontend sends refresh token
       ↓
Django blacklists it
       ↓
Token cannot be used again
```

---

# 38. REGISTRATION FLOW

The registration API is:

```text
POST /api/auth/register/
```

Conceptually:

```text
Frontend
   ↓
username
email
password
   ↓
RegisterSerializer
   ↓
validate data
   ↓
create_user()
   ↓
password hashed
   ↓
User created
   ↓
Profile signal
   ↓
Profile created
   ↓
JWT tokens generated
```

---

# 39. PASSWORD HASHING

The project uses:

```python
User.objects.create_user(...)
```

instead of:

```python
User.objects.create(password=...)
```

Why?

Because `create_user()` uses Django's password hashing system.

The database should contain a password hash, not the original password.

---

# 40. SERIALIZERS

Serializers are a core Django REST Framework concept.

They convert:

```text
Python/Django objects
        ↕
JSON
```

They also validate incoming data.

---

# 41. USER SERIALIZER

The UserSerializer controls what user information is returned.

For example:

```text
id
username
email
first_name
last_name
```

The password is deliberately not returned.

---

# 42. REGISTER SERIALIZER

RegisterSerializer accepts:

```text
username
email
password
first_name
last_name
```

The password is:

```python
write_only=True
```

meaning it can be submitted but won't be returned in API responses.

---

# 43. VALIDATION

Validation ensures that input is acceptable.

Examples:

```text
password too short
invalid email
missing required field
invalid date
invalid relationship
```

DRF can automatically return:

```json
{
  "password": [
    "This field must be at least 8 characters."
  ]
}
```

---

# 44. VIEWS

A Django REST Framework view handles an API request.

For example:

```text
POST /api/auth/login/
```

is routed to a view.

The view determines:

```text
What should happen?
```

---

# 45. URL ROUTING

The project's root URLs connect application URLs.

Conceptually:

```text
/api/auth/
      ↓
accounts.urls

/api/profile/
      ↓
profiles.urls

/api/careers/
      ↓
careers.urls

/api/assessments/
      ↓
assessments.urls

/api/recommendations/
      ↓
recommendations.urls

/api/roadmaps/
      ↓
roadmaps.urls

/api/counselor/
      ↓
counselor.urls
```

This keeps routing organized.

---

# 46. MIDDLEWARE

Middleware sits between the incoming request and Django's view.

Conceptually:

```text
Request
   ↓
Middleware
   ↓
URL routing
   ↓
View
   ↓
Response
   ↑
Middleware
   ↑
Client
```

Middleware can handle:

* security
* sessions
* authentication
* CORS
* common HTTP behavior

---

# 47. CORS

CORS means:

**Cross-Origin Resource Sharing.**

Example:

```text
Frontend:
http://localhost:5173

Backend:
http://127.0.0.1:8000
```

Browser security normally restricts cross-origin requests.

Django's CORS configuration tells the browser which frontend origins are allowed.

---

# 48. PROFILE SYSTEM

The profile contains career-related information.

Important categories:

### Personal

```text
date of birth
gender
phone
location
bio
```

### Education

```text
education level
school/college
course
branch
stream
graduation year
field of study
```

### Career

```text
career interests
skills
career goal
experience level
preferred work style
preferred career field
```

---

# 49. PROFILE COMPLETION

The profile has a completion percentage.

Conceptually:

```text
filled fields
     ÷
required/selected completion fields
     ×
100
```

Example:

```text
8 completed fields
10 total completion fields

8 / 10 × 100
= 80%
```

The current implementation uses equal weighting.

---

# 50. EDUCATION SYSTEM

The education app provides structured reference data.

The ZIP includes concepts such as:

```text
Education Level
Stream
Degree
Branch
Course
Field of Study
```

Instead of making users type everything manually, the frontend can request:

```text
GET /api/education/levels/
GET /api/education/streams/
GET /api/education/degrees/
GET /api/education/branches/
GET /api/education/courses/
GET /api/education/fields/
```

This gives the frontend standardized data.

---

# 51. WHY REFERENCE DATA?

Suppose one user writes:

```text
Computer Science
```

and another:

```text
computer science
```

and another:

```text
CS
```

Free text makes matching harder.

Structured reference data gives consistent values.

---

# 52. CAREER KNOWLEDGE BASE

The Career model represents a career.

It contains information such as:

```text
title
slug
description
category
industry
education requirements
required skills
preferred skills
work environment
experience level
salary information
growth outlook
related careers
entrepreneurship relevance
```

---

# 53. SLUG

A slug is a URL-friendly identifier.

Example:

```text
Software Engineer
```

becomes:

```text
software-engineer
```

Then:

```text
/api/careers/slug/software-engineer/
```

can identify the career.

---

# 54. CAREER SEARCH

The API supports:

```text
GET /api/careers/
```

and:

```text
GET /api/careers/search/?q=...
```

This allows the frontend to implement career discovery.

---

# 55. FILTERING

Career APIs can filter data.

Conceptually:

```text
category
industry
experience level
```

This is useful for exploration.

---

# 56. ASSESSMENTS

The assessment system is structured like:

```text
Assessment
    ↓
Question
    ↓
Option
```

A user creates:

```text
AssessmentAttempt
```

and submits:

```text
Answer
```

The backend calculates:

```text
AssessmentResult
```

---

# 57. ASSESSMENT FLOW

```text
User selects assessment
        ↓
POST /start/
        ↓
Attempt created
        ↓
User answers questions
        ↓
POST /answer/
        ↓
Answers stored
        ↓
User submits
        ↓
POST /submit/
        ↓
Scoring service
        ↓
Result generated
```

---

# 58. WHY SCORING SHOULD BE ON BACKEND

The frontend should not determine the final result.

Bad architecture:

```text
Frontend
   ↓
calculates score
```

A user could manipulate frontend code.

Better:

```text
Frontend
   ↓
answers
   ↓
Backend
   ↓
validates
   ↓
scores
   ↓
result
```

---

# 59. PREVENTING CHEATING

The backend should not expose:

```text
is_correct
```

in the user-facing option serializer.

Otherwise someone could inspect the API response and see correct answers.

The project intentionally separates internal correctness from public option data.

---

# 60. ASSESSMENT VALIDATION

When an answer is submitted, the selected option should belong to the question.

Conceptually:

```python
Option.objects.get(
    id=option_id,
    question=question
)
```

This prevents:

```text
Question 1
   ↓
Option from Question 99
```

---

# 61. RECOMMENDATION ENGINE

This is one of the most important parts of the application.

The recommendation engine combines profile information and career information.

The current engine is deterministic.

That means the same input should produce the same score.

---

# 62. RECOMMENDATION WEIGHTS

The current design uses approximately:

```text
Education      25%
Skills         30%
Interests      25%
Work style     10%
Career goal    10%
```

Total:

```text
100%
```

These weights are business rules.

They are not produced by Gemini.

---

# 63. WHY DETERMINISTIC RECOMMENDATIONS?

Because recommendation logic should be:

```text
repeatable
explainable
testable
debuggable
```

If a user asks:

> Why did you recommend Software Engineering?

the system can show:

```text
Skills match: 24/30
Education match: 20/25
Interest match: 22/25
Work style: 8/10
Career goal: 7/10
```

This is more transparent than:

> AI said so.

---

# 64. CURRENT RECOMMENDATION ENGINE LIMITATION

The current matching is relatively simple.

For example, it can use text overlap.

But human language is more complex.

These concepts may be related:

```text
Artificial Intelligence
Machine Learning
AI
ML
Data Science
```

Simple string matching may not understand their semantic relationship.

---

# 65. FUTURE RECOMMENDATION ENGINE

A future architecture could be:

```text
Profile
   ↓
Rule-based scoring
   +
Structured career data
   +
Assessment results
   +
Semantic similarity
   ↓
Hybrid recommendation
   ↓
AI explanation
```

The AI should preferably explain the recommendation rather than blindly determine everything.

---

# 66. ROADMAP SYSTEM

The roadmap system separates templates from user progress.

Template:

```text
Roadmap
   ↓
Stage
   ↓
Task
```

User-specific copy/progress:

```text
UserRoadmap
   ↓
UserTaskProgress
```

---

# 67. EXAMPLE ROADMAP

For Software Engineering:

```text
Stage 1
Programming Fundamentals

Tasks:
- Learn Python
- Learn Git
- Solve basic problems

Stage 2
Web Development

Tasks:
- HTML
- CSS
- JavaScript
- React

Stage 3
Backend

Tasks:
- Django
- REST API
- PostgreSQL

Stage 4
Projects

Tasks:
- Build portfolio
- Deploy project
- Prepare resume
```

---

# 68. ROADMAP PROGRESS

The backend calculates progress based on completed tasks.

Example:

```text
10 tasks
6 completed

Progress:
60%
```

---

# 69. ROADMAP GENERATION ENDPOINT

The current endpoint is named:

```text
POST /api/roadmaps/generate/
```

but its current behavior is essentially assigning an existing roadmap to a user.

So conceptually it is closer to:

```text
assign/start roadmap
```

than true AI/dynamic roadmap generation.

This distinction is important when explaining the project.

---

# 70. AI COUNSELOR

The AI counselor provides conversational guidance.

Endpoint:

```text
POST /api/counselor/chat/
```

Other endpoints:

```text
GET /api/counselor/conversations/
GET /api/counselor/conversations/<id>/
```

---

# 71. AI ARCHITECTURE

The important architecture is:

```text
Django View
     ↓
Counselor Service
     ↓
AI Provider Interface
     ↓
Gemini Provider
```

There is also:

```text
Mock AI Provider
```

for tests.

---

# 72. WHY USE AN AI PROVIDER ABSTRACTION?

Without abstraction:

```text
View
 ↓
Gemini API
```

Changing AI provider becomes difficult.

With abstraction:

```text
View
 ↓
Service
 ↓
BaseAIProvider
      ├── GeminiProvider
      └── MockAIProvider
```

You can replace the implementation without rewriting the API layer.

---

# 73. ABSTRACT BASE CLASS

The project defines an abstract provider concept.

Conceptually:

```python
class BaseAIProvider(ABC):
    @abstractmethod
    def chat(...):
        pass
```

This defines the contract.

Any AI provider should implement:

```text
chat()
```

---

# 74. MOCK AI

MockAIProvider is used for tests.

It does not call the internet.

It returns predictable responses.

Why is this important?

Because automated tests should not depend on:

```text
internet
API availability
API cost
API rate limits
API keys
AI randomness
```

---

# 75. GEMINI PROVIDER

The Gemini provider uses an API key from:

```env
GEMINI_API_KEY=...
```

The key must remain on the backend.

The frontend should never receive it.

---

# 76. AI SYSTEM PROMPT

The counselor service defines instructions such as:

```text
You are a career counselor.
Help with education and career decisions.
Provide practical next steps.
Do not promise guaranteed outcomes.
Do not provide medical/legal/financial advice.
Do not reveal other users' information.
```

This is called a system prompt/instruction layer.

---

# 77. USER CONTEXT

The counselor builds context from the user's profile.

For example:

```text
User: Aviral
Education level: 12th
Career interests: technology
Skills: Python
Career goal: software engineering
Experience: beginner
```

This context is passed to the AI.

Therefore:

```text
Generic AI
```

becomes:

```text
Personalized AI counselor
```

---

# 78. CONVERSATION MODEL

The AI system stores:

```text
Conversation
```

and:

```text
Message
```

A conversation can contain:

```text
User message
Assistant message
User message
Assistant message
...
```

The `Message` model contains:

```text
conversation
role
content
created_at
```

---

# 79. AI CONVERSATION FLOW

```text
User asks question
        ↓
Find/create conversation
        ↓
Save user message
        ↓
Load conversation history
        ↓
Build profile context
        ↓
Build system prompt
        ↓
Call AI provider
        ↓
Receive response
        ↓
Save assistant message
        ↓
Return JSON
```

---

# 80. IMPORTANT AI LIMITATION

The current AI implementation in the ZIP uses the `google-generativeai` package and a Gemini model configuration.

It should not be described as a Google ADK implementation.

The correct explanation is:

> "The project currently has an AI provider abstraction with Gemini and mock implementations. Google ADK can be introduced later as the agent orchestration layer."

---

# 81. AI VS RECOMMENDATION ENGINE

These are different.

### Recommendation engine

```text
structured inputs
       ↓
rules/scoring
       ↓
career recommendations
```

### AI counselor

```text
conversation
       ↓
context
       ↓
LLM
       ↓
natural-language guidance
```

They complement each other.

---

# 82. WHY NOT USE AI FOR EVERYTHING?

Because AI can be:

```text
non-deterministic
harder to test
expensive
occasionally incorrect
difficult to explain
```

Business rules such as scoring are often better handled deterministically.

AI can then explain the result.

---

# 83. COMMON PERMISSIONS

The project contains reusable permission logic.

The concept:

```text
IsOwnerOrReadOnly
```

means:

```text
GET
HEAD
OPTIONS
```

can be read safely,

while modifying an object requires ownership.

---

# 84. OBJECT OWNERSHIP

Example:

```text
User A
  ↓
Recommendation 1
```

User B should not be able to access:

```text
/api/recommendations/1/
```

if Recommendation 1 belongs to User A.

Therefore querysets should be scoped to:

```python
user=request.user
```

---

# 85. AUTHENTICATED API

Protected endpoints require:

```text
Authorization: Bearer <access-token>
```

If there is no valid token:

```text
401 Unauthorized
```

---

# 86. PAGINATION

The project defines:

```text
20 results per page
```

with:

```text
maximum 100
```

Example:

```text
/api/careers/?page=2
```

or:

```text
/api/careers/?page=1&page_size=50
```

Pagination prevents the server from returning thousands of objects at once.

---

# 87. THROTTLING

Throttling limits API request rates.

The project configures anonymous and authenticated request limits.

Why?

To reduce:

```text
abuse
accidental overload
automated spam
resource exhaustion
```

AI endpoints deserve particularly careful throttling because AI calls can be expensive.

---

# 88. LOGGING

Logging records useful server events.

For example:

```text
error
warning
information
```

Instead of using:

```python
print()
```

production applications should use logging.

---

# 89. ERROR HANDLING

The project contains shared exception handling concepts.

A good API should return structured errors.

Example:

```json
{
  "detail": "Refresh token is required."
}
```

rather than crashing and exposing internal details.

---

# 90. TEST SETTINGS

The project contains:

```text
config/test_settings.py
```

which uses SQLite for tests.

This allows tests to run without requiring the real PostgreSQL server.

Conceptually:

```text
Development
    ↓
PostgreSQL

Tests
    ↓
SQLite in-memory
```

---

# 91. WHY USE MOCK AI IN TESTS?

Imagine a test calls Gemini.

Then the test depends on:

```text
internet
API key
Gemini availability
rate limits
response variability
```

That's bad.

Mock provider gives:

```text
same input
    ↓
predictable output
```

This makes tests stable.

---

# 92. TESTING PYRAMID

A mature project normally has:

```text
          E2E tests
        /           \
     API tests     Integration
       /               \
     Unit tests / service tests
```

The ZIP contains many tests across the application modules.

But the actual pass result must be verified in the environment.

---

# 93. WHAT TO TEST

### Authentication

Test:

```text
registration
duplicate user
login
invalid password
refresh
logout
blacklisted token
/me
```

### Profile

Test:

```text
get profile
update profile
partial update
validation
ownership
completion percentage
```

### Careers

Test:

```text
list
detail
slug
search
filters
pagination
```

### Assessments

Test:

```text
start
answer
invalid option
submit
result
ownership
```

### Recommendations

Test:

```text
generation
score calculation
breakdown
ownership
```

### Roadmaps

Test:

```text
assignment
progress
ownership
```

### Counselor

Test:

```text
conversation creation
history
mock provider
error handling
ownership
```

---

# 94. UNIT TEST VS INTEGRATION TEST

### Unit test

Tests one small component.

Example:

```text
calculate_score()
```

### Integration test

Tests multiple components together.

Example:

```text
API request
 ↓
serializer
 ↓
database
 ↓
service
 ↓
response
```

---

# 95. TESTING AND DETERMINISTIC LOGIC

The recommendation engine is especially suitable for testing.

Example:

```text
same profile
+
same career
=
same score
```

That makes it easier to write reliable tests.

---

# 96. SECURITY

Important security areas:

```text
authentication
authorization
password hashing
secret management
CORS
CSRF
HTTPS
secure cookies
host validation
rate limiting
input validation
ownership checks
```

---

# 97. PASSWORD SECURITY

Never store:

```text
password123
```

directly.

Django stores a password hash.

---

# 98. API KEY SECURITY

Never:

```javascript
const GEMINI_API_KEY = "real-key";
```

in frontend code.

Instead:

```text
Frontend
   ↓
Django API
   ↓
Gemini
```

The Gemini key remains on the server.

---

# 99. CSRF

CSRF means:

**Cross-Site Request Forgery.**

Django provides CSRF protection.

For token-based APIs, authentication and CSRF behavior must be understood according to the authentication mechanism being used.

The important lesson is:

> Don't simply disable CSRF globally because an API request fails.

Understand which authentication mechanism the endpoint uses.

---

# 100. CORS VS CSRF

They are different.

### CORS

Controls:

> Which origins can make browser cross-origin requests?

### CSRF

Protects against:

> Unauthorized actions performed using a user's authenticated browser context.

Do not confuse them.

---

# 101. DEVELOPMENT VS PRODUCTION

Development:

```text
DEBUG=True
localhost
development database
console/email development tools
```

Production:

```text
DEBUG=False
HTTPS
real domain
secure cookies
production database
real email service
logging/monitoring
proper secret management
```

---

# 102. WSGI AND ASGI

Django includes:

```text
wsgi.py
asgi.py
```

### WSGI

Traditional synchronous Python web server interface.

### ASGI

Modern asynchronous server interface.

Useful for:

```text
async workloads
WebSockets
real-time applications
```

The current project includes both because Django provides them as standard deployment interfaces.

---

# 103. API DOCUMENTATION

Your API structure can be documented using:

```text
endpoint
method
authentication
request body
response
status codes
```

Example:

```text
POST /api/auth/register/

Request:
{
  username,
  email,
  password
}

Response:
{
  user,
  tokens
}
```

This becomes the contract between frontend and backend.

---

# 104. API CONTRACT

The frontend and backend must agree on:

```text
URL
HTTP method
request format
response format
authentication
error format
status codes
```

For example:

```text
Frontend expects:
career.title
```

Backend should consistently return:

```json
{
  "title": "Software Engineer"
}
```

---

# 105. FRONTEND-BACKEND COMMUNICATION

The overall flow:

```text
User clicks Login
       ↓
React collects email/password
       ↓
POST /api/auth/login/
       ↓
Django validates
       ↓
JWT returned
       ↓
Frontend stores/uses authentication state
       ↓
Frontend calls protected APIs
       ↓
Bearer token
       ↓
Django authenticates
       ↓
JSON response
       ↓
React displays data
```

---

# 106. COMPLETE USER FLOW

A realistic Career Counselor Lite user journey:

```text
Register
   ↓
Login
   ↓
Profile created
   ↓
Complete profile
   ↓
Select education
   ↓
Explore careers
   ↓
Take assessment
   ↓
Receive assessment result
   ↓
Generate career recommendations
   ↓
Choose a career direction
   ↓
Start roadmap
   ↓
Track progress
   ↓
Ask AI counselor questions
```

This is how all backend modules connect.

---

# 107. COMPLETE SYSTEM FLOW

```text
                    USER
                     |
                     ↓
                 FRONTEND
                     |
                     ↓
                REST API
                     |
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
    Accounts      Profile       Education
       |             |             |
       └─────────────┼─────────────┘
                     ↓
                Career Data
                     ↓
                Assessment
                     ↓
             Recommendation
                     ↓
                  Roadmap
                     ↓
              AI Counselor
                     |
                     ↓
                 PostgreSQL
```

---

# 108. WHY THIS ARCHITECTURE IS GOOD

Each layer has a responsibility.

```text
Frontend
    → presentation

API/View
    → request handling

Serializer
    → validation + representation

Service
    → business logic

Model
    → database representation

Database
    → persistent storage

AI Provider
    → external AI integration
```

This makes the system easier to maintain.

---

# 109. SERVICE LAYER

The project uses service modules for complex business logic.

Examples:

```text
assessments/services.py
recommendations/services.py
counselor/services.py
```

This is useful because views shouldn't become giant files.

Bad:

```text
View
 ├── validate
 ├── calculate
 ├── database operations
 ├── AI calls
 ├── recommendation logic
 └── response
```

Better:

```text
View
  ↓
Service
  ↓
business logic
```

---

# 110. RECOMMENDATION SERVICE

The recommendation service can perform:

```text
profile retrieval
career retrieval
score calculation
breakdown generation
recommendation persistence
```

This is business logic, so putting it in a service makes sense.

---

# 111. ASSESSMENT SERVICE

The assessment service handles:

```text
attempt creation
answer validation
scoring
result generation
```

Again, this is business logic rather than simple request routing.

---

# 112. COUNSELOR SERVICE

The counselor service handles:

```text
conversation creation
message saving
history retrieval
profile context
system prompt
AI provider call
assistant message storage
```

The view should not contain all of that.

---

# 113. DATA LIFECYCLE

Consider a new user.

### Step 1

User registers.

```text
POST /api/auth/register/
```

### Step 2

User is stored.

### Step 3

Profile is automatically created.

### Step 4

User completes profile.

### Step 5

Profile information becomes input to recommendations.

### Step 6

Assessment results provide additional information.

### Step 7

Recommendation engine combines information.

### Step 8

User starts roadmap.

### Step 9

AI counselor uses profile/context to answer questions.

This demonstrates how the modules work together.

---

# 114. IMPORTANT BUSINESS LOGIC DISTINCTION

The backend has three different kinds of information:

## Reference data

Examples:

```text
education levels
career catalog
roadmaps
assessment definitions
```

## User data

Examples:

```text
profile
assessment attempts
recommendations
progress
conversations
```

## Derived data

Examples:

```text
assessment results
recommendation scores
profile completion
roadmap progress
```

Understanding this distinction is useful for database design.

---

# 115. COMMON PROFESSOR QUESTION

## "Why PostgreSQL instead of SQLite?"

Answer:

> SQLite is excellent for local development and lightweight testing, but PostgreSQL is a stronger choice for a multi-user production application because it provides a full relational database system, concurrency support, stronger production features, indexing, constraints, and scalability options.

The project uses SQLite for test settings and PostgreSQL for the actual application database.

---

# 116. "Why Django?"

Answer:

> Django provides authentication foundations, ORM, migrations, admin, middleware, security features, and a mature application structure. It allows me to focus on the application's career-domain logic instead of implementing fundamental web infrastructure myself.

---

# 117. "Why Django REST Framework?"

Answer:

> Django REST Framework provides serializers, API views, authentication integration, permissions, pagination, throttling, validation, and structured JSON API development.

---

# 118. "Why JWT?"

Answer:

> JWT provides token-based authentication suitable for a frontend/mobile client communicating with a REST API. The backend issues access and refresh tokens, and protected requests use the access token.

---

# 119. "Why separate User and Profile?"

Answer:

> The User model handles identity and authentication, while Profile contains career-specific personal and educational information. Separating them keeps authentication concerns independent from domain-specific profile data.

---

# 120. "Why use serializers?"

Answer:

> Serializers translate Django/Python objects into JSON responses and validate incoming JSON data before it reaches business logic.

---

# 121. "Why use services?"

Answer:

> Services keep business logic separate from HTTP request handling. This makes the code easier to test, reuse, maintain, and understand.

---

# 122. "Why use MockAIProvider?"

Answer:

> Tests should not depend on external AI APIs, internet connectivity, API keys, cost, or nondeterministic responses. The mock provider gives predictable responses while maintaining the same provider interface.

---

# 123. "Why not let Gemini make the recommendation directly?"

Answer:

> The core recommendation logic is deterministic because it needs to be explainable, reproducible, and testable. AI can be used later to provide natural-language explanations and personalized counseling around those results.

---

# 124. "What is the difference between AI and recommendation engine?"

Answer:

> The recommendation engine is a deterministic business-rule system that calculates career matches using structured user and career information. The AI counselor is a conversational language model that provides natural-language guidance using user context and conversation history.

---

# 125. "What is a migration?"

Answer:

> A migration is Django's version-controlled representation of database schema changes. `makemigrations` creates migration files from model changes, while `migrate` applies those changes to the database.

---

# 126. "What happens when a user logs in?"

Answer:

```text
User sends credentials
        ↓
Login endpoint
        ↓
Django validates credentials
        ↓
JWT access + refresh tokens
        ↓
Frontend receives tokens
        ↓
Access token used for protected APIs
```

---

# 127. "What happens when the access token expires?"

Answer:

```text
Access token expires
       ↓
Frontend uses refresh token
       ↓
POST /api/auth/token/refresh/
       ↓
New access token
```

---

# 128. "How do you prevent one user from accessing another user's data?"

Answer:

> Protected querysets and object-level ownership checks scope user-specific resources to `request.user`. For example, recommendations, conversations, assessment attempts, and user roadmaps are queried against the authenticated user.

---

# 129. "How does profile completion work?"

Answer:

> The profile defines a set of completion fields. The backend checks which fields are populated, calculates the proportion completed, and exposes the resulting completion percentage.

---

# 130. "How are careers recommended?"

Answer:

> The current recommendation engine uses deterministic weighted matching across education, skills, interests, work style, and career goals. Each area contributes to an overall score and the system stores a scoring breakdown.

---

# 131. "Is the recommendation AI?"

Answer:

> The core recommendation scoring is not dependent on an LLM. It is rule-based and deterministic. The AI counselor is a separate layer used for conversational guidance.

---

# 132. "How does AI know the user's profile?"

Answer:

```text
Authenticated user
      ↓
Profile lookup
      ↓
Relevant profile fields
      ↓
Context construction
      ↓
System prompt
      ↓
AI provider
```

---

# 133. "Where is the Gemini key?"

Answer:

> It is configured as a backend environment variable and should never be exposed to the frontend.

---

# 134. "Can the AI provider be replaced?"

Answer:

> Yes. The project uses an abstract AI provider interface with separate provider implementations. This allows the Gemini implementation to be replaced or another provider to be added without changing the counselor API layer.

---

# 135. "What is an API?"

Answer:

> An API is an interface through which software systems communicate. In this project, the frontend communicates with Django through REST API endpoints using HTTP requests and JSON responses.

---

# 136. "What is an endpoint?"

An endpoint is a specific API URL that performs a particular operation.

Example:

```text
POST /api/auth/register/
```

is a registration endpoint.

---

# 137. "What is authentication?"

Authentication determines identity.

```text
Who are you?
```

---

# 138. "What is authorization?"

Authorization determines permissions.

```text
What are you allowed to access?
```

---

# 139. "What is ORM?"

ORM means Object Relational Mapping.

It maps:

```text
Python objects
       ↕
Database tables
```

---

# 140. "What is a serializer?"

A serializer:

```text
JSON → Python/validated data
Python/Django object → JSON
```

---

# 141. "What is middleware?"

Middleware is code that processes requests/responses around the view layer.

---

# 142. "What is CORS?"

CORS controls browser permission for cross-origin requests.

---

# 143. "What is pagination?"

Pagination divides a large result set into smaller pages.

Example:

```text
1–20
21–40
41–60
```

---

# 144. "What is throttling?"

Throttling limits how frequently clients can call an API.

---

# 145. "What is a foreign key?"

A ForeignKey creates a many-to-one database relationship.

Example:

```text
Many messages
      ↓
One conversation
```

---

# 146. "What is OneToOneField?"

It creates a one-to-one relationship.

Example:

```text
One User
   ↕
One Profile
```

---

# 147. "What is TextChoices?"

Django's `TextChoices` allows predefined choices.

For example:

```text
USER
ASSISTANT
SYSTEM
```

This prevents arbitrary role values from being used.

---

# 148. "Why use indexes?"

Indexes make certain database queries faster.

They are particularly useful for frequently searched or filtered fields.

But indexes also have a cost:

```text
more storage
slower writes
```

Therefore they should be based on actual query patterns.

---

# 149. "What is production readiness?"

Production readiness means more than:

```text
the application runs
```

It includes:

```text
security
testing
logging
monitoring
error handling
configuration
database reliability
deployment
performance
backups
secrets
documentation
```

---

# 150. CURRENT PROJECT LIMITATIONS YOU SHOULD KNOW

Do not claim the ZIP is perfect.

Important limitations identified during analysis:

## Dependency mismatch

The ZIP's requirements specify:

```text
Django 5.1.4
```

while some migration files were generated using:

```text
Django 6.1.1
```

This should be aligned.

---

## Secrets

The ZIP contains:

```text
.env
```

with environment configuration.

Real secrets should never be distributed in an archive or committed to Git.

---

## Gemini implementation

The current ZIP uses:

```text
google-generativeai
```

and a Gemini provider.

It is not currently a Google ADK implementation.

---

## Recommendation matching

The current matching logic is deterministic but relatively simple.

It can later be improved with structured skill relationships and semantic matching.

---

## Roadmap generation

The endpoint called `generate` currently behaves more like assigning an existing roadmap than dynamically generating one.

---

## Test verification

There are 120 test methods in the ZIP.

The README says they passed, but you should run the test suite yourself before claiming that as verified.

---

# 151. WHAT YOU SHOULD LEARN FIRST

Do not try to memorize the entire project at once.

Follow this order.

## Level 1 — Python

Learn:

```text
variables
strings
lists
dictionaries
sets
tuples
functions
classes
inheritance
exceptions
modules
packages
decorators
type hints
```

---

# 152. LEVEL 2 — WEB BASICS

Learn:

```text
HTTP
HTTPS
URL
request
response
headers
body
JSON
cookies
sessions
status codes
REST
API
CORS
CSRF
```

---

# 153. LEVEL 3 — DATABASE

Learn:

```text
database
table
row
column
primary key
foreign key
unique constraint
index
relationship
one-to-one
one-to-many
many-to-many
SQL
transactions
```

---

# 154. LEVEL 4 — DJANGO

Learn:

```text
project
app
settings
URLs
views
models
ORM
migrations
admin
middleware
authentication
signals
```

---

# 155. LEVEL 5 — DRF

Learn:

```text
APIView
GenericAPIView
ViewSet
Serializer
ModelSerializer
permissions
authentication
pagination
throttling
validation
Response
status codes
```

---

# 156. LEVEL 6 — AUTHENTICATION

Learn:

```text
password hashing
JWT
access token
refresh token
token expiration
blacklisting
authentication
authorization
ownership
```

---

# 157. LEVEL 7 — YOUR BUSINESS LOGIC

Learn your actual project:

```text
Profile
Education
Career
Assessment
Recommendation
Roadmap
Counselor
```

Don't just memorize definitions.

Understand how data flows between them.

---

# 158. LEVEL 8 — AI

Learn:

```text
LLM
prompt
system instruction
user message
conversation
context
AI provider
mock provider
Gemini
embeddings
RAG
agents
Google ADK
```

The current project gives you the provider abstraction foundation.

---

# 159. LEVEL 9 — TESTING

Learn:

```text
unit testing
API testing
integration testing
mocking
test database
fixtures
assertions
regression testing
```

---

# 160. LEVEL 10 — PRODUCTION

Learn:

```text
environment variables
Docker
Linux
Gunicorn
Uvicorn
Nginx
HTTPS
PostgreSQL production
logging
monitoring
CI/CD
backups
deployment
```

---

# 161. THE MOST IMPORTANT THING TO UNDERSTAND

Don't memorize:

```text
python manage.py migrate
```

Understand:

```text
models.py
    ↓
model changes
    ↓
makemigrations
    ↓
migration file
    ↓
migrate
    ↓
database schema
```

Likewise, don't memorize:

```text
POST /api/auth/login/
```

Understand:

```text
Frontend
 ↓
HTTP POST
 ↓
URL router
 ↓
Login View
 ↓
authentication
 ↓
JWT generation
 ↓
JSON response
```

---

# 162. THE PROJECT'S COMPLETE DATA FLOW

```text
                 USER
                   |
                   ↓
               FRONTEND
                   |
                   ↓
                HTTP
                   |
                   ↓
            Django REST API
                   |
       ┌───────────┼───────────┐
       ↓           ↓           ↓
    Serializer    Auth       Permission
       |           |           |
       └───────────┼───────────┘
                   ↓
                Service
                   |
                   ↓
                 ORM
                   |
                   ↓
              PostgreSQL
```

For AI:

```text
User
 ↓
Frontend
 ↓
Counselor API
 ↓
Counselor Service
 ↓
Profile Context
 ↓
Conversation History
 ↓
AI Provider
 ↓
Gemini
 ↓
Response
 ↓
Message Database
 ↓
Frontend
```

---

# 163. WHAT YOU SHOULD BE ABLE TO DRAW ON PAPER

Before saying you understand the project, you should be able to draw:

```text
User
 |
 +---- Profile
 |
 +---- AssessmentAttempt
 |          |
 |          +---- Answer
 |
 +---- Recommendation
 |
 +---- UserRoadmap
 |          |
 |          +---- UserTaskProgress
 |
 +---- Conversation
            |
            +---- Message


Assessment
 |
 +---- Question
          |
          +---- Option


Roadmap
 |
 +---- RoadmapStage
          |
          +---- RoadmapTask
```

If you understand this diagram, you understand a large part of the backend architecture.

---

# 164. YOUR 2-MINUTE PROFESSOR EXPLANATION

You can explain the project like this:

> "Career Counselor Lite is a Django REST API backend for a career guidance platform. I designed it using a modular architecture where authentication, profiles, education, careers, assessments, recommendations, roadmaps, and AI counseling are separate Django applications.
>
> The frontend communicates with the backend through REST APIs using JSON. Django REST Framework handles serialization, validation, authentication, permissions, pagination, and throttling.
>
> PostgreSQL is used as the primary relational database, and Django ORM handles communication with the database.
>
> I implemented a custom User model for authentication and separated career-specific information into a Profile model using a one-to-one relationship.
>
> The platform contains structured education and career data, an assessment system with questions, attempts, answers, and results, and a deterministic recommendation engine that scores careers using education, skills, interests, work style, and career goals.
>
> I also implemented roadmap templates with stages and tasks and user-specific progress tracking.
>
> For AI counseling, I created a provider abstraction so the counselor service can work with a mock provider during testing and a Gemini provider in production. The AI receives relevant user profile context and conversation history.
>
> Security is handled through JWT authentication, ownership checks, password hashing, environment variables, CORS configuration, throttling, and production security settings.
>
> The project also contains automated tests across the major modules. Before deployment, I would verify the complete test suite, align dependency versions, rotate any exposed development secrets, and further harden the AI and production configuration."

---

# 165. YOUR MOST IMPORTANT COMMANDS

Activate environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Check Django:

```powershell
python manage.py check
```

Create migrations:

```powershell
python manage.py makemigrations
```

Apply migrations:

```powershell
python manage.py migrate
```

Create admin user:

```powershell
python manage.py createsuperuser
```

Run server:

```powershell
python manage.py runserver
```

Run tests:

```powershell
python manage.py test
```

Run tests with test settings:

```powershell
python manage.py test --settings=config.test_settings --verbosity=2
```

Check migration differences:

```powershell
python manage.py makemigrations --check
```

---

# 166. GIT KNOWLEDGE

You should also understand:

```text
git status
git add
git commit
git push
git pull
git branch
```

`.gitignore` prevents files such as:

```text
.venv
.env
__pycache__
*.pyc
```

from being tracked.

But `.gitignore` does not automatically remove a file that was already committed.

---

# 167. WHAT NOT TO SAY TO YOUR PROFESSOR

Don't say:

> "Gemini generates all the career recommendations."

The current architecture doesn't work that way.

Say:

> "The recommendation engine is deterministic, while the AI counselor provides conversational guidance."

Don't say:

> "Google ADK is implemented."

The ZIP doesn't establish that.

Say:

> "The AI provider abstraction provides the foundation for later ADK/agent integration."

Don't say:

> "The backend is 100% production ready."

Instead:

> "The major backend functionality is implemented, with remaining stabilization and production-hardening work."

---

# 168. FINAL MENTAL MODEL

Remember these seven layers:

```text
1. USER
   ↓
2. FRONTEND
   ↓
3. REST API
   ↓
4. DJANGO / DRF
   ↓
5. BUSINESS LOGIC
   ↓
6. ORM
   ↓
7. POSTGRESQL
```

AI adds:

```text
Business Logic
      ↓
AI Provider
      ↓
Gemini
```

Authentication adds:

```text
Login
 ↓
JWT
 ↓
Authenticated Request
 ↓
Permission
 ↓
Resource
```

---

# 169. THE PROJECT IN ONE SENTENCE

> Career Counselor Lite is a Django REST and PostgreSQL career-guidance backend that manages users and profiles, structured education and career information, assessments, deterministic career recommendations, personalized roadmaps, and an AI counseling layer through a modular service-based architecture.

---

# 170. FINAL LEARNING CHECKLIST

Before you say:

> "I completely understand my backend."

You should be able to explain without looking at notes:

### Python

* [ ] Classes
* [ ] Inheritance
* [ ] Functions
* [ ] Exceptions
* [ ] Modules
* [ ] Decorators

### Django

* [ ] Project vs app
* [ ] Settings
* [ ] URL routing
* [ ] Views
* [ ] Models
* [ ] ORM
* [ ] Migrations
* [ ] Admin
* [ ] Middleware
* [ ] Signals

### Database

* [ ] Table
* [ ] Primary key
* [ ] Foreign key
* [ ] One-to-one
* [ ] Index
* [ ] Constraints
* [ ] Transactions
* [ ] PostgreSQL

### DRF

* [ ] Serializer
* [ ] APIView
* [ ] Generic views
* [ ] Request
* [ ] Response
* [ ] Permissions
* [ ] Authentication
* [ ] Pagination
* [ ] Throttling

### Authentication

* [ ] Password hashing
* [ ] JWT
* [ ] Access token
* [ ] Refresh token
* [ ] Blacklisting
* [ ] Authentication vs authorization

### Project

* [ ] Accounts
* [ ] Profiles
* [ ] Education
* [ ] Careers
* [ ] Assessments
* [ ] Recommendations
* [ ] Roadmaps
* [ ] Counselor

### AI

* [ ] LLM
* [ ] Prompt
* [ ] Context
* [ ] Conversation history
* [ ] Provider abstraction
* [ ] Mock provider
* [ ] Gemini
* [ ] Difference between recommendation engine and AI counselor
* [ ] Future ADK integration

### Production

* [ ] Environment variables
* [ ] DEBUG
* [ ] ALLOWED_HOSTS
* [ ] CORS
* [ ] CSRF
* [ ] HTTPS
* [ ] Secrets
* [ ] Logging
* [ ] Testing
* [ ] Deployment
* [ ] Backups

---

# 171. THE BEST WAY TO STUDY THIS PROJECT

Do not read these notes once and try to memorize them.

Use this cycle:

```text
READ CONCEPT
     ↓
FIND IT IN YOUR CODE
     ↓
RUN IT
     ↓
BREAK IT INTENTIONALLY
     ↓
SEE THE ERROR
     ↓
FIX IT
     ↓
EXPLAIN IT WITHOUT LOOKING
```

For example:

```text
Learn JWT
 ↓
Find SimpleJWT settings
 ↓
Run login API
 ↓
Inspect access token
 ↓
Call /me
 ↓
Remove token
 ↓
See 401
 ↓
Understand why
 ↓
Explain authentication
```

That will teach you much more effectively than memorizing the README.

# FINAL RESULT

The backend gives you a very good learning project because it contains almost the complete journey:

```text
Python
  ↓
Django
  ↓
Database
  ↓
ORM
  ↓
REST API
  ↓
Authentication
  ↓
Authorization
  ↓
Business Logic
  ↓
Testing
  ↓
AI Integration
  ↓
Production Engineering
```

The most important thing now is **not to add more features immediately**.

First learn and verify the existing system.

The best next learning sequence is:

```text
1. Python fundamentals
2. HTTP + REST + JSON
3. PostgreSQL + SQL
4. Django fundamentals
5. Django ORM
6. Models + relationships
7. Migrations
8. Django REST Framework
9. Serializers
10. Views + URLs
11. JWT authentication
12. Permissions
13. Profile module
14. Education + Career modules
15. Assessments
16. Recommendation engine
17. Roadmaps
18. AI provider architecture
19. Gemini
20. Testing
21. Security
22. Deployment
23. Google ADK / agents
```

Once you can explain each layer **and point to the corresponding code in your project**, you can legitimately say that you built and understand the backend rather than merely having generated it.
