# HRMS Lite (Full-Stack Assignment)

Lightweight HRMS app to manage **employees** and track **daily attendance**.

## Tech stack
- **Frontend**: React + Vite + Axios
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL

## Features
- **Employee management**
  - Add employee (unique employee ID, full name, email, department)
  - List employees
  - Delete employee
- **Attendance management**
  - Mark attendance (Present/Absent) for an employee on a date
  - View attendance records (filter by employee and date)

## Project structure
- `hrms-frontend/`: frontend (Vite)
- `hrms_backend/`, `employee/`, `attendance/`, `common/`: backend (Django project + apps)

## Run locally

### Backend (Django)
Prereqs: Python 3.x, PostgreSQL running locally.

1) Create and activate a virtual env

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Configure environment variables (PowerShell example)

```powershell
$env:DJANGO_DEBUG="1"
$env:DB_NAME="hrms"
$env:DB_USER="postgres"
$env:DB_PASSWORD="admin"
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
```

4) Run migrations and start server

```bash
python manage.py migrate
python manage.py runserver
```

Backend base URL: `http://127.0.0.1:8000/api`

### Frontend (React)
Prereqs: Node.js 18+

```bash
cd hrms-frontend
npm install
```

Create `hrms-frontend/.env`:

```bash
VITE_API_URL=http://127.0.0.1:8000/api
```

Start dev server:

```bash
npm run dev
```

## API endpoints (summary)
- `GET /api/employees/` (paginated)
- `POST /api/employees/`
- `DELETE /api/employees/{id}/`
- `GET /api/attendance/?employee_id=&date=` (paginated)
- `POST /api/attendance/`

## Assumptions / limitations
- Single admin user (no authentication).
- Production hardening (CSRF strategy, restricted CORS/hosts, secrets, logging) should be configured via environment variables when deploying.

