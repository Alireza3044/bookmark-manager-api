# Bookmark Manager API

A robust RESTful API built with Django REST Framework (DRF) for organizing and managing web bookmarks into nested categories, complete with token-based user authentication, bookmark favoriting, and summary analytics.

<!-- Optional: Add an API overview diagram or Postman/Swagger screenshot here -->
<!-- ![API Overview](path/to/demo.png) -->

---

## Features

* **Token-Based Authentication:** Complete user registration, login (token retrieval), and logout workflows.
* **Nested Resource Architecture:** Category-driven bookmark management implemented via DRF nested routers.
* **Global & Filtered Views:** Access category-specific bookmark lists or fetch global user bookmarks across all categories.
* **Favorite Toggle:** Dedicated endpoint for favoriting/unfavoriting key bookmarks.
* **Summary Analytics:** Aggregated insights and metrics for user categories and bookmarks.
* **User-Isolated Access:** Permission enforcement ensuring users only view and modify their own bookmarks and categories.

---

## Tech Stack

* **Backend:** Django, Django REST Framework (DRF)
* **Authentication:** DRF Token Authentication (`rest_framework.authtoken`)
* **Routing:** `drf-nested-routers`
* **Database:** PostgreSQL

---

## API Endpoints Reference

### Authentication

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/api/auth/register/` | `POST` | Register a new user account |
| `/api/auth/login/` | `POST` | Authenticate credentials and receive an auth token |
| `/api/auth/logout/` | `POST` | Revoke current user authentication token |

### Categories & Bookmarks

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/api/categories/` | `GET`, `POST` | List all user categories or create a new category |
| `/api/categories/{id}/` | `GET`, `PUT`, `DELETE` | Retrieve, update, or delete a specific category |
| `/api/categories/{category_pk}/bookmarks/` | `GET`, `POST` | List bookmarks within a category or create a nested bookmark |
| `/api/categories/{category_pk}/bookmarks/{id}/` | `GET`, `PUT`, `DELETE` | Retrieve, update, or delete a category-nested bookmark |
| `/api/bookmarks/` | `GET` | List all global bookmarks across all categories |
| `/api/favorite/{id}/` | `POST` | Toggle favorite status for a target bookmark |
| `/api/summary/` | `GET` | Retrieve summary stats for user categories and bookmarks |

---

## Getting Started

### Prerequisites
* Python 3.12+
* Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alireza3044/bookmark-manager-api.git
   cd bookmark-manager-api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True

   # Database Settings
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
   > **Note:** To generate a secure `SECRET_KEY`, run:
   > `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
